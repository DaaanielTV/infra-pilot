/**
 * CLI Bridge for Discord Bot
 *
 * Replaces direct Pterodactyl API calls with `ipilot` CLI subprocess calls.
 *
 * Usage:
 *   const { cli } = require('./cli-bridge');
 *   const result = await cli('server list');
 *   if (result.success) {
 *     const servers = result.data;
 *   }
 */

const { execSync } = require('child_process');

const IPILOT_CMD = process.env.IPILOT_CMD || 'ipilot';

/**
 * Execute an ipilot CLI command and return parsed JSON.
 */
function cli(command) {
  try {
    const fullCmd = `${IPILOT_CMD} ${command} --output json`;
    const stdout = execSync(fullCmd, {
      encoding: 'utf-8',
      timeout: 30000,
      windowsHide: true,
    });
    const data = JSON.parse(stdout.trim());
    return { success: true, data };
  } catch (err) {
    if (err.stdout) {
      try {
        return { success: true, data: JSON.parse(err.stdout.toString().trim()) };
      } catch (_) {}
    }
    return {
      success: false,
      data: null,
      error: err.stderr?.toString() || err.message || String(err),
    };
  }
}

/**
 * Convenience wrappers for Discord bot operations.
 */
const ipilot = {
  server: {
    list: () => cli('server list'),
    create: (name, type, memory) =>
      cli(`server create "${name}" --type "${type}"${memory ? ` --memory ${memory}` : ''}`),
    delete: (serverId) => cli(`server delete "${serverId}"`),
    status: (serverId) => cli(`server status "${serverId}"`),
  },
  backup: {
    list: (serverId) => cli(`backup list${serverId ? ` "${serverId}"` : ''}`),
    create: (serverId) => cli(`backup create "${serverId}"`),
  },
  health: {
    check: () => cli('health'),
  },
  energy: {
    current: () => cli('energy current'),
    summary: (period) => cli(`energy summary --period ${period || 'daily'}`),
  },
};

module.exports = { cli, ipilot };
