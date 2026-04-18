package com.playerservers;

import net.md_5.bungee.config.Configuration;

import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.TimeUnit;
import java.util.logging.Level;

public class ServerManager {
    private final PlayerServerManager plugin;
    private final Map<Integer, Process> runningProcesses;
    private final String serverJar;
    private final String serverHost;
    private final String templateDir;
    private final String serversDir;
    private final int memoryMB;
    
    public ServerManager(PlayerServerManager plugin) {
        this.plugin = plugin;
        this.runningProcesses = new HashMap<>();
        
        Configuration config = plugin.getConfig();
        this.serverJar = config.getString("server.jar_file", "paper.jar");
        this.serverHost = config.getString("server.host", "localhost");
        this.templateDir = config.getString("server.template_dir", plugin.getDataFolder() + File.separator + "template");
        this.serversDir = config.getString("server.servers_dir", plugin.getDataFolder() + File.separator + "servers");
        this.memoryMB = config.getInt("server.memory_mb", 1024);
        
        // Create directories if they don't exist
        new File(templateDir).mkdirs();
        new File(serversDir).mkdirs();
    }
    
    public boolean createServer(PlayerServer server) {
        String serverDir = getServerDirectory(server);
        
        // Create server directory
        File serverDirFile = new File(serverDir);
        if (!serverDirFile.exists()) {
            serverDirFile.mkdirs();
        }
        
        // Copy template files
        try {
            File templateDirFile = new File(templateDir);
            if (templateDirFile.exists() && templateDirFile.isDirectory()) {
                copyDirectory(Paths.get(templateDir), Paths.get(serverDir));
            }
            
            // Copy server jar if it doesn't exist in template
            File serverJarFile = new File(serverDir, serverJar);
            if (!serverJarFile.exists()) {
                File sourceJarFile = new File(plugin.getDataFolder(), serverJar);
                if (sourceJarFile.exists()) {
                    Files.copy(sourceJarFile.toPath(), serverJarFile.toPath(), StandardCopyOption.REPLACE_EXISTING);
                } else {
                    plugin.getLogger().warning("Server JAR file not found: " + sourceJarFile.getAbsolutePath());
                    return false;
                }
            }
            
            // Generate server.properties
            generateServerProperties(server);
            
            // Generate bukkit.yml and spigot.yml (if needed)
            generateBukkitConfig(server);
            
            // Add server to BungeeCord config (if needed)
            configureBungeeConfig(server);
            
            return true;
        } catch (IOException e) {
            plugin.getLogger().log(Level.SEVERE, "Failed to create server files for " + server.getServerName(), e);
            return false;
        }
    }
    
    public boolean startServer(PlayerServer server) {
        // Check if already running
        if (server.isRunning() || runningProcesses.containsKey(server.getId())) {
            return true;
        }
        
        String serverDir = getServerDirectory(server);
        File workingDir = new File(serverDir);
        
        if (!workingDir.exists() || !workingDir.isDirectory()) {
            plugin.getLogger().warning("Server directory not found: " + serverDir);
            return false;
        }
        
        // Build process command
        ProcessBuilder pb = new ProcessBuilder(
                "java",
                "-Xmx" + memoryMB + "M",
                "-Xms" + (memoryMB / 2) + "M",
                "-jar",
                serverJar,
                "--nogui",
                "--port", String.valueOf(server.getPort())
        );
        
        pb.directory(workingDir);
        pb.redirectErrorStream(true);
        
        try {
            // Start the process
            Process process = pb.start();
            runningProcesses.put(server.getId(), process);
            server.setRunning(true);
            
            // Log output for debugging
            final BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            plugin.getProxy().getScheduler().runAsync(plugin, () -> {
                try {
                    String line;
                    while ((line = reader.readLine()) != null) {
                        if (plugin.getConfig().getBoolean("server.debug_logging", false)) {
                            plugin.getLogger().info("[" + server.getServerName() + "] " + line);
                        }
                    }
                } catch (IOException e) {
                    if (server.isRunning()) {
                        plugin.getLogger().log(Level.SEVERE, "Error reading server process output for " + server.getServerName(), e);
                    }
                }
            });
            
            // Handle process termination
            plugin.getProxy().getScheduler().runAsync(plugin, () -> {
                try {
                    int exitCode = process.waitFor();
                    plugin.getLogger().info("Server " + server.getServerName() + " terminated with exit code " + exitCode);
                    
                    // Clean up
                    runningProcesses.remove(server.getId());
                    server.setRunning(false);
                } catch (InterruptedException e) {
                    plugin.getLogger().log(Level.SEVERE, "Error monitoring server process for " + server.getServerName(), e);
                }
            });
            
            // Wait for server to start up
            plugin.getLogger().info("Starting server " + server.getServerName() + " on port " + server.getPort());
            
            // Wait for server to be ready (in a real implementation, we would check if the server is ready to accept connections)
            try {
                TimeUnit.SECONDS.sleep(10);
            } catch (InterruptedException e) {
                plugin.getLogger().log(Level.WARNING, "Interrupted while waiting for server to start", e);
            }
            
            return true;
        } catch (IOException e) {
            plugin.getLogger().log(Level.SEVERE, "Failed to start server process for " + server.getServerName(), e);
            return false;
        }
    }
    
