const { spawn, execFile } = require('child_process');
const { EmbedBuilder } = require('discord.js');
const { query } = require('./db');
const { docker, containers } = require('./docker');

const COMMAND_SPECS = [
  { name: 'node', description: 'Display node status', type: 1 },
  { name: 'deploy', description: 'Deploy a new SSH VPS', type: 1 },
  {
    name: 'regen-ssh',
    description: 'Regenerate SSH credentials',
    options: [{ name: 'container_name', description: 'Container name or ID', type: 3, required: true }],
  },
  { name: 'earncredit', description: 'Earn credits by shortening a URL', type: 1 },
  { name: 'bal', description: 'Check your credit balance', type: 1 },
  {
    name: 'renew',
    description: 'Renew a VPS for 8 days (costs 2 credits)',
    options: [{ name: 'vps_id', description: 'ID of the VPS to renew', type: 3, required: true }],
  },
  {
    name: 'port-add',
    description: 'Add SSH port forwarding via serveo',
    options: [
      { name: 'container_name', description: 'Container name', type: 3, required: true },
      { name: 'container_port', description: 'Internal port', type: 4, required: true },
    ],
  },
  {
    name: 'port-http',
    description: 'Forward HTTP traffic via serveo',
    options: [
      { name: 'container_name', description: 'Container name', type: 3, required: true },
      { name: 'container_port', description: 'Internal HTTP port', type: 4, required: true },
    ],
  },
];

function toSpec() {
  return COMMAND_SPECS;
}

function isParsed(name) {
  return COMMAND_SPECS.some((c) => c.name === name);
}

async function ensureTable() {
  await query(`
    CREATE TABLE IF NOT EXISTS user_credits (
      user_id VARCHAR(255) PRIMARY KEY,
      credits INT DEFAULT 0,
      renewals JSONB DEFAULT '{}'::jsonb,
      updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
  `);
}

async function getCredits(userId) {
  const result = await query('SELECT credits FROM user_credits WHERE user_id = $1', [userId]).catch(() => null);
  return result && result.rows.length ? result.rows[0].credits : 0;
}

async function addCredits(userId, amount) {
  await query(
    `INSERT INTO user_credits (user_id, credits) VALUES ($1, $2)
     ON CONFLICT (user_id) DO UPDATE SET credits = user_credits.credits + $2, updated_at = NOW()`,
    [userId, amount]
  );
}

async function spendCredits(userId, amount) {
  const result = await query(
    `UPDATE user_credits SET credits = credits - $2, updated_at = NOW()
     WHERE user_id = $1 AND credits >= $2 RETURNING credits`,
    [userId, amount]
  ).catch(() => null);
  return result && result.rows.length ? result.rows[0].credits : null;
}

function captureLine(args, keyword, timeoutMs = 30000) {
  return new Promise((resolve) => {
    const child = spawn('docker', args);
    let output = '';
    const timer = setTimeout(() => {
      child.kill();
      resolve(null);
    }, timeoutMs);
    child.stdout.on('data', (data) => {
      output += data.toString();
      if (output.toLowerCase().includes(keyword.toLowerCase())) {
        clearTimeout(timer);
        child.kill();
        resolve(output);
      }
    });
    child.on('close', () => {
      clearTimeout(timer);
      resolve(output.trim() || null);
    });
  });
}

const DEFAULT_SSH_IMAGE = process.env.DEFAULT_SSH_IMAGE || 'ubuntu:22.04';
const PUBLIC_IP = process.env.PUBLIC_IP || '127.0.0.1';
const SERVER_LIMIT = parseInt(process.env.SERVER_LIMIT, 10) || 5;

