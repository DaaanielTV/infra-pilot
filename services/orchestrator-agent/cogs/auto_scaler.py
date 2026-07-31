"""Discord cog for managing auto-scaling rules.

Provides commands to create, list, view, enable/disable, and delete
scaling rules via the database, plus a summary of recent scaling events.
"""

import logging
from datetime import datetime, timedelta

import discord
from config import config
from db import get_sync_cursor
from discord import app_commands
from discord.ext import commands

logger = logging.getLogger(__name__)


class AutoScaler(commands.Cog):
    """Manage auto-scaling rules for VPS instances."""

    def __init__(self, bot, scaling_engine=None):
        self.bot = bot
        self.engine = scaling_engine

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------
    def _get_server_name(self, container_id: str) -> str:
        """Resolve a container_id to a friendly name."""
        vps_cog = self.bot.get_cog("VPSCommands")
        if vps_cog and hasattr(vps_cog, "vps_manager"):
            info = vps_cog.vps_manager.vps_instances.get(container_id, {})
            name = info.get("container_id", container_id)
            return name[:12]
        return container_id[:12]

    def _validate_metric(self, metric: str) -> bool:
        return metric in ("cpu_usage", "memory_usage")

    def _validate_action(self, action: str) -> bool:
        return action in ("scale_up", "scale_down")

    # ------------------------------------------------------------------
    # Commands
    # ------------------------------------------------------------------
    @app_commands.command(name="scaling-rules")
    @app_commands.describe(container_id="Optional: show rules for a specific container")
    async def list_rules(
        self, interaction: discord.Interaction, container_id: str = ""
    ):
        """List all auto-scaling rules, optionally filtered by container."""
        await interaction.response.defer()
        try:
            cur = get_sync_cursor()
            if container_id:
                cur.execute(
                    "SELECT * FROM scaling_rules WHERE container_id = %s ORDER BY id",
                    (container_id,),
                )
            else:
                cur.execute("SELECT * FROM scaling_rules ORDER BY id")
            rows = cur.fetchall()
            cur.connection.close()
        except Exception as exc:
            await interaction.followup.send(f"Database error: {exc}")
            return

        if not rows:
            await interaction.followup.send("No scaling rules found.")
            return

        embed = discord.Embed(
            title="Auto-Scaling Rules",
            color=discord.Color.blue(),
        )
        for row in rows:
            status = "✅ Enabled" if row["enabled"] else "⛔ Disabled"
            embed.add_field(
                name=f"Rule #{row['id']} — {self._get_server_name(row['container_id'])}",
                value=(
                    f"Metric: `{row['metric']}`\n"
                    f"Threshold: `{row['threshold']}%`\n"
                    f"Duration: `{row['duration_minutes']} min`\n"
                    f"Action: `{row['action']}`\n"
                    f"Status: {status}"
                ),
                inline=True,
            )
        await interaction.followup.send(embed=embed)

    @app_commands.command(name="scaling-rule-create")
    @app_commands.describe(
        container_id="Container ID of the VPS",
        metric="Metric to monitor (cpu_usage or memory_usage)",
        threshold="Threshold percentage to trigger (e.g. 80)",
        duration="Duration in minutes threshold must be breached",
        action="Action: scale_up or scale_down",
    )
    async def create_rule(
        self,
        interaction: discord.Interaction,
        container_id: str,
        metric: str,
        threshold: float,
        duration: int,
        action: str,
    ):
        """Create a new auto-scaling rule."""
        await interaction.response.defer()

        if not self._validate_metric(metric):
            await interaction.followup.send(
                "Invalid metric. Use `cpu_usage` or `memory_usage`."
            )
            return
        if not self._validate_action(action):
            await interaction.followup.send(
                "Invalid action. Use `scale_up` or `scale_down`."
            )
            return
        if threshold < 1 or threshold > 100:
            await interaction.followup.send("Threshold must be between 1 and 100.")
            return
        if duration < 1 or duration > 60:
            await interaction.followup.send(
                "Duration must be between 1 and 60 minutes."
            )
            return

        try:
            cur = get_sync_cursor()
            cur.execute(
                "INSERT INTO scaling_rules "
                "(container_id, metric, threshold, duration_minutes, action) "
                "VALUES (%s, %s, %s, %s, %s) RETURNING id",
                (container_id, metric, threshold, duration, action),
            )
            row = cur.fetchone()
            cur.connection.commit()
            cur.connection.close()
            rule_id = row["id"]

            # Also add to in-memory engine if available
            if self.engine:
                from scaling import ScalingEngine, ScalingRule

                self.engine.add_rule(
                    ScalingRule(
                        id=rule_id,
                        container_id=container_id,
                        metric=metric,
                        threshold=threshold,
                        duration_minutes=duration,
                        action=action,
                    )
                )

            await interaction.followup.send(
                f"✅ Created scaling rule **#{rule_id}**\n"
                f"Container: `{container_id[:12]}`\n"
                f"Metric: `{metric}` >= `{threshold}%` for `{duration} min` → `{action}`"
            )
        except Exception as exc:
            await interaction.followup.send(f"Failed to create rule: {exc}")

    @app_commands.command(name="scaling-rule-delete")
    @app_commands.describe(rule_id="ID of the scaling rule to delete")
    async def delete_rule(self, interaction: discord.Interaction, rule_id: int):
        """Delete a scaling rule."""
        await interaction.response.defer()
        try:
            cur = get_sync_cursor()
            cur.execute("DELETE FROM scaling_rules WHERE id = %s", (rule_id,))
            deleted = cur.rowcount
            cur.connection.commit()
            cur.connection.close()

            if deleted:
                self.engine and self.engine.remove_rule(rule_id)
                await interaction.followup.send(
                    f"🗑️ Deleted scaling rule **#{rule_id}**"
                )
            else:
                await interaction.followup.send(f"Rule **#{rule_id}** not found.")
        except Exception as exc:
            await interaction.followup.send(f"Failed to delete rule: {exc}")

    @app_commands.command(name="scaling-rule-toggle")
    @app_commands.describe(rule_id="ID of the scaling rule to enable/disable")
    async def toggle_rule(self, interaction: discord.Interaction, rule_id: int):
        """Enable or disable a scaling rule."""
        await interaction.response.defer()
        try:
            cur = get_sync_cursor()
            cur.execute(
                "UPDATE scaling_rules SET enabled = NOT enabled WHERE id = %s "
                "RETURNING id, enabled",
                (rule_id,),
            )
            row = cur.fetchone()
            cur.connection.commit()
            cur.connection.close()

            if row:
                status = "enabled" if row["enabled"] else "disabled"
                # Sync in-memory rule
                if self.engine:
                    rule = self.engine.get_rule(rule_id)
                    if rule:
                        rule.enabled = row["enabled"]
                await interaction.followup.send(
                    f"🔄 Rule **#{rule_id}** is now **{status}**"
                )
            else:
                await interaction.followup.send(f"Rule **#{rule_id}** not found.")
        except Exception as exc:
            await interaction.followup.send(f"Failed to toggle rule: {exc}")

    @app_commands.command(name="scaling-events")
    @app_commands.describe(limit="Number of recent events to show (default 10)")
    async def recent_events(self, interaction: discord.Interaction, limit: int = 10):
        """Show recent auto-scaling events."""
        await interaction.response.defer()
        if not self.engine:
            await interaction.followup.send("Scaling engine is not running.")
            return

        events = self.engine._recent_events[-limit:][::-1]
        if not events:
            await interaction.followup.send("No recent scaling events.")
            return

        embed = discord.Embed(
            title="Recent Scaling Events",
            color=discord.Color.gold(),
            timestamp=datetime.utcnow(),
        )
        for e in events:
            icon = "📈" if e.action == "scale_up" else "📉"
            embed.add_field(
                name=f"{icon} {self._get_server_name(e.container_id)}",
                value=(
                    f"Rule #{e.rule_id}: {e.metric} was {e.value:.1f}% (threshold {e.threshold}%)\n"
                    f"CPU: {e.previous_cores} → {e.new_cores}  |  RAM: {e.previous_memory_mb} → {e.new_memory_mb} MB\n"
                    f"{'✅ Success' if e.success else '❌ Failed'}: {e.message[:80]}"
                ),
                inline=False,
            )
        await interaction.followup.send(embed=embed)


async def setup(bot):
    await bot.add_cog(AutoScaler(bot))
