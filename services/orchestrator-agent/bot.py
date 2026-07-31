# NOTE: This is a legacy standalone implementation. Use main.py instead,
# which loads all 29 cogs from the cogs/ directory.
# This file has been refactored to replace the flat-file database with
# PostgreSQL and remove duplicate function definitions.

import asyncio
import concurrent.futures
import logging
import os
import random
import re
import subprocess
import sys
import time
from datetime import datetime, timedelta
from threading import Lock

import discord
import docker
import requests
from discord import app_commands
from discord.ext import commands, tasks

# -----------------------------------------------------------------------------
# Bot Configuration and Global Variables
# -----------------------------------------------------------------------------

# Bot token and configuration settings
TOKEN = os.getenv("DISCORD_BOT_TOKEN", "")
RAM_LIMIT = "1g"
SERVER_LIMIT = 1

# Docker client for container management
client = docker.from_env()

# Discord bot intents and bot/client initialization
intents = discord.Intents.default()
intents.messages = False
intents.message_content = False
bot = commands.Bot(command_prefix="/", intents=intents)

# A set of whitelisted user IDs (admin privileges)
whitelist_ids = set(filter(None, os.getenv("WHITELIST_IDS", "").split(",")))

# In-memory dictionaries (should be replaced with persistent storage in production)
user_credits = {}
vps_renewals = {}

# API key for the cuty.io URL-shortening service
API_KEY = os.getenv("CUTTLY_API_KEY", "")

# Public IP address used in port forwarding commands
PUBLIC_IP = os.getenv("PUBLIC_IP", "")
database_lock = Lock()
SAFE_CONTAINER_RE = re.compile(r"^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,127}$")

# -----------------------------------------------------------------------------
# Database Helper (PostgreSQL via psycopg2, falls back to flat file)
# -----------------------------------------------------------------------------


def _get_db_connection():
    """Create a synchronous PostgreSQL connection, or None if unavailable."""
    try:
        from db import get_sync_connection

        return get_sync_connection()
    except Exception:
        return None


def add_to_database(userid, container_name, ssh_command):
    """Record a VPS instance to the database (PostgreSQL primary, flat file fallback)."""
    conn = _get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO vps_containers (container_id, user_id, container_name, ssh_command) "
                "VALUES (%s, %s, %s, %s) ON CONFLICT (container_id) DO NOTHING",
                (
                    container_name[:255],
                    str(userid),
                    container_name[:255],
                    ssh_command or "",
                ),
            )
            conn.commit()
            cursor.close()
            conn.close()
            return
        except Exception:
            conn.close()
    # Fallback to flat file
    with database_lock:
        with open("database.txt", "a", encoding="utf-8") as f:
            f.write(f"{userid}|{container_name}|{ssh_command}\n")


def remove_from_database(ssh_command):
    """Remove a VPS instance from the database."""
    conn = _get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM vps_containers WHERE ssh_command = %s",
                (ssh_command,),
            )
            conn.commit()
            cursor.close()
            conn.close()
            return
        except Exception:
            conn.close()
    if not os.path.exists("database.txt"):
        return
    with database_lock:
        with open("database.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
        with open("database.txt", "w", encoding="utf-8") as f:
            for line in lines:
                if ssh_command not in line:
                    f.write(line)


def _is_safe_container_name(name: str) -> bool:
    return bool(SAFE_CONTAINER_RE.fullmatch(name))


def get_user_servers(user):
    """Return a list of VPS entries for the given user."""
    conn = _get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT container_id, user_id, container_name, ssh_command "
                "FROM vps_containers WHERE user_id = %s",
                (str(user),),
            )
            rows = cursor.fetchall()
            cursor.close()
            conn.close()
            return [f"{row[1]}|{row[0]}|{row[3] or ''}" for row in rows]
        except Exception:
            conn.close()
    if not os.path.exists("database.txt"):
        return []
    servers = []
    with open("database.txt", "r") as f:
        for line in f:
            if line.startswith(str(user)):
                servers.append(line.strip())
    return servers


def count_user_servers(userid):
    """Return the number of VPS instances for a given user."""
    return len(get_user_servers(str(userid)))


