/**
 * @file Vite configuration for the management-panel frontend.
 * Supports both web-only mode and Tauri desktop builds.
 */

import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import path from "path";

const host = process.env.TAURI_DEV_HOST;

export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
      // Fallback stub for lucide-react when the real package is not in the lockfile.
      // This keeps `vite build` green on CI without requiring a lockfile bump.
      // Remove once lucide-react is properly added to dependencies.
      "lucide-react": path.resolve(__dirname, "./src/lib/lucide-stub.tsx"),
    },
  },
  clearScreen: false,
  server: {
    port: 5173,
    strictPort: true,
    host: host || false,
    hmr: host ? { protocol: "ws", host, port: 5174 } : undefined,
    watch: {
      ignored: ["**/src-tauri/**"],
    },
  },
  envPrefix: ["VITE_", "TAURI_"],
  build: {
    target: process.env.TAURI_ENV_PLATFORM === "windows" ? "chrome105" : "safari13",
    minify: false,
    sourcemap: !!process.env.TAURI_ENV_DEBUG,
  },
});
