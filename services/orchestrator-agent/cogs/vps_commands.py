import discord
from discord.ext import commands
from discord import app_commands
from vps_manager import VPSManager, VPSConfig
import asyncio
from typing import Optional
import humanize

class VPSCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.vps_manager = VPSManager()
        self.loading_emoji = "⌛"
        self.success_emoji = "✅"
        self.error_emoji = "❌"

    @app_commands.command(name="createvps")
    @app_commands.describe(
        cpu="Number of CPU cores (0.5-4)",
        memory="Memory in MB (512-8192)",
        storage="Storage in GB (10-100)",
        image="Docker image to use (e.g. ubuntu:latest)"
    )
    async def create_vps(
        self, 
        interaction: discord.Interaction, 
        cpu: float, 
        memory: int, 
        storage: int, 
        image: str = "ubuntu:latest"
    ):
        """Create a new VPS instance"""
        await interaction.response.defer()

        # Validate resource limits
        if not (0.5 <= cpu <= 4):
            await interaction.followup.send(f"{self.error_emoji} CPU cores must be between 0.5 and 4")
            return
        if not (512 <= memory <= 8192):
            await interaction.followup.send(f"{self.error_emoji} Memory must be between 512MB and 8GB")
            return
        if not (10 <= storage <= 100):
            await interaction.followup.send(f"{self.error_emoji} Storage must be between 10GB and 100GB")
            return

        config = VPSConfig(
            cpu_limit=cpu,
            memory_limit=memory,
            storage_limit=storage,
            image=image,
            ports={},  # Will be configured separately
            env_vars={}
        )

        container_id = await self.vps_manager.create_vps(str(interaction.user.id), config)
        
        if container_id:
            embed = discord.Embed(
                title="VPS Created Successfully",
                description=f"Your VPS instance has been created!",
                color=discord.Color.green()
            )
            embed.add_field(name="Container ID", value=container_id[:12])
            embed.add_field(name="CPU Cores", value=str(cpu))
            embed.add_field(name="Memory", value=f"{memory}MB")
            embed.add_field(name="Storage", value=f"{storage}GB")
            embed.add_field(name="Image", value=image)
            
            await interaction.followup.send(embed=embed)
        else:
            await interaction.followup.send(f"{self.error_emoji} Failed to create VPS instance")

    @app_commands.command(name="listvps")
    async def list_vps(self, interaction: discord.Interaction):
        """List all your VPS instances"""
        await interaction.response.defer()

        instances = await self.vps_manager.list_user_instances(str(interaction.user.id))
        
        if not instances:
            await interaction.followup.send("You don't have any VPS instances")
            return

        embed = discord.Embed(
            title="Your VPS Instances",
            color=discord.Color.blue()
        )

        for instance in instances:
            stats = instance["stats"]
            info = instance["info"]
            
            status_emoji = "🟢" if stats and stats["status"] == "running" else "🔴"
            
            field_value = (
                f"Status: {status_emoji} {stats['status'] if stats else 'Unknown'}\n"
                f"CPU: {stats['cpu_usage']}% | RAM: {stats['memory_usage']}%\n"
                f"Created: {info['created_at']}\n"
                f"ID: `{instance['container_id'][:12]}`"
            )
            
            embed.add_field(
                name=f"Instance {info['config']['image']}",
                value=field_value,
                inline=False
            )

        await interaction.followup.send(embed=embed)

    @app_commands.command(name="startvps")
    @app_commands.describe(container_id="The ID of the VPS to start")
    async def start_vps(self, interaction: discord.Interaction, container_id: str):
        """Start a VPS instance"""
        await interaction.response.defer()

        if await self.vps_manager.start_vps(container_id):
            await interaction.followup.send(f"{self.success_emoji} VPS started successfully")
        else:
            await interaction.followup.send(f"{self.error_emoji} Failed to start VPS")

    @app_commands.command(name="stopvps")
    @app_commands.describe(container_id="The ID of the VPS to stop")
    async def stop_vps(self, interaction: discord.Interaction, container_id: str):
        """Stop a VPS instance"""
        await interaction.response.defer()

        if await self.vps_manager.stop_vps(container_id):
            await interaction.followup.send(f"{self.success_emoji} VPS stopped successfully")
        else:
            await interaction.followup.send(f"{self.error_emoji} Failed to stop VPS")

    @app_commands.command(name="restartvps")
    @app_commands.describe(container_id="The ID of the VPS to restart")
    async def restart_vps(self, interaction: discord.Interaction, container_id: str):
        """Restart a VPS instance"""
        await interaction.response.defer()

        if await self.vps_manager.restart_vps(container_id):
            await interaction.followup.send(f"{self.success_emoji} VPS restarted successfully")
        else:
            await interaction.followup.send(f"{self.error_emoji} Failed to restart VPS")

    @app_commands.command(name="deletevps")
    @app_commands.describe(container_id="The ID of the VPS to delete")
    async def delete_vps(self, interaction: discord.Interaction, container_id: str):
        """Delete a VPS instance"""
        await interaction.response.defer()

        # Add confirmation button
        confirm = discord.ui.Button(label="Confirm", style=discord.ButtonStyle.danger)
        cancel = discord.ui.Button(label="Cancel", style=discord.ButtonStyle.secondary)
        
        async def confirm_callback(interaction: discord.Interaction):
            if await self.vps_manager.delete_vps(container_id):
                await interaction.response.edit_message(
                    content=f"{self.success_emoji} VPS deleted successfully",
                    view=None
                )
            else:
                await interaction.response.edit_message(
                    content=f"{self.error_emoji} Failed to delete VPS",
                    view=None
                )

        async def cancel_callback(interaction: discord.Interaction):
            await interaction.response.edit_message(
                content="Operation cancelled",
                view=None
            )

        confirm.callback = confirm_callback
        cancel.callback = cancel_callback

        view = discord.ui.View()
        view.add_item(confirm)
        view.add_item(cancel)

        await interaction.followup.send(
            f"Are you sure you want to delete VPS {container_id[:12]}? This action cannot be undone.",
            view=view
        )

    @app_commands.command(name="vpsstats")
    @app_commands.describe(container_id="The ID of the VPS to get stats for")
    async def vps_stats(self, interaction: discord.Interaction, container_id: str):
        """Get detailed statistics for a VPS instance"""
        await interaction.response.defer()

        stats = await self.vps_manager.get_vps_stats(container_id)
        if not stats:
            await interaction.followup.send(f"{self.error_emoji} Failed to get VPS statistics")
            return

        embed = discord.Embed(
            title=f"VPS Statistics",
            color=discord.Color.blue()
        )

        embed.add_field(name="Status", value=stats["status"], inline=True)
        embed.add_field(name="CPU Usage", value=f"{stats['cpu_usage']}%", inline=True)
        embed.add_field(name="Memory Usage", value=f"{stats['memory_usage']}%", inline=True)
        
        network = stats["network"]
        embed.add_field(
            name="Network",
            value=f"↓ {humanize.naturalsize(network['rx_bytes'])}\n"
                  f"↑ {humanize.naturalsize(network['tx_bytes'])}",
            inline=True
        )

        await interaction.followup.send(embed=embed)

    @app_commands.command(name="backup")
    @app_commands.describe(container_id="The ID of the VPS to backup")
    async def backup_vps(self, interaction: discord.Interaction, container_id: str):
        """Create a backup of a VPS instance"""
        await interaction.response.defer()

        backup_id = await self.vps_manager.create_backup(container_id)
        if backup_id:
            embed = discord.Embed(
                title="Backup Created",
                description=f"Backup ID: `{backup_id[:12]}`",
                color=discord.Color.green()
            )
            await interaction.followup.send(embed=embed)
        else:
            await interaction.followup.send(f"{self.error_emoji} Failed to create backup")

    @app_commands.command(name="restore")
    @app_commands.describe(
        container_id="The ID of the VPS to restore",
        backup_id="The ID of the backup to restore from"
    )
    async def restore_vps(self, interaction: discord.Interaction, container_id: str, backup_id: str):
        """Restore a VPS from backup"""
        await interaction.response.defer()

        if await self.vps_manager.restore_backup(container_id, backup_id):
            await interaction.followup.send(f"{self.success_emoji} VPS restored successfully")
        else:
            await interaction.followup.send(f"{self.error_emoji} Failed to restore VPS")

async def setup(bot):
    await bot.add_cog(VPSCommands(bot))