def get_container_id_from_database(userid, container_name=None):
    """Retrieve a container ID for a user, optionally matching by name."""
    conn = _get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            if container_name:
                cursor.execute(
                    "SELECT container_id FROM vps_containers "
                    "WHERE user_id = %s AND (container_id = %s OR container_name = %s)",
                    (str(userid), container_name, container_name),
                )
            else:
                cursor.execute(
                    "SELECT container_id FROM vps_containers "
                    "WHERE user_id = %s LIMIT 1",
                    (str(userid),),
                )
            row = cursor.fetchone()
            cursor.close()
            conn.close()
            if row:
                return row[0]
        except Exception:
            conn.close()
    if not os.path.exists("database.txt"):
        return None
    with open("database.txt", "r") as f:
        for line in f:
            if line.startswith(str(userid)) and (
                not container_name or container_name in line
            ):
                return line.split("|")[1]
    return None


def get_ssh_command_from_database(container_id):
    """Retrieve the SSH command for a container ID."""
    conn = _get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT ssh_command FROM vps_containers WHERE container_id = %s",
                (container_id,),
            )
            row = cursor.fetchone()
            cursor.close()
            conn.close()
            if row:
                return row[0]
        except Exception:
            conn.close()
    if not os.path.exists("database.txt"):
        return None
    with open("database.txt", "r") as f:
        for line in f:
            if container_id in line:
                return line.split("|")[2] if "|" in line else None
    return None


def generate_random_port():
    """Generate a random available port number."""
    return random.randint(1025, 65535)


async def capture_ssh_session_line(process):
    """Capture the SSH session command line from process output."""
    while True:
        output = await process.stdout.readline()
        if not output:
            break
        output = output.decode("utf-8").strip()
        if "ssh session:" in output:
            return output.split("ssh session:")[1].strip()
    return None


async def capture_output(process, keyword):
    """Read process output until a line containing the keyword is found."""
    while True:
        output = await process.stdout.readline()
        if not output:
            break
        output = output.decode("utf-8").strip()
        if keyword in output:
            return output
    return None


# -----------------------------------------------------------------------------
# Discord Bot Commands
# -----------------------------------------------------------------------------


@bot.tree.command(
    name="earncredit", description="Generate a URL to shorten and earn credits."
)
async def earncredit(interaction: discord.Interaction):
    """Shorten a predetermined URL using the cuty.io API to earn credits."""
    user_id = interaction.user.id
    default_url = "https://cuty.io/e58WUzLMmE3S"
    api_url = f"https://cutt.ly/api/api.php?key={API_KEY}&short={default_url}"
    try:
        response = requests.get(api_url, timeout=10).json()
    except Exception:
        await interaction.response.send_message(
            "Failed to reach URL shortener service."
        )
        return
    if response.get("url", {}).get("status") == 7:
        shortened_url = response["url"]["shortLink"]
        credits_earned = 1
        user_credits[user_id] = user_credits.get(user_id, 0) + credits_earned
        await interaction.response.send_message(
            f"Success! Here's your shortened URL: {shortened_url}. You earned {credits_earned} credit!"
        )
    else:
        error_message = response.get("url", {}).get(
            "title", "Failed to generate a shortened URL."
        )
        await interaction.response.send_message(error_message)


@bot.tree.command(name="bal", description="Check your credit balance.")
async def bal(interaction: discord.Interaction):
    """Show the user their current credit balance."""
    user_id = interaction.user.id
    credits = user_credits.get(user_id, 0)
    await interaction.response.send_message(f"You have {credits} credits.")