    public boolean stopServer(PlayerServer server) {
        if (!server.isRunning() || !runningProcesses.containsKey(server.getId())) {
            server.setRunning(false);
            return true;
        }
        
        Process process = runningProcesses.get(server.getId());
        if (process != null) {
            // Try to stop gracefully first
            process.destroy();
            
            // Wait for the process to terminate
            try {
                if (!process.waitFor(30, TimeUnit.SECONDS)) {
                    // Force kill if it doesn't terminate
                    process.destroyForcibly();
                }
            } catch (InterruptedException e) {
                plugin.getLogger().log(Level.WARNING, "Interrupted while waiting for server to stop", e);
                // Force kill
                process.destroyForcibly();
            }
            
            runningProcesses.remove(server.getId());
        }
        
        server.setRunning(false);
        return true;
    }
    
    public boolean deleteServer(PlayerServer server) {
        // Stop the server if it's running
        if (server.isRunning()) {
            stopServer(server);
        }
        
        // Delete server files
        String serverDir = getServerDirectory(server);
        File serverDirFile = new File(serverDir);
        
        if (serverDirFile.exists() && serverDirFile.isDirectory()) {
            try {
                deleteDirectory(serverDirFile);
                return true;
            } catch (IOException e) {
                plugin.getLogger().log(Level.SEVERE, "Failed to delete server directory for " + server.getServerName(), e);
                return false;
            }
        }
        
        return true;
    }
    
    public boolean installPlugin(PlayerServer server, String pluginName) {
        if (!server.isRunning()) {
            return false;
        }
        
        // Check if plugin is in the allowed list
        Configuration config = plugin.getConfig();
        if (!config.getStringList("server.allowed_plugins").contains(pluginName)) {
            return false;
        }
        
        // Copy plugin jar from plugins directory to server's plugins directory
        String serverDir = getServerDirectory(server);
        File pluginsDir = new File(serverDir, "plugins");
        if (!pluginsDir.exists()) {
            pluginsDir.mkdirs();
        }
        
        File sourcePluginFile = new File(plugin.getDataFolder(), "plugins" + File.separator + pluginName + ".jar");
        File targetPluginFile = new File(pluginsDir, pluginName + ".jar");
        
        try {
            Files.copy(sourcePluginFile.toPath(), targetPluginFile.toPath(), StandardCopyOption.REPLACE_EXISTING);
            
            // Add to database
            try (Connection conn = plugin.getDbConnection();
                 PreparedStatement stmt = conn.prepareStatement("INSERT INTO server_plugins (server_id, plugin_name) VALUES (?, ?)")) {
                stmt.setInt(1, server.getId());
                stmt.setString(2, pluginName);
                stmt.executeUpdate();
            } catch (SQLException e) {
                plugin.getLogger().log(Level.SEVERE, "Failed to update database for plugin installation", e);
            }
            
            // Add to server object
            server.addPlugin(pluginName);
            
            return true;
        } catch (IOException e) {
            plugin.getLogger().log(Level.SEVERE, "Failed to install plugin " + pluginName + " for server " + server.getServerName(), e);
            return false;
        }
    }
    
    public boolean uninstallPlugin(PlayerServer server, String pluginName) {
        if (!server.hasPlugin(pluginName)) {
            return false;
        }
        
        // Delete plugin jar
        String serverDir = getServerDirectory(server);
        File pluginFile = new File(serverDir, "plugins" + File.separator + pluginName + ".jar");
        
        if (pluginFile.exists()) {
            pluginFile.delete();
        }
        
        // Remove from database
        try (Connection conn = plugin.getDbConnection();
             PreparedStatement stmt = conn.prepareStatement("DELETE FROM server_plugins WHERE server_id = ? AND plugin_name = ?")) {
            stmt.setInt(1, server.getId());
            stmt.setString(2, pluginName);
            stmt.executeUpdate();
        } catch (SQLException e) {
            plugin.getLogger().log(Level.SEVERE, "Failed to update database for plugin uninstallation", e);
        }
        
        // Remove from server object
        server.removePlugin(pluginName);
        
        return true;
    }
    
