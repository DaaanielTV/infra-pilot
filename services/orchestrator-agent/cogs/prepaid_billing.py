"""Prepaid billing cog — pay-as-you-go balance, hourly deduction, top-ups.

Manages user prepaid balances with hourly deduction for running VPS
instances. Provides balance check, top-up, and cost estimation commands.
"""

import asyncio
import json
import logging
import os
import secrets
from datetime import datetime, timedelta
from typing import Optional

import discord
from discord.ext import commands, tasks

logger = logging.getLogger(__name__)


class PrepaidBilling(commands.Cog):
    """Prepaid balance / pay-as-you-go billing system."""

    def __init__(self, bot):
        self.bot = bot
        self.data_file = "data/billing.json"
        self._ensure_data_dir()
        self._load_data()
        self.billing_loop.start()

    def _ensure_data_dir(self):
        os.makedirs("data", exist_ok=True)

    def _load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file) as f:
                self.data = json.load(f)
        else:
            self.data = {
                "users": {},
                "rates": {
                    "cpu_per_core_hour": 0.05,
                    "ram_per_gb_hour": 0.02,
                    "storage_per_gb_hour": 0.001,
                    "backup_per_gb": 0.01,
                },
                "min_topup": 5.00,
                "min_balance": 0.00,
            }
            self._save_data()

    def _save_data(self):
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
        with open(self.data_file, "w") as f:
            json.dump(self.data, f, indent=2)

    def _get_user(self, user_id: str) -> dict:
        if user_id not in self.data["users"]:
            self.data["users"][user_id] = {
                "balance": 0.0,
                "total_spent": 0.0,
                "total_topped_up": 0.0,
                "transactions": [],
                "created_at": datetime.utcnow().isoformat(),
            }
            self._save_data()
        return self.data["users"][user_id]

    def _add_transaction(
        self, user_id: str, amount: float, description: str, transaction_type: str
    ):
        user = self._get_user(user_id)
        user["transactions"].append(
            {
                "id": secrets.token_hex(8),
                "amount": amount,
                "description": description,
                "type": transaction_type,
                "balance_after": user["balance"],
                "timestamp": datetime.utcnow().isoformat(),
            }
        )
        user["transactions"] = user["transactions"][-100:]
        self._save_data()

    def get_balance(self, user_id: str) -> float:
        return self._get_user(user_id)["balance"]

    def add_funds(
        self, user_id: str, amount: float, description: str = "Top-up"
    ) -> dict:
        user = self._get_user(user_id)
        user["balance"] += amount
        user["total_topped_up"] += amount
        self._add_transaction(user_id, amount, description, "topup")
        return {"balance": user["balance"], "amount": amount}

    def deduct_funds(self, user_id: str, amount: float, description: str) -> bool:
        user = self._get_user(user_id)
        if user["balance"] < amount:
            return False
        user["balance"] -= amount
        user["total_spent"] += amount
        self._add_transaction(user_id, -amount, description, "charge")
        return True

    def calculate_hourly_cost(self, resources: dict) -> float:
        rates = self.data["rates"]
        cost = 0.0
        cost += rates["cpu_per_core_hour"] * resources.get("cpu_cores", 1)
        cost += rates["ram_per_gb_hour"] * (resources.get("memory_mb", 1024) / 1024)
        cost += rates["storage_per_gb_hour"] * resources.get("storage_gb", 10)
        return round(cost, 4)

    @tasks.loop(hours=1)
    async def billing_loop(self):
        """Charge users for running VPS instances every hour."""
        logger.info("Running hourly billing cycle...")
        cog = self.bot.get_cog("VPSCommands")
        vps_manager = getattr(cog, "vps_manager", None) if cog else None
        if not vps_manager:
            logger.warning("VPSManager not available, skipping billing")
            return

        billed = 0
        stopped = 0
        errors = 0

        for container_id, instance in list(vps_manager.vps_instances.items()):
            try:
                user_id = instance.get("user_id", "")
                if not user_id:
                    continue

                cfg = instance.get("config", {})
                resources = {
                    "cpu_cores": cfg.get("cpu_limit", 1),
                    "memory_mb": cfg.get("memory_limit", 1024),
                    "storage_gb": cfg.get("storage_limit", 10),
                }
                hourly_cost = self.calculate_hourly_cost(resources)
                if hourly_cost <= 0:
                    continue

                success = self.deduct_funds(
                    user_id,
                    hourly_cost,
                    f"Hourly charge for {container_id[:12]}",
                )
                if success:
                    billed += 1
                else:
                    logger.warning(
                        "Insufficient funds for %s (balance=%.2f), stopping %s",
                        user_id,
                        self.get_balance(user_id),
                        container_id[:12],
                    )
                    try:
                        await vps_manager.stop_vps(container_id)
                        stopped += 1
                    except Exception as exc:
                        logger.error("Failed to stop %s: %s", container_id[:12], exc)
                        errors += 1
            except Exception as exc:
                logger.error("Billing error for %s: %s", container_id[:12], exc)
                errors += 1

        logger.info(
            "Billing cycle done: %d billed, %d stopped, %d errors",
            billed,
            stopped,
            errors,
        )

    @billing_loop.before_loop
    async def before_billing(self):
        await self.bot.wait_until_ready()

    @commands.group(name="balance")
    async def balance_group(self, ctx):
        """Check and manage your prepaid balance."""
        if ctx.invoked_subcommand is None:
            await self.balance_show(ctx)

    async def balance_show(self, ctx):
        user_id = str(ctx.author.id)
        balance = self.get_balance(user_id)
        user = self._get_user(user_id)

        embed = discord.Embed(
            title="\U0001f4b0 Prepaid Balance",
            color=discord.Color.green() if balance > 0 else discord.Color.red(),
        )
        embed.add_field(name="Current Balance", value=f"${balance:.2f}")
        embed.add_field(name="Total Spent", value=f'${user["total_spent"]:.2f}')
        embed.add_field(name="Total Top-Ups", value=f'${user["total_topped_up"]:.2f}')
        embed.set_footer(text=f"User ID: {ctx.author.id}")
        await ctx.send(embed=embed)

    @balance_group.command(name="add")
    @commands.has_permissions(administrator=True)
    async def balance_add(self, ctx, member: discord.Member, amount: float):
        """[Admin] Add funds to a user's balance."""
        result = self.add_funds(
            str(member.id), amount, f"Manual top-up by {ctx.author}"
        )
        await ctx.send(f"\u2705 Added ${amount:.2f} to {member.mention}'s balance.")

    @balance_group.command(name="history")
    async def balance_history(self, ctx, limit: int = 10):
        """Show recent transactions."""
        user = self._get_user(str(ctx.author.id))
        txns = user["transactions"][-limit:]

        if not txns:
            await ctx.send("No transactions yet.")
            return

        embed = discord.Embed(
            title="\U0001f4ca Transaction History", color=discord.Color.blue()
        )
        for txn in reversed(txns):
            icon = "\u2795" if txn["amount"] > 0 else "\u2796"
            embed.add_field(
                name=f"{icon} ${abs(txn['amount']):.2f} \u2014 {txn['description'][:40]}",
                value=f"{txn['timestamp'][:19]} | Balance: ${txn['balance_after']:.2f}",
                inline=False,
            )
        await ctx.send(embed=embed)

    @balance_group.command(name="cost")
    async def balance_cost(
        self, ctx, cpu_cores: float = 1, memory_mb: int = 1024, storage_gb: int = 10
    ):
        """Calculate hourly cost for resources: /balance cost 2 2048 20"""
        cost = self.calculate_hourly_cost(
            {
                "cpu_cores": cpu_cores,
                "memory_mb": memory_mb,
                "storage_gb": storage_gb,
            }
        )
        daily = cost * 24
        monthly = daily * 30
        await ctx.send(
            f"**Cost Estimate:**\n"
            f"\u2022 Hourly: ${cost:.4f}\n"
            f"\u2022 Daily: ${daily:.2f}\n"
            f"\u2022 Monthly (30d): ${monthly:.2f}"
        )


async def setup(bot):
    await bot.add_cog(PrepaidBilling(bot))
