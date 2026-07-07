/**
 * CLI Bridge - Web Dashboard calls `ipilot` CLI commands internally.
 *
 * Instead of duplicating business logic in Express routes, these helpers
 * invoke the CLI via subprocess and return parsed JSON results.
 *
 * Usage:
 *   import { cli } from './cli-bridge.js';
 *   const servers = await cli('server list --output json');
 */

import { execSync } from 'child_process';

const IPILOT_CMD = process.env.IPILOT_CMD || 'ipilot';

export interface CliResult {
  success: boolean;
  data: any;
  error?: string;
}

/**
 * Execute an ipilot CLI command and return parsed JSON.
 * The command string should NOT include --output json (it's added automatically).
 */
export function cli(command: string): CliResult {
  try {
    const fullCmd = `${IPILOT_CMD} ${command} --output json`;
    const stdout = execSync(fullCmd, {
      encoding: 'utf-8',
      timeout: 30000,
      windowsHide: true,
    });
    return { success: true, data: JSON.parse(stdout.trim()) };
  } catch (err: any) {
    const message = err.stderr?.toString() || err.message || String(err);
    // Try to parse stdout if available
    if (err.stdout) {
      try {
        return { success: true, data: JSON.parse(err.stdout.toString().trim()) };
      } catch {
        // ignore parse error, fall through to error
      }
    }
    return { success: false, data: null, error: message };
  }
}

/**
 * Convenience wrappers for common operations.
 */
export const ipilot = {
  server: {
    list: () => cli('server list'),
    create: (name: string, type: string, memory?: number) =>
      cli(`server create "${name}" --type "${type}"${memory ? ` --memory ${memory}` : ''}`),
    delete: (serverId: string) => cli(`server delete "${serverId}"`),
    status: (serverId: string) => cli(`server status "${serverId}"`),
  },
  backup: {
    list: (serverId?: string) => cli(`backup list${serverId ? ` "${serverId}"` : ''}`),
    create: (serverId: string) => cli(`backup create "${serverId}"`),
  },
  logs: {
    fetch: (serverId: string, lines?: number) =>
      cli(`logs fetch "${serverId}"${lines ? ` --lines ${lines}` : ''}`),
  },
  edge: {
    list: () => cli('edge list'),
    register: (name: string, type: string, hardwareId: string) =>
      cli(`edge register "${name}" "${type}" "${hardwareId}"`),
    status: (deviceId: string) => cli(`edge status "${deviceId}"`),
  },
  health: {
    check: () => cli('health'),
  },
  config: {
    get: (key?: string) => cli(`config get${key ? ` ${key}` : ''}`),
    set: (key: string, value: string) => cli(`config set ${key} "${value}"`),
  },
};
