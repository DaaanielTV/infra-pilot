const cron = require('node-cron');
const { EmbedBuilder } = require('discord.js');
const { query } = require('./db');
const { exec } = require('./docker');

const CHECK_TYPES = ['ping', 'port', 'process', 'api'];
const DEFAULT_PING_TARGET = '8.8.8.8';
const DEFAULT_PORT_CHECK = 'localhost:22';
const DEFAULT_PROCESS = 'sshd';
const DEFAULT_HEALTH_URL = 'http://localhost:80/health';
const INTERVAL_SECONDS = parseInt(process.env.HEALTH_CHECK_INTERVAL_SECONDS, 10) || 60;

let clientRef = null;
let loopTask = null;

function init(client) {
  clientRef = client;
  if (loopTask) return;
  loopTask = cron.schedule(`*/${Math.max(10, INTERVAL_SECONDS)} * * * * *`, () => {
    runLoop().catch((err) => console.error('[HealthChecks] loop error:', err));
  });
}

function stop() {
  if (loopTask) { loopTask.stop(); loopTask = null; }
}

async function runLoop() {
  const result = await query('SELECT * FROM health_checks').catch(() => null);
  if (!result) return;
  for (const check of result.rows) {
    const r = await runHealthCheck(check.container_id, check.check_type, check.target);
    await updateCheckStatus(check.id, r.status);
    if (r.status === 'failed') await notifyFailure(check, r);
  }
}

async function runHealthCheck(containerId, checkType, target = null) {
  const result = { status: 'unknown', response_time_ms: 0, error: null };
  const start = Date.now();
  try {
    if (checkType === 'ping') {
      const pingTarget = target || DEFAULT_PING_TARGET;
      const ok = await exec(containerId, `ping -c 1 -W 2 ${pingTarget}`).then(() => true).catch(() => false);
      result.status = ok ? 'passed' : 'failed';
    } else if (checkType === 'port') {
      const [host, port] = (target || DEFAULT_PORT_CHECK).split(':');
      const ok = await exec(containerId, `timeout 2 bash -c 'echo >/dev/tcp/${host}/${port}' 2>/dev/null`)
        .then(() => true)
        .catch(() => false);
      result.status = ok ? 'passed' : 'failed';
    } else if (checkType === 'process') {
      const process = target || DEFAULT_PROCESS;
      const ok = await exec(containerId, `pgrep -x ${process}`).then(() => true).catch(() => false);
      result.status = ok ? 'passed' : 'failed';
    } else if (checkType === 'api') {
      const url = target || DEFAULT_HEALTH_URL;
      const out = await exec(containerId, `curl -s -o /dev/null -w '%{http_code}' ${url}`)
        .catch(() => '');
      result.status = ['200', '201', '204'].includes(out.trim()) ? 'passed' : 'failed';
    } else {
      result.status = 'unknown';
      result.error = `Unknown check type: ${checkType}`;
    }
  } catch (err) {
    result.status = 'failed';
    result.error = err.message;
  }
  result.response_time_ms = Date.now() - start;
  await recordResult(containerId, checkType, result);
  return result;
}

async function updateCheckStatus(checkId, status) {
  await query(
    'UPDATE health_checks SET last_check = NOW(), last_status = $2 WHERE id = $1',
    [checkId, status]
  ).catch((err) => console.error('[HealthChecks] status update failed:', err.message));
}

async function recordResult(containerId, checkType, result) {
  await query(
    `INSERT INTO health_check_results
     (check_id, status, response_time_ms, error_message, checked_at)
     VALUES (
       (SELECT id FROM health_checks WHERE container_id = $1 AND check_type = $2 LIMIT 1),
       $3, $4, $5, NOW()
     )`,
    [containerId, checkType, result.status, result.response_time_ms, result.error]
  ).catch(() => {});
}

async function notifyFailure(check, result) {
  try {
    const owner = await query(
      'SELECT user_id FROM vps_containers WHERE container_id = $1',
      [check.container_id]
    );
    if (!owner.rows.length) return;
    const user = await clientRef.users.fetch(owner.rows[0].user_id).catch(() => null);
    if (!user) return;
    const embed = new EmbedBuilder()
      .setTitle('Health Check Failed')
      .setColor(0xff0000)
      .addFields(
        { name: 'Container', value: check.container_id.slice(0, 12), inline: true },
        { name: 'Check Type', value: check.check_type, inline: true },
        { name: 'Response', value: `${result.response_time_ms}ms`, inline: true },
        { name: 'Error', value: result.error || 'Unknown', inline: false }
      );
    await user.send({ embeds: [embed] });
  } catch (err) {
    console.error('[HealthChecks] failure notify error:', err.message);
  }
}

