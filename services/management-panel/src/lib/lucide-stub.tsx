/**
 * Minimal stub for lucide-react to keep the Vite build green when the
 * real package is not present in the lockfile. Each icon is a dummy
 * span so the UI still renders and the import does not crash Rollup.
 * Real lucide-react can be re-added later without changing consumers.
 */
import React from 'react';

const DummyIcon = (props: any) => React.createElement('span', { ...props, 'data-lucide-stub': true }, '·');

export const X = DummyIcon;
export const Filter = DummyIcon;
export const Download = DummyIcon;
export const Clock = DummyIcon;
export const User = DummyIcon;
export const AlertTriangle = DummyIcon;
export const Info = DummyIcon;
export const AlertCircle = DummyIcon;
export const Users = DummyIcon;
export const Share2 = DummyIcon;
export const MessageSquare = DummyIcon;
export const Search = DummyIcon;
export const FileText = DummyIcon;
export const Server = DummyIcon;
export const Archive = DummyIcon;
export const Save = DummyIcon;
export const Eye = DummyIcon;
export const Edit3 = DummyIcon;
export const Plus = DummyIcon;
export const Trash2 = DummyIcon;
export const Tag = DummyIcon;
export const ArrowLeft = DummyIcon;
export const Globe = DummyIcon;
export const ChevronRight = DummyIcon;
export const FolderOpen = DummyIcon;
export const Folder = DummyIcon;
export const Terminal = DummyIcon;
export const Maximize2 = DummyIcon;
export const Minimize2 = DummyIcon;
export const TerminalIcon = DummyIcon;

// Fallback for any other named import via Proxy (ESM named imports are static,
// but this helps if a file does `import * as Icons from 'lucide-react'`).
const handler: ProxyHandler<any> = {
  get(_target, prop) {
    if (prop in _target) return _target[prop];
    return DummyIcon;
  },
};

export default new Proxy(
  {
    X,
    Filter,
    Download,
    Clock,
    User,
    AlertTriangle,
    Info,
    AlertCircle,
    Users,
    Share2,
    MessageSquare,
    Search,
    FileText,
    Server,
    Archive,
    Save,
    Eye,
    Edit3,
    Plus,
    Trash2,
    Tag,
    ArrowLeft,
    Globe,
    ChevronRight,
    FolderOpen,
    Folder,
    Terminal,
    Maximize2,
    Minimize2,
  },
  handler,
);
