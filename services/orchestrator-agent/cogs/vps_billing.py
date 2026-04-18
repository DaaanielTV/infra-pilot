import discord
from discord.ext import commands, tasks
import mysql.connector
from datetime import datetime, timedelta
import os
import logging
from typing import Dict, List

class VPSBilling(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = self.initialize_database()
        self.logger = logging.getLogger('vps_billing')
        self.check_billing_loop.start()
        self.grace_period = timedelta(days=3)  # Grace period for late payments

    def initialize_database(self):
        return mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )

    def cog_unload(self):
        self.check_billing_loop.cancel()

    @tasks.loop(hours=1)  # Check every hour
    async def check_billing_loop(self):
        """Check for VPS instances that need billing"""
        try:
            # Get all active VPS instances
            vps_manager = self.bot.get_cog('VPSCommands').vps_manager
            vps_pricing = self.bot.get_cog('VPSPricing')

            for container_id, instance in vps_manager.vps_instances.items():
                await self.process_instance_billing(container_id, instance, vps_manager, vps_pricing)
        except Exception as e:
            self.logger.error(f"Error in billing loop: {e}")

    async def process_instance_billing(self, container_id: str, instance: Dict, vps_manager, vps_pricing):
        """Process billing for a single VPS instance"""
        try:
            last_billing = datetime.fromisoformat(instance.get('last_billing', instance['created_at']))
            next_billing = last_billing + timedelta(days=30)
            now = datetime.now()

            if now >= next_billing:
                await self.bill_instance(container_id, instance, vps_manager, vps_pricing)

        except Exception as e:
            self.logger.error(f"Error processing billing for container {container_id}: {e}")

    async def bill_instance(self, container_id: str, instance: Dict, vps_manager, vps_pricing):
        """Bill a VPS instance"""
        user_id = instance['user_id']
        config = instance['config']

        # Calculate cost
        monthly_cost = vps_pricing.calculate_vps_cost(
            config['cpu_limit'],
            config['memory_limit'],
            config['storage_limit']
        )

        # Check user's balance
        balance = await vps_pricing.check_balance(user_id)
        
        if balance >= monthly_cost:
            # Process payment
            payment_success = await vps_pricing.process_payment(
                user_id,
                monthly_cost,
                f"VPS Monthly Billing - {container_id[:12]}"
            )

            if payment_success:
                # Update last billing date
                instance['last_billing'] = datetime.now().isoformat()
                vps_manager.save_instances()

                # Notify user
                await self.notify_user(user_id, "VPS Billing Success", {
                    "container_id": container_id[:12],
                    "amount": monthly_cost,
                    "next_billing": (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")
                })
            else:
                await self.handle_failed_payment(container_id, instance, monthly_cost)
        else:
            await self.handle_insufficient_funds(container_id, instance, monthly_cost, balance)

    async def handle_failed_payment(self, container_id: str, instance: Dict, amount: float):
        """Handle a failed payment"""
        user_id = instance['user_id']
        
        # Mark instance as payment overdue
        instance['payment_overdue'] = True
        instance['grace_period_end'] = (datetime.now() + self.grace_period).isoformat()

        # Notify user
        await self.notify_user(user_id, "VPS Payment Failed", {
            "container_id": container_id[:12],
            "amount": amount,
            "grace_period_end": instance['grace_period_end']
        })

        # Check if grace period has expired
        if 'grace_period_end' in instance:
            grace_end = datetime.fromisoformat(instance['grace_period_end'])
            if datetime.now() > grace_end:
                await self.suspend_instance(container_id, instance)

    async def handle_insufficient_funds(self, container_id: str, instance: Dict, amount: float, current_balance: float):
        """Handle insufficient funds"""
        user_id = instance['user_id']
        
        # Mark instance as payment overdue
        instance['payment_overdue'] = True
        instance['grace_period_end'] = (datetime.now() + self.grace_period).isoformat()

        # Notify user
        await self.notify_user(user_id, "VPS Insufficient Funds", {
            "container_id": container_id[:12],
            "amount": amount,
            "current_balance": current_balance,
            "needed": amount - current_balance,
            "grace_period_end": instance['grace_period_end']
        })

    async def suspend_instance(self, container_id: str, instance: Dict):
        """Suspend a VPS instance due to payment issues"""
        vps_manager = self.bot.get_cog('VPSCommands').vps_manager
        
        # Stop the VPS
        await vps_manager.stop_vps(container_id)
        
        # Mark as suspended
        instance['status'] = 'suspended'
        instance['suspended_at'] = datetime.now().isoformat()
        vps_manager.save_instances()

        # Notify user
        await self.notify_user(instance['user_id'], "VPS Suspended", {
            "container_id": container_id[:12],
            "suspended_at": instance['suspended_at']
        })

    async def notify_user(self, user_id: str, notification_type: str, data: Dict):
        """Send a notification to a user"""
        try:
            user = await self.bot.fetch_user(int(user_id))
            if not user:
                return

            embed = discord.Embed(
                title=notification_type,
                color=self.get_notification_color(notification_type),
                timestamp=datetime.utcnow()
            )

            if notification_type == "VPS Billing Success":
                embed.description = "Your VPS monthly payment has been processed successfully."
                embed.add_field(name="Container ID", value=data['container_id'])
                embed.add_field(name="Amount Paid", value=f"${data['amount']:.2f}")
                embed.add_field(name="Next Billing Date", value=data['next_billing'])

            elif notification_type == "VPS Payment Failed":
                embed.description = "⚠️ Your VPS payment has failed. Please add funds to your account."
                embed.add_field(name="Container ID", value=data['container_id'])
                embed.add_field(name="Amount Due", value=f"${data['amount']:.2f}")
                embed.add_field(name="Grace Period Ends", value=data['grace_period_end'])
                embed.add_field(
                    name="Warning",
                    value="Your VPS will be suspended if payment is not received before the grace period ends.",
                    inline=False
                )

            elif notification_type == "VPS Insufficient Funds":
                embed.description = "⚠️ You have insufficient funds for your VPS payment."
                embed.add_field(name="Container ID", value=data['container_id'])
                embed.add_field(name="Amount Needed", value=f"${data['amount']:.2f}")
                embed.add_field(name="Current Balance", value=f"${data['current_balance']:.2f}")
                embed.add_field(name="Additional Funds Needed", value=f"${data['needed']:.2f}")
                embed.add_field(name="Grace Period Ends", value=data['grace_period_end'])
                embed.add_field(
                    name="Warning",
                    value="Your VPS will be suspended if funds are not added before the grace period ends.",
                    inline=False
                )

            elif notification_type == "VPS Suspended":
                embed.description = "❌ Your VPS has been suspended due to payment issues."
                embed.add_field(name="Container ID", value=data['container_id'])
                embed.add_field(name="Suspended At", value=data['suspended_at'])
                embed.add_field(
                    name="How to Reactivate",
                    value="Add sufficient funds to your account and contact support to reactivate your VPS.",
                    inline=False
                )

            await user.send(embed=embed)
        except Exception as e:
            self.logger.error(f"Error sending notification to user {user_id}: {e}")

    def get_notification_color(self, notification_type: str) -> discord.Color:
        """Get the appropriate color for a notification type"""
        colors = {
            "VPS Billing Success": discord.Color.green(),
            "VPS Payment Failed": discord.Color.orange(),
            "VPS Insufficient Funds": discord.Color.orange(),
            "VPS Suspended": discord.Color.red()
        }
        return colors.get(notification_type, discord.Color.default())

    @check_billing_loop.before_loop
    async def before_billing_check(self):
        """Wait for the bot to be ready before starting the billing loop"""
        await self.bot.wait_until_ready()

async def setup(bot):
    await bot.add_cog(VPSBilling(bot))