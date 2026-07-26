"""Orchestrator Agent entry point - Discord bot with webhook server."""

import asyncio
import logging
import os
import sys

import discord
from discord.ext import commands
from aiohttp import web

from config import config
from integration import init_database_tables

logger = logging.getLogger(__name__)

BOT_PREFIX = "/"

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix=BOT_PREFIX, intents=intents)
bot.config = config

CORE_COGS = [
    "cogs.vps_commands",
    "cogs.vps_pricing",
    "cogs.vps_billing",
    "cogs.prepaid_billing",
    "cogs.monitoring",
    "cogs.bot_commands",
    "cogs.health_checks",
    "cogs.backup_manager",
    "cogs.resource_manager",
    "cogs.template_manager",
    "cogs.task_scheduler",
    "cogs.alert_manager",
    "cogs.cleanup",
    "cogs.database_manager",
    "cogs.modpack_installer",
    "cogs.update_manager",
]


async def load_cogs():
    """Load all core Discord cogs."""
    for cog in CORE_COGS:
        try:
            await bot.load_extension(cog)
            logger.info("Loaded cog: %s", cog)
        except commands.errors.ExtensionAlreadyLoaded:
            logger.warning("Cog already loaded: %s", cog)
        except Exception as exc:
            logger.error("Failed to load cog %s: %s", cog, exc)


@bot.event
async def on_ready():
    """Handle the bot ready event - initialise DB and sync commands."""
    logger.info("Bot ready. Logged in as %s", bot.user)
    try:
        init_database_tables()
        logger.info("Database tables initialised")
    except Exception as exc:
        logger.warning("Database initialisation skipped: %s", exc)

    await bot.tree.sync()
    logger.info("Commands synced")
    asyncio.create_task(start_webhook_server(bot))


async def start_webhook_server(bot_instance: commands.Bot):
    """Start the aiohttp webhook server for GitOps and health endpoints.

    Args:
        bot_instance: The Discord bot instance to attach webhook routes from.
    """
    app = web.Application()

    async def health(request: web.Request) -> web.Response:
        return web.json_response({
            "status": "ok",
            "service": "orchestrator-agent",
        })

    app.router.add_get("/health", health)

    cog = bot_instance.get_cog("GitDeployer")
    if cog:
        app.router.add_post(
            "/webhook/github/{deploy_id}", cog.handle_webhook
        )
        app.router.add_post("/webhook/github", cog.handle_webhook)

    gitops_cog = bot_instance.get_cog("GitOpsSync")
    if gitops_cog:
        app.router.add_post("/webhook/gitops", gitops_cog.handle_webhook)

    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.getenv("GITOPS_WEBHOOK_PORT", "8500"))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()
    logger.info("Webhook server listening on port %d", port)


async def run_health_only():
    """Run only the health/webhook server without the Discord bot."""
    await start_webhook_server(bot)
    await asyncio.Event().wait()


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[logging.StreamHandler()],
    )

    token_missing = (
        not config.DISCORD_BOT_TOKEN
        or config.DISCORD_BOT_TOKEN == "your_discord_bot_token_here"
    )
    disabled = os.getenv("ORCHESTRATOR_AGENT_DISABLED", "true").lower() == "true"

    if token_missing or disabled:
        logger.warning(
            "Discord bot disabled; starting health/webhook server only"
        )
        try:
            asyncio.run(run_health_only())
        except KeyboardInterrupt:
            logger.info("Server shutting down")
        sys.exit(0)

    asyncio_loop = None
    try:
        asyncio_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(asyncio_loop)
        asyncio_loop.run_until_complete(load_cogs())
        bot.run(config.DISCORD_BOT_TOKEN)
    except KeyboardInterrupt:
        logger.info("Bot shutting down")
    finally:
        if asyncio_loop:
            asyncio_loop.close()