async function listForUser(userId) {
  try {
    const result = await query(
      `SELECT hc.* FROM health_checks hc
       JOIN vps_containers vc ON vc.container_id = hc.container_id
       WHERE vc.user_id = $1
       ORDER BY hc.created_at DESC`,
      [userId]
    );
    return result.rows;
  } catch (err) {
    console.error('[HealthChecks] list failed:', err.message);
    return [];
  }
}

const COMMAND_SPECS = [
  {
    name: 'health',
    description: 'Run health check on a VPS',
    options: [{ name: 'container_id', description: 'Container ID or name', type: 3, required: true }],
  },
  {
    name: 'healthcreate',
    description: 'Create a health check for a VPS',
    options: [
      { name: 'container_id', description: 'Container ID or name', type: 3, required: true },
      { name: 'check_type', description: 'ping/port/process/api', type: 3, required: true },
      { name: 'target', description: 'Target (host:port, process name, URL)', type: 3, required: false },
    ],
  },
  { name: 'healthlist', description: 'List active health checks', type: 1 },
];

function toSpec() {
  return COMMAND_SPECS;
}

function isParsed(name) {
  return COMMAND_SPECS.some((c) => c.name === name);
}

async function handle(interaction) {
  const { commandName, options } = interaction;
  if (commandName === 'health') {
    await interaction.deferReply({ ephemeral: true });
    const input = options.getString('container_id');
    const vpsManager = require('./vpsManager');
    const owned = await vpsManager.resolveContainerForUser(interaction.user.id, input);
    if (!owned) return interaction.editReply({ content: '❌ VPS not found for your account' });
    const embed = new EmbedBuilder()
      .setTitle(`Health Check: ${owned.container_id.slice(0, 12)}`)
      .setColor(0x3498db)
      .setTimestamp();
    for (const checkType of CHECK_TYPES) {
      const r = await runHealthCheck(owned.container_id, checkType);
      const emoji = r.status === 'passed' ? '✅' : '❌';
      embed.addFields({ name: checkType, value: `${emoji} ${r.status} (${r.response_time_ms}ms)`, inline: true });
    }
    return interaction.editReply({ embeds: [embed] });
  }
  if (commandName === 'healthcreate') {
    const input = options.getString('container_id');
    const checkType = options.getString('check_type').toLowerCase();
    const target = options.getString('target');
    const vpsManager = require('./vpsManager');
    const owned = await vpsManager.resolveContainerForUser(interaction.user.id, input);
    if (!owned) return interaction.reply({ content: '❌ VPS not found for your account', ephemeral: true });
    if (!CHECK_TYPES.includes(checkType)) {
      return interaction.reply({ content: `❌ Invalid type. Options: ${CHECK_TYPES.join(', ')}`, ephemeral: true });
    }
    try {
      await query(
        `INSERT INTO health_checks (container_id, check_type, target, interval_seconds)
         VALUES ($1, $2, $3, $4)`,
        [owned.container_id, checkType, target, INTERVAL_SECONDS]
      );
      return interaction.reply({
        content: `✅ Health check created: ${checkType} on \`${owned.container_id.slice(0, 12)}\``,
        ephemeral: true,
      });
    } catch (err) {
      return interaction.reply({ content: `❌ Error: ${err.message}`, ephemeral: true });
    }
  }
  if (commandName === 'healthlist') {
    const checks = await listForUser(interaction.user.id);
    if (!checks.length) {
      return interaction.reply({ content: 'No health checks configured.', ephemeral: true });
    }
    const embed = new EmbedBuilder().setTitle('Health Checks').setColor(0x3498db);
    for (const c of checks) {
      embed.addFields({
        name: `${c.check_type} - ${c.container_id.slice(0, 12)}`,
        value: `Status: ${c.last_status || 'pending'}\nTarget: ${c.target || 'N/A'}\nInterval: ${c.interval_seconds}s`,
        inline: false,
      });
    }
    return interaction.reply({ embeds: [embed], ephemeral: true });
  }
  return null;
}

module.exports = { init, stop, toSpec, isParsed, handle, runHealthCheck };