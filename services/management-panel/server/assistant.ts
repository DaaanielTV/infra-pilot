/**
 * @file Assistant: real execution of infrastructure intents.
 * Parses a natural-language request into a plan, resolves it against real
 * data (docker_apps, deployments) and reports which tools will run.
 * Actual tool execution happens in the route handlers that call the same
 * helpers used by the rest of the API (dockerAction, runBenchmark, ...).
 */

export type AssistantTool =
  | 'start'
  | 'stop'
  | 'restart'
  | 'status'
  | 'logs'
  | 'benchmark'
  | 'deploy';

export interface AssistantAction {
  tool: AssistantTool;
  appId?: string;
  target?: string;
  reason: string;
}

export interface AssistantPlan {
  intent: string;
  requires_approval: boolean;
  actions: AssistantAction[];
  message: string;
}

const TOOL_ALIASES: Record<AssistantTool, string[]> = {
  start: ['start', 'launch', 'boot', 'turn on', 'auf', 'starten', 'hochfahren'],
  stop: ['stop', 'halt', 'shut down', 'kill', 'aus', 'stoppen', 'stopp'],
  restart: ['restart', 'reboot', 'reload', 'neustart', 'neu starten', 'restarten'],
  status: ['status', 'state', 'health', 'läuft', 'running', 'up?', 'funktioniert'],
  logs: ['log', 'logs', 'ausgabe', 'console'],
  benchmark: ['benchmark', 'bench', 'performance', 'messung', 'benchmarken'],
  deploy: ['deploy', 'deployment', 'release', 'installieren', 'deployen'],
};

function normalize(text: string): string {
  return text.toLowerCase().replace(/[.,!?;:]/g, ' ').replace(/\s+/g, ' ').trim();
}

function findTool(text: string): AssistantTool | null {
  const matches: { tool: AssistantTool; index: number }[] = [];
  for (const [tool, aliases] of Object.entries(TOOL_ALIASES)) {
    for (const alias of aliases as string[]) {
      const index = text.indexOf(alias);
      if (index >= 0) {
        matches.push({ tool: tool as AssistantTool, index });
      }
    }
  }
  if (matches.length === 0) return null;
  matches.sort((a, b) => a.index - b.index);
  return matches[0].tool;
}

/** Find a likely app id/name in the text, or the first part that looks like one. */
function findTarget(text: string): string | undefined {
  const idMatch = text.match(/\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b/);
  if (idMatch) return idMatch[0];
  const quoted = text.match(/"([^"]+)"/) || text.match(/'([^']+)'/);
  if (quoted) return quoted[1];
  return undefined;
}

/**
 * Build an execution plan from a request. Pure and unit-testable.
 * The `apps` list comes from the caller (real data).
 */
export function buildPlan(
  request: string,
  apps: { id: string; name: string }[],
): AssistantPlan {
  const text = normalize(request);
  const tool = findTool(text) || 'status';
  const target = findTarget(text);
  const app = target
    ? apps.find((a) => a.id === target || a.name.toLowerCase() === target.toLowerCase())
    : undefined;
  const appId = app ? app.id : target;
  const unknownTarget = target && !app && !/^[0-9a-f-]{36}$/.test(target);

  if (unknownTarget) {
    return {
      intent: tool,
      requires_approval: false,
      actions: [],
      message: `I couldn't find an app named "${target}". I searched your registered apps.`,
    };
  }
  if (!app && target && /^[0-9a-f-]{36}$/.test(target)) {
    return {
      intent: tool,
      requires_approval: true,
      actions: [{ tool, appId, reason: `Run "${tool}" on app ${appId}` }],
      message: `I found an app by id ${appId}. ${tool} will be executed with your approval.`,
    };
  }

  const label = app ? `"${app.name}"` : (target || 'the system');
  if (tool === 'benchmark' && !app) {
    return {
      intent: 'benchmark',
      requires_approval: true,
      actions: [{ tool: 'benchmark', reason: 'Run a local performance benchmark (10s)' }],
      message: `I can run a local benchmark. It measures CPU, memory and disk for 10 seconds. Approve to continue.`,
    };
  }

  return {
    intent: tool,
    requires_approval: tool !== 'status' && tool !== 'logs',
    actions: [{ tool, appId, reason: `${tool} on ${label}` }],
    message: `Plan: ${tool} on ${label}.`,
  };
}

export { TOOL_ALIASES };