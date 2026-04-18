import discord
from discord.ext import commands
from discord import app_commands
import mysql.connector
from typing import Dict, Optional
import json
import os
from datetime import datetime, timedelta

class VPSPricing(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = self.initialize_database()
        self.prices = {
            'cpu_per_core': 50.0,  # $50 per CPU core
            'memory_per_gb': 25.0,  # $25 per GB of RAM
            'storage_per_gb': 1.0,  # $1 per GB of storage
            'bandwidth_per_gb': 0.5  # $0.5 per GB of bandwidth
        }
        self.billing_interval = timedelta(days=30)  # Bill every 30 days

    def initialize_database(self):
        return mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )

    def calculate_vps_cost(self, cpu: float, memory: int, storage: int) -> float:
        """Calculate the monthly cost for a VPS configuration"""
        cpu_cost = cpu * self.prices['cpu_per_core']
        memory_cost = (memory / 1024) * self.prices['memory_per_gb']  # Convert MB to GB
        storage_cost = storage * self.prices['storage_per_gb']
        
        return cpu_cost + memory_cost + storage_cost

    async def check_balance(self, user_id: str) -> float:
        """Check user's balance from the shared economy system"""
        cursor = self.db.cursor()
        cursor.execute("SELECT balance FROM player_economy WHERE uuid = %s", (user_id,))
        result = cursor.fetchone()
        cursor.close()
        return result[0] if result else 0.0

    async def process_payment(self, user_id: str, amount: float, description: str) -> bool:
        """Process a payment from user's balance"""
        try:
            cursor = self.db.cursor()
            
            # Check balance
            cursor.execute("SELECT balance FROM player_economy WHERE uuid = %s", (user_id,))
            result = cursor.fetchone()
            if not result or result[0] < amount:
                return False

            # Update balance
            cursor.execute(
                "UPDATE player_economy SET balance = balance - %s WHERE uuid = %s",
                (amount, user_id)
            )

            # Record transaction
            cursor.execute(
                """INSERT INTO economy_transactions 
                   (uuid, amount, type, description) 
                   VALUES (%s, %s, %s, %s)""",
                (user_id, -amount, "VPS_PAYMENT", description)
            )

            self.db.commit()
            cursor.close()
            return True
        except Exception as e:
            self.bot.logger.error(f"Payment processing error: {e}")
            self.db.rollback()
            return False

    @app_commands.command(name="vpscost")
    @app_commands.describe(
        cpu="Number of CPU cores (0.5-4)",
        memory="Memory in MB (512-8192)",
        storage="Storage in GB (10-100)"
    )
    async def calculate_cost(
        self,
        interaction: discord.Interaction,
        cpu: float,
        memory: int,
        storage: int
    ):
        """Calculate the cost of a VPS configuration"""
        await interaction.response.defer()

        # Validate resource limits
        if not (0.5 <= cpu <= 4):
            await interaction.followup.send("CPU cores must be between 0.5 and 4")
            return
        if not (512 <= memory <= 8192):
            await interaction.followup.send("Memory must be between 512MB and 8GB")
            return
        if not (10 <= storage <= 100):
            await interaction.followup.send("Storage must be between 10GB and 100GB")
            return

        monthly_cost = self.calculate_vps_cost(cpu, memory, storage)
        user_balance = await self.check_balance(str(interaction.user.id))

        embed = discord.Embed(
            title="VPS Cost Calculation",
            color=discord.Color.blue(),
            timestamp=datetime.utcnow()
        )

        embed.add_field(
            name="Configuration",
            value=f"CPU: {cpu} cores\nMemory: {memory}MB\nStorage: {storage}GB",
            inline=False
        )

        embed.add_field(
            name="Cost Breakdown",
            value=f"CPU: ${cpu * self.prices['cpu_per_core']:.2f}\n"
                  f"Memory: ${(memory / 1024) * self.prices['memory_per_gb']:.2f}\n"
                  f"Storage: ${storage * self.prices['storage_per_gb']:.2f}",
            inline=False
        )

        embed.add_field(
            name="Total Monthly Cost",
            value=f"${monthly_cost:.2f}",
            inline=False
        )

        embed.add_field(
            name="Your Balance",
            value=f"${user_balance:.2f}",
            inline=False
        )

        can_afford = user_balance >= monthly_cost
        embed.add_field(
            name="Status",
            value="✅ You can afford this VPS!" if can_afford else "❌ Insufficient funds",
            inline=False
        )

        await interaction.followup.send(embed=embed)

    @app_commands.command(name="purchasevps")
    @app_commands.describe(
        cpu="Number of CPU cores (0.5-4)",
        memory="Memory in MB (512-8192)",
        storage="Storage in GB (10-100)"
    )
    async def purchase_vps(
        self,
        interaction: discord.Interaction,
        cpu: float,
        memory: int,
        storage: int
    ):
        """Purchase a new VPS instance using your balance"""
        await interaction.response.defer()

        # Validate resource limits
        if not (0.5 <= cpu <= 4):
            await interaction.followup.send("CPU cores must be between 0.5 and 4")
            return
        if not (512 <= memory <= 8192):
            await interaction.followup.send("Memory must be between 512MB and 8GB")
            return
        if not (10 <= storage <= 100):
            await interaction.followup.send("Storage must be between 10GB and 100GB")
            return

        monthly_cost = self.calculate_vps_cost(cpu, memory, storage)
        user_balance = await self.check_balance(str(interaction.user.id))

        if user_balance < monthly_cost:
            await interaction.followup.send(
                f"Insufficient funds! You need ${monthly_cost:.2f} but have ${user_balance:.2f}"
            )
            return

        # Process payment
        payment_success = await self.process_payment(
            str(interaction.user.id),
            monthly_cost,
            f"VPS Purchase - {cpu} CPU, {memory}MB RAM, {storage}GB Storage"
        )

        if not payment_success:
            await interaction.followup.send("Failed to process payment. Please try again later.")
            return

        # Create VPS instance
        vps_config = {
            'cpu_limit': cpu,
            'memory_limit': memory,
            'storage_limit': storage,
            'image': 'ubuntu:latest',
            'ports': {},
            'env_vars': {}
        }

        try:
            vps_manager = self.bot.get_cog('VPSCommands').vps_manager
            container_id = await vps_manager.create_vps(str(interaction.user.id), vps_config)

            if container_id:
                embed = discord.Embed(
                    title="VPS Purchase Successful",
                    description="Your VPS has been created!",
                    color=discord.Color.green(),
                    timestamp=datetime.utcnow()
                )

                embed.add_field(name="Container ID", value=container_id[:12])
                embed.add_field(name="Monthly Cost", value=f"${monthly_cost:.2f}")
                embed.add_field(name="Next Billing Date", value=(datetime.utcnow() + self.billing_interval).strftime("%Y-%m-%d"))
                
                await interaction.followup.send(embed=embed)
            else:
                # Refund the payment if VPS creation fails
                await self.process_payment(
                    str(interaction.user.id),
                    -monthly_cost,
                    "VPS Creation Failed - Refund"
                )
                await interaction.followup.send("Failed to create VPS. Your payment has been refunded.")
        except Exception as e:
            self.bot.logger.error(f"VPS creation error: {e}")
            # Refund the payment
            await self.process_payment(
                str(interaction.user.id),
                -monthly_cost,
                "VPS Creation Error - Refund"
            )
            await interaction.followup.send("An error occurred. Your payment has been refunded.")

async def setup(bot):
    await bot.add_cog(VPSPricing(bot))