@bot.tree.command(
    name="port-forward-new",
    description="Set up port forwarding for a container using localhost.run.",
)
@app_commands.describe(
    container_name="The name of the container",
    container_port="The internal container port to forward",
)
async def port_forward_win(
    interaction: discord.Interaction, container_name: str, container_port: int
):
    """Set up port forwarding using localhost.run."""
    await interaction.response.defer()
    try:
        if not _is_safe_container_name(container_name):
            await interaction.followup.send("Invalid container name.", ephemeral=True)
            return
        process = await asyncio.create_subprocess_exec(
            "docker",
            "exec",
            "-i",
            container_name,
            "ssh",
            "-R",
            f"80:localhost:{container_port}",
            "ssh.localhost.run",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        if stdout:
            output = stdout.decode().strip()
            await interaction.followup.send(
                embed=discord.Embed(
                    description=f"### Port Forwarding Successful:\n{output}",
                    color=0x00FF00,
                )
            )
        if stderr:
            error = stderr.decode().strip()
            await interaction.followup.send(
                embed=discord.Embed(
                    description=f"### Error in Port Forwarding:\n{error}",
                    color=0xFF0000,
                )
            )
    except Exception as e:
        await interaction.followup.send(
            embed=discord.Embed(
                description="### Failed to set up port forwarding.", color=0xFF0000
            )
        )


def get_node_status():
    """Retrieve Docker container statuses and system memory usage."""
    try:
        containers = client.containers.list(all=True)
        container_status = (
            "\n".join(
                [f"{container.name} - {container.status}" for container in containers]
            )
            or "No containers running."
        )
        with open("/proc/meminfo", "r") as f:
            meminfo = f.read()
        mem_total = int(re.search(r"MemTotal:\s+(\d+)", meminfo).group(1)) / 1024
        mem_free = int(re.search(r"MemFree:\s+(\d+)", meminfo).group(1)) / 1024
        mem_available = (
            int(re.search(r"MemAvailable:\s+(\d+)", meminfo).group(1)) / 1024
        )
        memory_used = mem_total - mem_available
        memory_percentage = (memory_used / mem_total) * 100 if mem_total else 0
        return {
            "containers": container_status,
            "memory_total": mem_total,
            "memory_used": memory_used,
            "memory_percentage": memory_percentage,
        }
    except Exception as e:
        return str(e)


@bot.tree.command(name="node", description="Show the current status of the VPS node.")
async def node_status(interaction: discord.Interaction):
    """Display the VPS node's container status and memory usage."""
    try:
        node_info = get_node_status()
        if isinstance(node_info, str):
            await interaction.response.send_message(
                embed=discord.Embed(
                    description=f"### Error fetching node status: {node_info}",
                    color=0xFF0000,
                )
            )
            return
        embed = discord.Embed(title="VPS Node1 Status", color=0x00FF00)
        embed.add_field(name="Containers", value=node_info["containers"], inline=False)
        embed.add_field(
            name="Memory Usage",
            value=f"{node_info['memory_used']:.2f} / {node_info['memory_total']:.2f} MB ({node_info['memory_percentage']:.2f}%)",
            inline=False,
        )
        await interaction.response.send_message(embed=embed)
    except Exception as e:
        await interaction.response.send_message(
            embed=discord.Embed(
                description=f"### Failed to fetch node status: {str(e)}", color=0xFF0000
            )
        )


@bot.tree.command(name="renew", description="Renew a VPS for 8 days using 2 credits.")
@app_commands.describe(vps_id="ID of the VPS to renew")
async def renew(interaction: discord.Interaction, vps_id: str):
    """Renew a VPS by extending its duration by 8 days (costs 2 credits)."""
    user_id = str(interaction.user.id)
    credits = user_credits.get(user_id, 0)
    if credits < 2:
        await interaction.response.send_message(
            embed=discord.Embed(
                description="You don't have enough credits to renew the VPS. You need 2 credits.",
                color=0xFF0000,
            )
        )
        return
    container_id = get_container_id_from_database(user_id, vps_id)
    if not container_id:
        await interaction.response.send_message(
            embed=discord.Embed(
                description=f"VPS with ID {vps_id} not found.", color=0xFF0000
            )
        )
        return
    user_credits[user_id] -= 2
    renewal_date = datetime.now() + timedelta(days=8)
    vps_renewals[vps_id] = renewal_date
    await interaction.response.send_message(
        embed=discord.Embed(
            description=f"VPS {vps_id} has been renewed for 8 days. New expiry date: {renewal_date.strftime('%Y-%m-%d')}. "
            f"You now have {user_credits[user_id]} credits remaining.",
            color=0x00FF00,
        )
    )


async def remove_everything_task(interaction: discord.Interaction):
    """Remove all Docker containers and clear database."""
    await interaction.channel.send("### Node is full. Resetting all user instances...")
    try:
        for container in client.containers.list(all=True):
            container.remove(force=True)
        if os.path.exists("database.txt"):
            os.remove("database.txt")
        await interaction.channel.send("### All instances and data have been reset.")
    except Exception as e:
        await interaction.channel.send("### Failed to reset instances.")


@bot.tree.command(
    name="killvps", description="Kill all user VPS instances. Admin only."
)
async def kill_vps(interaction: discord.Interaction):
    """Admin-only command to terminate all VPS instances."""
    userid = str(interaction.user.id)
    if userid not in whitelist_ids:
        await interaction.response.send_message(
            embed=discord.Embed(
                description="You do not have permission to use this command.",
                color=0xFF0000,
            )
        )
        return
    await remove_everything_task(interaction)
    await interaction.response.send_message(
        embed=discord.Embed(
            description="### All user VPS instances have been terminated.",
            color=0x00FF00,
        )
    )


@bot.tree.command(
    name="remove-everything", description="Removes all data and containers"
)
async def remove_everything(interaction: discord.Interaction):
    """Admin-only command to remove all Docker containers and data."""
    userid = str(interaction.user.id)
    if userid not in whitelist_ids:
        await interaction.response.send_message(
            embed=discord.Embed(
                description="You do not have permission to use this command.",
                color=0xFF0000,
            )
        )
        return
    try:
        for container in client.containers.list(all=True):
            container.remove(force=True)
        await interaction.response.send_message(
            embed=discord.Embed(
                description="All Docker containers have been removed.", color=0x00FF00
            )
        )
    except Exception as e:
        await interaction.response.send_message(
            embed=discord.Embed(
                description="Failed to remove Docker containers.", color=0xFF0000
            )
        )
    try:
        if os.path.exists("database.txt"):
            os.remove("database.txt")
        await interaction.response.send_message(
            embed=discord.Embed(
                description="Database has been cleared.", color=0x00FF00
            )
        )
    except Exception as e:
        await interaction.response.send_message(
            embed=discord.Embed(description="Failed to clear database.", color=0xFF0000)
        )


@bot.event
async def on_ready():
    """Sync commands and log ready status."""
    print(f"Bot is ready. Logged in as {bot.user}")
    await bot.tree.sync()


async def regen_ssh_command(interaction: discord.Interaction, container_name: str):
    """Regenerate the SSH session command for a VPS."""
    user = str(interaction.user)
    container_id = get_container_id_from_database(user, container_name)
    if not container_id:
        await interaction.response.send_message(
            embed=discord.Embed(
                description="### No active instance found for your user.",
                color=0xFF0000,
            )
        )
        return
    try:
        exec_cmd = await asyncio.create_subprocess_exec(
            "docker",
            "exec",
            container_id,
            "tmate",
            "-F",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
    except subprocess.CalledProcessError as e:
        await interaction.response.send_message(
            embed=discord.Embed(
                description=f"Error executing tmate in Docker container: {e}",
                color=0xFF0000,
            )
        )
        return
    ssh_session_line = await capture_ssh_session_line(exec_cmd)
    if ssh_session_line:
        await interaction.user.send(
            embed=discord.Embed(
                description=f"### New SSH Session Command: ```{ssh_session_line}```",
                color=0x00FF00,
            )
        )
        await interaction.response.send_message(
            embed=discord.Embed(
                description="### New SSH session generated. Check your DMs for details.",
                color=0x00FF00,
            )
        )
    else:
        await interaction.response.send_message(
            embed=discord.Embed(
                description="### Failed to generate new SSH session.", color=0xFF0000
            )
        )


async def start_server(interaction: discord.Interaction, container_name: str):
    """Start a VPS instance and retrieve a new SSH session."""
    userid = str(interaction.user.id)
    container_id = get_container_id_from_database(userid, container_name)
    if not container_id:
        await interaction.response.send_message(
            embed=discord.Embed(
                description="### No instance found for your user.", color=0xFF0000
            )
        )
        return
    try:
        subprocess.run(["docker", "start", container_id], check=True)
        exec_cmd = await asyncio.create_subprocess_exec(
            "docker",
            "exec",
            container_id,
            "tmate",
            "-F",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        ssh_session_line = await capture_ssh_session_line(exec_cmd)
        if ssh_session_line:
            await interaction.user.send(
                embed=discord.Embed(
                    description=f"### Instance Started\nSSH Session Command: ```{ssh_session_line}```",
                    color=0x00FF00,
                )
            )
            await interaction.response.send_message(
                embed=discord.Embed(
                    description="### Instance started successfully. Check your DMs for details.",
                    color=0x00FF00,
                )
            )
        else:
            await interaction.response.send_message(
                embed=discord.Embed(
                    description="### Instance started, but failed to get SSH session line.",
                    color=0xFF0000,
                )
            )
    except subprocess.CalledProcessError as e:
        await interaction.response.send_message(
            embed=discord.Embed(
                description=f"Error starting instance: {e}", color=0xFF0000
            )
        )


async def stop_server(interaction: discord.Interaction, container_name: str):
    """Stop a running VPS instance."""
    userid = str(interaction.user.id)
    container_id = get_container_id_from_database(userid, container_name)
    if not container_id:
        await interaction.response.send_message(
            embed=discord.Embed(
                description="### No instance found for your user.", color=0xFF0000
            )
        )
        return
    try:
        subprocess.run(["docker", "stop", container_id], check=True)
        await interaction.response.send_message(
            embed=discord.Embed(
                description="### Instance stopped successfully.", color=0x00FF00
            )
        )
    except subprocess.CalledProcessError as e:
        await interaction.response.send_message(
            embed=discord.Embed(
                description=f"### Error stopping instance: {e}", color=0xFF0000
            )
        )


async def restart_server(interaction: discord.Interaction, container_name: str):
    """Restart a VPS instance and refresh its SSH session."""
    userid = str(interaction.user.id)
    container_id = get_container_id_from_database(userid, container_name)
    if not container_id:
        await interaction.response.send_message(
            embed=discord.Embed(
                description="### No instance found for your user.", color=0xFF0000
            )
        )
        return
    try:
        subprocess.run(["docker", "restart", container_id], check=True)
        exec_cmd = await asyncio.create_subprocess_exec(
            "docker",
            "exec",
            container_id,
            "tmate",
            "-F",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        ssh_session_line = await capture_ssh_session_line(exec_cmd)
        if ssh_session_line:
            await interaction.user.send(
                embed=discord.Embed(
                    description=f"### Instance Restarted\nSSH Session Command: ```{ssh_session_line}```\nOS: Ubuntu 22.04",
                    color=0x00FF00,
                )
            )
            await interaction.response.send_message(
                embed=discord.Embed(
                    description="### Instance restarted successfully. Check your DMs for details.",
                    color=0x00FF00,
                )
            )
        else:
            await interaction.response.send_message(
                embed=discord.Embed(
                    description="### Instance restarted, but failed to get SSH session line.",
                    color=0xFF0000,
                )
            )
    except subprocess.CalledProcessError as e:
        await interaction.response.send_message(
            embed=discord.Embed(
                description=f"Error restarting instance: {e}", color=0xFF0000
            )
        )


async def create_server_task(interaction):
    """Create a new VPS instance (Docker container)."""
    await interaction.response.send_message(
        embed=discord.Embed(
            description="### Creating Instance, this may take a few seconds.",
            color=0x00FF00,
        )
    )
    userid = str(interaction.user.id)
    if count_user_servers(userid) >= SERVER_LIMIT:
        await interaction.followup.send(
            embed=discord.Embed(
                description="```Error: Instance Limit reached```", color=0xFF0000
            )
        )
        return
    image = "ubuntu-22.04-with-tmate"
    try:
        container_id = (
            subprocess.check_output(
                [
                    "docker",
                    "run",
                    "-itd",
                    "--privileged",
                    "--hostname",
                    "crashcloud",
                    "--cap-add=ALL",
                    image,
                ]
            )
            .strip()
            .decode("utf-8")
        )
    except subprocess.CalledProcessError as e:
        await interaction.followup.send(
            embed=discord.Embed(
                description=f"### Error creating Docker container: {e}", color=0xFF0000
            )
        )
        return
    try:
        exec_cmd = await asyncio.create_subprocess_exec(
            "docker",
            "exec",
            container_id,
            "tmate",
            "-F",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
    except subprocess.CalledProcessError as e:
        await interaction.followup.send(
            embed=discord.Embed(
                description=f"### Error executing tmate in Docker container: {e}",
                color=0xFF0000,
            )
        )
        subprocess.run(["docker", "kill", container_id])
        subprocess.run(["docker", "rm", container_id])
        return
    ssh_session_line = await capture_ssh_session_line(exec_cmd)
    if ssh_session_line:
        await interaction.user.send(
            embed=discord.Embed(
                description=f"### Successfully created Instance\nSSH Session Command: ```{ssh_session_line}```\nOS: Ubuntu 22.04\nPassword: root",
                color=0x00FF00,
            )
        )
        add_to_database(userid, container_id, ssh_session_line)
        await interaction.followup.send(
            embed=discord.Embed(
                description="### Instance created successfully. Check your DMs for details.",
                color=0x00FF00,
            )
        )
    else:
        await interaction.followup.send(
            embed=discord.Embed(
                description="### Something went wrong or the Instance is taking longer than expected. Contact Support if the issue persists.",
                color=0xFF0000,
            )
        )
        subprocess.run(["docker", "kill", container_id])
        subprocess.run(["docker", "rm", container_id])


@bot.tree.command(
    name="deploy", description="Creates a new instance with Ubuntu 22.04."
)
async def deploy_ubuntu(interaction: discord.Interaction):
    """Deploy a new Ubuntu 22.04-based VPS instance."""
    await create_server_task(interaction)


@bot.tree.command(
    name="regen-ssh", description="Generates a new SSH session for your instance."
)
@app_commands.describe(container_name="The identifier of your instance")
async def regen_ssh(interaction: discord.Interaction, container_name: str):
    """Regenerate the SSH session command for a VPS."""
    await regen_ssh_command(interaction, container_name)


@bot.tree.command(name="start", description="Starts your instance.")
@app_commands.describe(container_name="The identifier of your instance")
async def start(interaction: discord.Interaction, container_name: str):
    """Start a paused or stopped VPS instance."""
    await start_server(interaction, container_name)


@bot.tree.command(name="stop", description="Stops your instance.")
@app_commands.describe(container_name="The identifier of your instance")
async def stop(interaction: discord.Interaction, container_name: str):
    """Stop a running VPS instance."""
    await stop_server(interaction, container_name)


@bot.tree.command(name="restart", description="Restarts your instance.")
@app_commands.describe(container_name="The identifier of your instance")
async def restart(interaction: discord.Interaction, container_name: str):
    """Restart a VPS instance and refresh its SSH session."""
    await restart_server(interaction, container_name)


@bot.tree.command(name="ping", description="Check the bot's latency.")
async def ping(interaction: discord.Interaction):
    """Check and display the bot's current latency."""
    await interaction.response.defer()
    latency = round(bot.latency * 1000)
    embed = discord.Embed(
        title="Pong!", description=f"Latency: {latency}ms", color=discord.Color.green()
    )
    await interaction.response.send_message(embed=embed)


@bot.tree.command(name="list", description="Lists all your instances.")
async def list_servers(interaction: discord.Interaction):
    """List all VPS instances deployed by the user."""
    await interaction.response.defer()
    userid = str(interaction.user.id)
    servers = get_user_servers(userid)
    if servers:
        embed = discord.Embed(title="Your Instances", color=0x00FF00)
        for server in servers:
            _, container_name, _ = server.split("|")
            embed.add_field(
                name=container_name, value="32GB RAM - Premium - 4 cores", inline=False
            )
        await interaction.followup.send(embed=embed)
    else:
        await interaction.followup.send(
            embed=discord.Embed(description="You have no servers.", color=0xFF0000)
        )


@bot.tree.command(name="port-add", description="Adds a port forwarding rule.")
@app_commands.describe(
    container_name="The name of the container",
    container_port="The internal container port",
)
async def port_add(
    interaction: discord.Interaction, container_name: str, container_port: int
):
    """Set up a port forwarding rule via serveo.net."""
    await interaction.response.send_message(
        embed=discord.Embed(
            description="### Setting up port forwarding. This might take a moment...",
            color=0x00FF00,
        )
    )
    public_port = generate_random_port()
    try:
        if not _is_safe_container_name(container_name):
            await interaction.followup.send("Invalid container name.", ephemeral=True)
            return
        await asyncio.create_subprocess_exec(
            "docker",
            "exec",
            container_name,
            "ssh",
            "-o",
            "StrictHostKeyChecking=no",
            "-R",
            f"{public_port}:localhost:{container_port}",
            "serveo.net",
            "-N",
            "-f",
            stdout=asyncio.subprocess.DEVNULL,
            stderr=asyncio.subprocess.DEVNULL,
        )
        await interaction.followup.send(
            embed=discord.Embed(
                description=f"### Port added successfully. Your service is hosted on {PUBLIC_IP}:{public_port}.",
                color=0x00FF00,
            )
        )
    except Exception as e:
        await interaction.followup.send(
            embed=discord.Embed(
                description="### An unexpected error occurred.", color=0xFF0000
            )
        )


@bot.tree.command(
    name="port-http", description="Forward HTTP traffic to your container."
)
@app_commands.describe(
    container_name="The name of your container",
    container_port="The internal container port to forward",
)
async def port_forward_website(
    interaction: discord.Interaction, container_name: str, container_port: int
):
    """Forward HTTP traffic to a container port using serveo.net."""
    try:
        exec_cmd = await asyncio.create_subprocess_exec(
            "docker",
            "exec",
            container_name,
            "ssh",
            "-o StrictHostKeyChecking=no",
            "-R",
            f"80:localhost:{container_port}",
            "serveo.net",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        url_line = await capture_output(exec_cmd, "Forwarding HTTP traffic from")
        if url_line:
            url = url_line.split(" ")[-1]
            await interaction.response.send_message(
                embed=discord.Embed(
                    description=f"### Website forwarded successfully. Your website is accessible at {url}.",
                    color=0x00FF00,
                )
            )
        else:
            await interaction.response.send_message(
                embed=discord.Embed(
                    description="### Failed to capture forwarding URL.", color=0xFF0000
                )
            )
    except subprocess.CalledProcessError as e:
        await interaction.response.send_message(
            embed=discord.Embed(
                description=f"### Error executing website forwarding: {e}",
                color=0xFF0000,
            )
        )


@bot.tree.command(name="remove", description="Removes an instance.")
@app_commands.describe(container_name="The identifier of your instance")
async def remove_server(interaction: discord.Interaction, container_name: str):
    """Remove a VPS instance by stopping and deleting its container."""
    await interaction.response.defer()
    userid = str(interaction.user.id)
    container_id = get_container_id_from_database(userid, container_name)
    if not container_id:
        await interaction.response.send_message(
            embed=discord.Embed(
                description="### No instance found for your user with that name.",
                color=0xFF0000,
            )
        )
        return
    try:
        subprocess.run(["docker", "stop", container_id], check=True)
        subprocess.run(["docker", "rm", container_id], check=True)
        remove_from_database(container_id)
        await interaction.response.send_message(
            embed=discord.Embed(
                description=f"Instance '{container_name}' removed successfully.",
                color=0x00FF00,
            )
        )
    except subprocess.CalledProcessError as e:
        await interaction.response.send_message(
            embed=discord.Embed(
                description=f"Error removing instance: {e}", color=0xFF0000
            )
        )


@bot.tree.command(name="help", description="Shows the help message.")
async def help_command(interaction: discord.Interaction):
    """Display an embedded help message."""
    embed = discord.Embed(title="Help", color=0x00FF00)
    embed.add_field(
        name="/deploy", value="Creates a new instance with Ubuntu 22.04.", inline=False
    )
    embed.add_field(
        name="/remove <ssh_command/Name>", value="Removes a server.", inline=False
    )
    embed.add_field(
        name="/start <ssh_command/Name>", value="Starts a server.", inline=False
    )
    embed.add_field(
        name="/stop <ssh_command/Name>", value="Stops a server.", inline=False
    )
    embed.add_field(
        name="/regen-ssh <ssh_command/Name>",
        value="Regenerates SSH credentials.",
        inline=False,
    )
    embed.add_field(
        name="/restart <ssh_command/Name>", value="Restarts a server.", inline=False
    )
    embed.add_field(name="/list", value="Lists all your servers.", inline=False)
    embed.add_field(name="/ping", value="Checks the bot's latency.", inline=False)
    embed.add_field(
        name="/node", value="Shows the node storage and memory usage.", inline=False
    )
    embed.add_field(
        name="/bal", value="Displays your current credit balance.", inline=False
    )
    embed.add_field(name="/renew", value="Renews your VPS.", inline=False)
    embed.add_field(
        name="/earncredit", value="Earn credits by shortening a URL.", inline=False
    )
    await interaction.response.send_message(embed=embed)


# -----------------------------------------------------------------------------
# Run the Bot
# -----------------------------------------------------------------------------

logging.warning(
    "NOTE: bot.py is a legacy standalone implementation. Use main.py instead for the full feature set."
)
bot.run(TOKEN)