async function handle(interaction) {
  const client = interaction.client;
  const vpsManager = require('./vpsManager');
  try { await ensureTable(); } catch (err) { console.error('[$] credits table setup failed:', err.message); }

  if (interaction.commandName === 'node') {
    const list = await containers();
    const embed = new EmbedBuilder()
      .setTitle('VPS Node Status')
      .setColor(0x28a745)
      .addFields(
        { name: 'Containers', value: list.map((c) => `${c.Name} - ${c.Status}`).join('\n') || 'No containers.', inline: false },
        { name: 'Total Containers', value: String(list.length), inline: true },
        { name: 'Running', value: String(list.filter((c) => c.Status.includes('Up')).length), inline: true }
      );
    return interaction.reply({ embeds: [embed], ephemeral: true });
  }

  if (interaction.commandName === 'deploy') {
    await interaction.deferReply({ ephemeral: true });
    const owned = await vpsManager.getContainersForUser(interaction.user.id);
    if (owned.length >= SERVER_LIMIT) return interaction.editReply({ content: '❌ Instance limit reached.' });
    try {
      const containerId = await docker([
        'run', '-itd', '--hostname', 'vps',
        '--cap-drop=ALL', '--security-opt', 'no-new-privileges',
        DEFAULT_SSH_IMAGE,
      ], { timeout: 120000 });
      if (!containerId) return interaction.editReply({ content: '❌ Creation failed. Please try again.' });
      const line = await captureLine(['exec', containerId, 'tmate', '-F'], 'ssh session:');
      if (line) {
        const sshSession = line.split('ssh session:')[1].trim();
        await vpsManager.addToDatabase(interaction.user.id, containerId, `vps_${containerId.slice(0, 8)}`, sshSession);
        await interaction.user.send(`**Instance created!**\nSSH: \`\`\`${sshSession}\`\`\`\nOS: Ubuntu 22.04`).catch(() => {});
        return interaction.editReply({ content: '✅ Instance created. Check your DMs for SSH details.' });
      }
      await docker(['kill', containerId]).catch(() => {});
      await docker(['rm', containerId]).catch(() => {});
      return interaction.editReply({ content: '❌ Creation failed. Please try again.' });
    } catch (err) {
      return interaction.editReply({ content: `❌ Error: ${err.message}` });
    }
  }

  if (interaction.commandName === 'regen-ssh') {
    await interaction.deferReply({ ephemeral: true });
    const input = interaction.options.getString('container_name');
    const owned = await vpsManager.resolveContainerForUser(interaction.user.id, input);
    if (!owned) return interaction.editReply({ content: '❌ Instance not found.' });
    try {
      const line = await captureLine(['exec', owned.container_id, 'tmate', '-F'], 'ssh session:');
      if (line) {
        const sshSession = line.split('ssh session:')[1].trim();
        await interaction.user.send(`**New SSH:** \`\`\`${sshSession}\`\`\``).catch(() => {});
        return interaction.editReply({ content: '✅ SSH regenerated. Check your DMs.' });
      }
      return interaction.editReply({ content: '❌ Failed to generate SSH.' });
    } catch (err) {
      return interaction.editReply({ content: `❌ Error: ${err.message}` });
    }
  }

  if (interaction.commandName === 'earncredit') {
    const cuttlyKey = process.env.CUTTLY_API_KEY;
    if (!cuttlyKey) return interaction.reply({ content: '❌ CUTTLY_API_KEY not configured.', ephemeral: true });
    try {
      const apiUrl = `https://cutt.ly/api/api.php?key=${cuttlyKey}&short=https://cuty.io/e58WUzLMmE3S`;
      const response = await require('axios').get(apiUrl, { timeout: 10000 }).then((r) => r.data);
      if (response.url && response.url.status === 7) {
        await addCredits(interaction.user.id, 1);
        return interaction.reply({ content: `Success! Shortened URL: ${response.url.shortLink}. You earned 1 credit!`, ephemeral: true });
      }
      return interaction.reply({ content: response.url && response.url.title ? response.url.title : 'Failed to generate URL', ephemeral: true });
    } catch (err) {
      return interaction.reply({ content: 'Failed to earn credit. Please try again.', ephemeral: true });
    }
  }

  if (interaction.commandName === 'bal') {
    const credits = await getCredits(interaction.user.id);
    return interaction.reply({ content: `You have ${credits} credits.`, ephemeral: true });
  }

  if (interaction.commandName === 'renew') {
    const vpsInput = interaction.options.getString('vps_id');
    const credits = await getCredits(interaction.user.id);
    if (credits < 2) return interaction.reply({ content: '❌ You need 2 credits to renew.', ephemeral: true });
    const owned = await vpsManager.resolveContainerForUser(interaction.user.id, vpsInput);
    if (!owned) return interaction.reply({ content: `❌ VPS ${vpsInput} not found.`, ephemeral: true });
    const remaining = await spendCredits(interaction.user.id, 2);
    const renewalDate = new Date(Date.now() + 8 * 24 * 60 * 60 * 1000);
    await query(
      `INSERT INTO user_credits (user_id, renewals) VALUES ($1, $2::jsonb)
       ON CONFLICT (user_id) DO UPDATE SET renewals = user_credits.renewals || $2::jsonb, updated_at = NOW()`,
      [interaction.user.id, JSON.stringify({ [vpsInput]: renewalDate.toISOString() })]
    ).catch(() => {});
    return interaction.reply({
      content: `✅ VPS renewed for 8 days until ${renewalDate.toISOString().slice(0, 10)}. Remaining: ${remaining} credits`,
      ephemeral: true,
    });
  }

  if (interaction.commandName === 'port-add') {
    const containerName = interaction.options.getString('container_name');
    const containerPort = interaction.options.getInteger('container_port');
    const safe = /^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,127}$/.test(containerName);
    if (!safe) return interaction.reply({ content: 'Invalid container name.', ephemeral: true });
    const publicPort = Math.floor(Math.random() * (65535 - 1025 + 1)) + 1025;
    await interaction.deferReply({ ephemeral: true });
    try {
      await execFile('docker', ['exec', containerName, 'ssh', '-o', 'StrictHostKeyChecking=no', '-R', `${publicPort}:localhost:${containerPort}`, 'serveo.net', '-N', '-f'], { timeout: 15000 });
      return interaction.editReply({ content: `✅ Port forwarding: ${PUBLIC_IP}:${publicPort}` });
    } catch (err) {
      return interaction.editReply({ content: '❌ Error setting up port forwarding.' });
    }
  }

  if (interaction.commandName === 'port-http') {
    const containerName = interaction.options.getString('container_name');
    const containerPort = interaction.options.getInteger('container_port');
    await interaction.deferReply({ ephemeral: true });
    const urlLine = await captureLine(['exec', containerName, 'ssh', '-o', 'StrictHostKeyChecking=no', '-R', `80:localhost:${containerPort}`, 'serveo.net'], 'Forwarding HTTP traffic from', 45000);
    if (urlLine) {
      const url = urlLine.trim().split(/\s+/).pop();
      return interaction.editReply({ content: `✅ Website available at: ${url}` });
    }
    return interaction.editReply({ content: '❌ Failed to get forwarding URL.' });
  }

  return null;
}

module.exports = { toSpec, isParsed, handle, ensureTable };