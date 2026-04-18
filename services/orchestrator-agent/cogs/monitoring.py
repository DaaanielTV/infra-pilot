import discord
from discord.ext import commands, tasks
import psutil
import docker
import mysql.connector
from datetime import datetime, timedelta
import asyncio
import json
from typing import Dict, List, Optional
import logging
from .vps_manager import VPSManager
import matplotlib.pyplot as plt
import io
import os

class Monitoring(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.docker_client = docker.from_env()
        self.vps_manager = VPSManager()
        self.stats_cache: Dict[str, Dict] = {}
        self.alert_thresholds = {
            'cpu': 90.0,  # 90% CPU usage
            'memory': 90.0,  # 90% Memory usage
            'disk': 90.0,  # 90% Disk usage
            'network': 90.0  # 90% Network bandwidth
        }
        self.monitoring_loop.start()
        self.db_connection = self.connect_to_database()
        self.update_status.start()
        
    def connect_to_database(self):
        return mysql.connector.connect(
            host=self.bot.config['db_host'],
            user=self.bot.config['db_user'],
            password=self.bot.config['db_password'],
            database=self.bot.config['db_name']
        )

    def cog_unload(self):
        self.monitoring_loop.cancel()
        self.update_status.cancel()
        if self.db_connection:
            self.db_connection.close()

    @tasks.loop(minutes=1)
    async def monitoring_loop(self):
        try:
            containers = self.docker_client.containers.list()
            for container in containers:
                stats = self.get_container_stats(container)
                if stats:
                    self.stats_cache[container.id] = stats
                    await self.check_alerts(container.id, stats)
                    await self.update_database_stats(container.id, stats)
        except Exception as e:
            logging.error(f"Error in monitoring loop: {str(e)}")

    def get_container_stats(self, container) -> Optional[Dict]:
        try:
            stats = container.stats(stream=False)
            
            # Calculate CPU usage
            cpu_delta = stats["cpu_stats"]["cpu_usage"]["total_usage"] - \
                       stats["precpu_stats"]["cpu_usage"]["total_usage"]
            system_delta = stats["cpu_stats"]["system_cpu_usage"] - \
                          stats["precpu_stats"]["system_cpu_usage"]
            cpu_usage = (cpu_delta / system_delta) * 100.0 if system_delta > 0 else 0.0

            # Calculate memory usage
            memory_usage = stats["memory_stats"]["usage"]
            memory_limit = stats["memory_stats"]["limit"]
            memory_percent = (memory_usage / memory_limit) * 100.0

            # Calculate network usage
            network_stats = stats["networks"]["eth0"]
            rx_bytes = network_stats["rx_bytes"]
            tx_bytes = network_stats["tx_bytes"]

            # Get disk usage
            disk_stats = container.exec_run("df -h /").output.decode()
            disk_percent = float(disk_stats.split()[11].strip('%'))

            return {
                'timestamp': datetime.now().isoformat(),
                'container_id': container.id,
                'name': container.name,
                'status': container.status,
                'cpu_usage': round(cpu_usage, 2),
                'memory_usage': round(memory_percent, 2),
                'memory_used': memory_usage,
                'memory_total': memory_limit,
                'network': {
                    'rx_bytes': rx_bytes,
                    'tx_bytes': tx_bytes
                },
                'disk_usage': disk_percent
            }
        except Exception as e:
            logging.error(f"Error getting stats for container {container.id}: {str(e)}")
            return None

    async def update_database_stats(self, container_id: str, stats: Dict):
        try:
            cursor = self.db_connection.cursor()
            
            # Update current stats
            query = """
                INSERT INTO vps_statistics 
                (container_id, cpu_usage, memory_usage, memory_used, memory_total, 
                network_rx, network_tx, disk_usage, status, timestamp)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = (
                container_id,
                stats['cpu_usage'],
                stats['memory_usage'],
                stats['memory_used'],
                stats['memory_total'],
                stats['network']['rx_bytes'],
                stats['network']['tx_bytes'],
                stats['disk_usage'],
                stats['status'],
                stats['timestamp']
            )
            cursor.execute(query, values)
            
            # Update peak values if necessary
            peak_query = """
                UPDATE vps_peak_statistics
                SET peak_cpu = GREATEST(peak_cpu, %s),
                    peak_memory = GREATEST(peak_memory, %s),
                    peak_network = GREATEST(peak_network, %s),
                    last_updated = NOW()
                WHERE container_id = %s
            """
            peak_values = (
                stats['cpu_usage'],
                stats['memory_usage'],
                max(stats['network']['rx_bytes'], stats['network']['tx_bytes']),
                container_id
            )
            cursor.execute(peak_query, peak_values)
            
            self.db_connection.commit()
            cursor.close()
        except Exception as e:
            logging.error(f"Error updating database stats: {str(e)}")
            if not self.db_connection.is_connected():
                self.db_connection = self.connect_to_database()

    async def check_alerts(self, container_id: str, stats: Dict):
        alerts = []
        
        if stats['cpu_usage'] > self.alert_thresholds['cpu']:
            alerts.append(f"🔴 High CPU Usage: {stats['cpu_usage']}%")
        
        if stats['memory_usage'] > self.alert_thresholds['memory']:
            alerts.append(f"🔴 High Memory Usage: {stats['memory_usage']}%")
        
        if stats['disk_usage'] > self.alert_thresholds['disk']:
            alerts.append(f"🔴 High Disk Usage: {stats['disk_usage']}%")

        if alerts:
            await self.send_alert(container_id, alerts)

    async def send_alert(self, container_id: str, alerts: List[str]):
        try:
            # Get the Discord user ID associated with this container
            cursor = self.db_connection.cursor()
            query = "SELECT user_id FROM vps_containers WHERE container_id = %s"
            cursor.execute(query, (container_id,))
            result = cursor.fetchone()
            cursor.close()

            if result:
                user_id = result[0]
                user = await self.bot.fetch_user(user_id)
                if user:
                    embed = discord.Embed(
                        title="🚨 VPS Resource Alert",
                        description=f"Container ID: {container_id[:12]}",
                        color=discord.Color.red()
                    )
                    embed.add_field(
                        name="Resource Warnings",
                        value="\n".join(alerts),
                        inline=False
                    )
                    await user.send(embed=embed)
        except Exception as e:
            logging.error(f"Error sending alert: {str(e)}")

    @commands.command()
    async def vps_stats(self, ctx, container_id: Optional[str] = None):
        """Get current VPS statistics"""
        if not container_id:
            # Get the user's container ID
            cursor = self.db_connection.cursor()
            query = "SELECT container_id FROM vps_containers WHERE user_id = %s"
            cursor.execute(query, (ctx.author.id,))
            result = cursor.fetchone()
            cursor.close()
            
            if not result:
                return await ctx.send("You don't have a VPS instance.")
            container_id = result[0]

        stats = self.stats_cache.get(container_id)
        if not stats:
            return await ctx.send("No statistics available for this VPS instance.")

        embed = discord.Embed(
            title="VPS Statistics",
            description=f"Container ID: {container_id[:12]}",
            color=discord.Color.blue(),
            timestamp=datetime.now()
        )

        embed.add_field(
            name="Status",
            value=stats['status'].capitalize(),
            inline=True
        )
        embed.add_field(
            name="CPU Usage",
            value=f"{stats['cpu_usage']}%",
            inline=True
        )
        embed.add_field(
            name="Memory Usage",
            value=f"{stats['memory_usage']}%\n({self.format_bytes(stats['memory_used'])} / {self.format_bytes(stats['memory_total'])})",
            inline=True
        )
        embed.add_field(
            name="Network Usage",
            value=f"↓ {self.format_bytes(stats['network']['rx_bytes'])}\n↑ {self.format_bytes(stats['network']['tx_bytes'])}",
            inline=True
        )
        embed.add_field(
            name="Disk Usage",
            value=f"{stats['disk_usage']}%",
            inline=True
        )

        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def set_alert_threshold(self, ctx, resource: str, threshold: float):
        """Set resource alert thresholds (Admin only)"""
        if resource not in self.alert_thresholds:
            return await ctx.send(f"Invalid resource. Valid options: {', '.join(self.alert_thresholds.keys())}")
        
        if not 0 <= threshold <= 100:
            return await ctx.send("Threshold must be between 0 and 100")
        
        self.alert_thresholds[resource] = threshold
        await ctx.send(f"Alert threshold for {resource} set to {threshold}%")

    def format_bytes(self, bytes_value: int) -> str:
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if bytes_value < 1024:
                return f"{bytes_value:.1f} {unit}"
            bytes_value /= 1024
        return f"{bytes_value:.1f} PB"

    def create_usage_graph(self, data: list, metric: str) -> discord.File:
        plt.figure(figsize=(10, 6))
        timestamps = [datetime.fromisoformat(record['timestamp']) for record in data]
        values = [record[metric] for record in data]
        
        plt.plot(timestamps, values)
        plt.title(f'{metric.replace("_", " ").title()} Over Time')
        plt.xlabel('Time')
        plt.ylabel(metric.replace("_", " ").title())
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()

        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        plt.close()

        return discord.File(buffer, filename=f'{metric}_graph.png')

    @commands.group(name='vps')
    async def vps(self, ctx):
        """VPS management commands"""
        if ctx.invoked_subcommand is None:
            await ctx.send('Invalid VPS command. Use `!help vps` for more information.')

    @vps.command(name='stats')
    async def stats(self, ctx, container_id: str):
        """Show current VPS statistics"""
        try:
            cursor = self.db_connection.cursor(dictionary=True)
            query = """
                SELECT *
                FROM vps_statistics
                WHERE container_id = %s
                ORDER BY timestamp DESC
                LIMIT 1
            """
            cursor.execute(query, (container_id,))
            stats = cursor.fetchone()
            cursor.close()

            if not stats:
                await ctx.send("No statistics found for this VPS.")

            embed = discord.Embed(
                title=f"VPS Statistics for {container_id[:12]}",
                color=discord.Color.blue(),
                timestamp=datetime.now()
            )

            embed.add_field(
                name="CPU Usage",
                value=f"{stats['cpu_usage']}%",
                inline=True
            )
            embed.add_field(
                name="Memory Usage",
                value=f"{stats['memory_usage']}%\n({stats['memory_used'] / 1024 / 1024:.1f}MB / {stats['memory_total'] / 1024 / 1024:.1f}MB)",
                inline=True
            )
            embed.add_field(
                name="Disk Usage",
                value=f"{stats['disk_usage']}%",
                inline=True
            )
            embed.add_field(
                name="Network Statistics",
                value=f"↓ {stats['network_rx'] / 1024 / 1024:.1f}MB\n↑ {stats['network_tx'] / 1024 / 1024:.1f}MB",
                inline=True
            )
            embed.add_field(
                name="Status",
                value=stats['status'],
                inline=True
            )

            await ctx.send(embed=embed)

        except Exception as e:
            await ctx.send(f"Error fetching statistics: {str(e)}")

    @vps.command(name='history')
    async def history(self, ctx, container_id: str, hours: int = 24):
        """Show VPS statistics history"""
        try:
            cursor = self.db_connection.cursor(dictionary=True)
            query = """
                SELECT *
                FROM vps_statistics
                WHERE container_id = %s
                AND timestamp > DATE_SUB(NOW(), INTERVAL %s HOUR)
                ORDER BY timestamp ASC
            """
            cursor.execute(query, (container_id, hours))
            history = cursor.fetchall()
            cursor.close()

            if not history:
                await ctx.send("No historical data found for this VPS.")

            # Create graphs for different metrics
            cpu_graph = self.create_usage_graph(history, 'cpu_usage')
            memory_graph = self.create_usage_graph(history, 'memory_usage')
            disk_graph = self.create_usage_graph(history, 'disk_usage')

            embed = discord.Embed(
                title=f"VPS History for {container_id[:12]} (Last {hours} hours)",
                color=discord.Color.blue(),
                timestamp=datetime.now()
            )

            # Calculate averages
            avg_cpu = sum(record['cpu_usage'] for record in history) / len(history)
            avg_memory = sum(record['memory_usage'] for record in history) / len(history)
            avg_disk = sum(record['disk_usage'] for record in history) / len(history)

            embed.add_field(
                name="Average CPU Usage",
                value=f"{avg_cpu:.1f}%",
                inline=True
            )
            embed.add_field(
                name="Average Memory Usage",
                value=f"{avg_memory:.1f}%",
                inline=True
            )
            embed.add_field(
                name="Average Disk Usage",
                value=f"{avg_disk:.1f}%",
                inline=True
            )

            await ctx.send(embed=embed)
            await ctx.send(files=[cpu_graph, memory_graph, disk_graph])

        except Exception as e:
            await ctx.send(f"Error fetching history: {str(e)}")

    @vps.command(name='alerts')
    async def alerts(self, ctx, container_id: str):
        """Show any active alerts for the VPS"""
        try:
            cursor = self.db_connection.cursor(dictionary=True)
            query = """
                SELECT *
                FROM vps_statistics
                WHERE container_id = %s
                ORDER BY timestamp DESC
                LIMIT 1
            """
            cursor.execute(query, (container_id,))
            stats = cursor.fetchone()
            cursor.close()

            if not stats:
                await ctx.send("No statistics found for this VPS.")

            alerts = []
            if stats['cpu_usage'] > 90:
                alerts.append("⚠️ High CPU usage detected!")
            if stats['memory_usage'] > 90:
                alerts.append("⚠️ High memory usage detected!")
            if stats['disk_usage'] > 90:
                alerts.append("⚠️ High disk usage detected!")
            if stats['status'] != 'running':
                alerts.append(f"⚠️ Container is not running (Status: {stats['status']})")

            if alerts:
                embed = discord.Embed(
                    title=f"VPS Alerts for {container_id[:12]}",
                    color=discord.Color.red(),
                    timestamp=datetime.now()
                )
                for alert in alerts:
                    embed.add_field(name="Alert", value=alert, inline=False)
            else:
                embed = discord.Embed(
                    title=f"VPS Alerts for {container_id[:12]}",
                    description="No active alerts",
                    color=discord.Color.green(),
                    timestamp=datetime.now()
                )

            await ctx.send(embed=embed)

        except Exception as e:
            await ctx.send(f"Error checking alerts: {str(e)}")

    @tasks.loop(minutes=5)
    async def update_status(self):
        """Update bot status with overall system health"""
        try:
            cursor = self.db_connection.cursor(dictionary=True)
            query = """
                SELECT AVG(cpu_usage) as avg_cpu,
                       AVG(memory_usage) as avg_memory,
                       COUNT(*) as total_vps
                FROM vps_statistics
                WHERE timestamp > DATE_SUB(NOW(), INTERVAL 5 MINUTE)
            """
            cursor.execute(query)
            stats = cursor.fetchone()
            cursor.close()

            if stats and stats['avg_cpu'] is not None:
                status = f"🖥️ {stats['total_vps']} VPS | CPU: {stats['avg_cpu']:.1f}% | RAM: {stats['avg_memory']:.1f}%"
                await self.bot.change_presence(activity=discord.Game(name=status))

        except Exception as e:
            print(f"Error updating status: {str(e)}")

    @update_status.before_loop
    async def before_update_status(self):
        await self.bot.wait_until_ready()

def setup(bot):
    bot.add_cog(Monitoring(bot))