    public boolean updateServerSetting(PlayerServer server, String key, String value) {
        // Update server.properties if needed
        if (key.equals("max_players") || key.equals("motd") || key.equals("gamemode") || 
            key.equals("difficulty") || key.equals("whitelist")) {
            
            String serverDir = getServerDirectory(server);
            File propertiesFile = new File(serverDir, "server.properties");
            
            // In a real implementation, we would update the specific property in the file
            // For now, we'll just regenerate the entire file
            generateServerProperties(server);
        }
        
        // Update database
        try (Connection conn = plugin.getDbConnection();
             PreparedStatement stmt = conn.prepareStatement(
                     "INSERT OR REPLACE INTO server_settings (server_id, setting_key, setting_value) VALUES (?, ?, ?)")) {
            stmt.setInt(1, server.getId());
            stmt.setString(2, key);
            stmt.setString(3, value);
            stmt.executeUpdate();
        } catch (SQLException e) {
            plugin.getLogger().log(Level.SEVERE, "Failed to update database for server setting", e);
            return false;
        }
        
        // Update server object
        server.setSetting(key, value);
        
        return true;
    }
    
    private String getServerDirectory(PlayerServer server) {
        return serversDir + File.separator + server.getServerName();
    }
    
    private void generateServerProperties(PlayerServer server) {
        String serverDir = getServerDirectory(server);
        File propertiesFile = new File(serverDir, "server.properties");
        
        Map<String, String> properties = new HashMap<>();
        properties.put("server-port", String.valueOf(server.getPort()));
        properties.put("server-ip", serverHost);
        properties.put("max-players", server.getSetting("max_players"));
        properties.put("motd", server.getSetting("motd"));
        properties.put("gamemode", server.getSetting("gamemode"));
        properties.put("difficulty", server.getSetting("difficulty"));
        properties.put("white-list", server.getSetting("whitelist"));
        properties.put("spawn-protection", "0");
        properties.put("online-mode", "false"); // Required for BungeeCord
        properties.put("enable-command-block", "false");
        
        StringBuilder sb = new StringBuilder();
        sb.append("# Minecraft server properties\n");
        sb.append("# Generated by PlayerServerManager\n");
        for (Map.Entry<String, String> entry : properties.entrySet()) {
            sb.append(entry.getKey()).append("=").append(entry.getValue()).append("\n");
        }
        
        try {
            Files.write(propertiesFile.toPath(), sb.toString().getBytes());
        } catch (IOException e) {
            plugin.getLogger().log(Level.SEVERE, "Failed to write server.properties for server " + server.getServerName(), e);
        }
    }
    
    private void generateBukkitConfig(PlayerServer server) {
        String serverDir = getServerDirectory(server);
        
        // bukkit.yml
        File bukkitFile = new File(serverDir, "bukkit.yml");
        if (!bukkitFile.exists()) {
            try {
                StringBuilder sb = new StringBuilder();
                sb.append("settings:\n");
                sb.append("  allow-end: true\n");
                sb.append("  connection-throttle: 4000\n");
                sb.append("  query-plugins: false\n");
                sb.append("  permissions-file: permissions.yml\n");
                sb.append("  use-exact-login-location: false\n");
                sb.append("  ping-packet-limit: 100\n");
                sb.append("  bungeecord: true\n"); // Required for BungeeCord
                
                Files.write(bukkitFile.toPath(), sb.toString().getBytes());
            } catch (IOException e) {
                plugin.getLogger().log(Level.SEVERE, "Failed to write bukkit.yml for server " + server.getServerName(), e);
            }
        }
        
        // spigot.yml
        File spigotFile = new File(serverDir, "spigot.yml");
        if (!spigotFile.exists()) {
            try {
                StringBuilder sb = new StringBuilder();
                sb.append("settings:\n");
                sb.append("  bungeecord: true\n"); // Required for BungeeCord
                sb.append("  restart-on-crash: false\n");
                sb.append("  sample-count: 12\n");
                
                Files.write(spigotFile.toPath(), sb.toString().getBytes());
            } catch (IOException e) {
                plugin.getLogger().log(Level.SEVERE, "Failed to write spigot.yml for server " + server.getServerName(), e);
            }
        }
    }
    
    private void configureBungeeConfig(PlayerServer server) {
        // In a real implementation, we would update the BungeeCord config.yml
        // However, since we're registering servers dynamically in the plugin,
        // we don't need to modify the config file
    }
    
    private void copyDirectory(Path source, Path target) throws IOException {
        if (!Files.exists(target)) {
            Files.createDirectories(target);
        }
        
        Files.walk(source).forEach(sourcePath -> {
            try {
                Path targetPath = target.resolve(source.relativize(sourcePath));
                if (Files.isDirectory(sourcePath)) {
                    if (!Files.exists(targetPath)) {
                        Files.createDirectories(targetPath);
                    }
                } else {
                    Files.copy(sourcePath, targetPath, StandardCopyOption.REPLACE_EXISTING);
                }
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        });
    }
    
    private void deleteDirectory(File directory) throws IOException {
        if (!directory.exists()) {
            return;
        }
        
        File[] files = directory.listFiles();
        if (files != null) {
            for (File file : files) {
                if (file.isDirectory()) {
                    deleteDirectory(file);
                } else {
                    file.delete();
                }
            }
        }
        
        directory.delete();
    }
}
