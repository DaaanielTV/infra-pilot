package com.playerservers;

import net.md_5.bungee.api.ChatColor;
import net.md_5.bungee.api.CommandSender;
import net.md_5.bungee.api.chat.ComponentBuilder;
import net.md_5.bungee.api.config.ServerInfo;
import net.md_5.bungee.api.connection.ProxiedPlayer;
import net.md_5.bungee.api.plugin.Command;
import net.md_5.bungee.api.plugin.Plugin;
import net.md_5.bungee.config.Configuration;
import net.md_5.bungee.config.ConfigurationProvider;
import net.md_5.bungee.config.YamlConfiguration;

import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.net.InetSocketAddress;
import java.nio.file.Files;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.HashMap;
import java.util.Map;
import java.util.UUID;
import java.util.concurrent.TimeUnit;
import java.util.logging.Level;

public class PlayerServerManager extends Plugin {
    private Configuration config;
    private Connection dbConnection;
    private Map<UUID, PlayerServer> playerServers = new HashMap<>();
    private ServerManager serverManager;
    private GuiManager guiManager;

    @Override
    public void onEnable() {
        // Initialize configuration
        loadConfig();
        
        // Initialize database connection
        initDatabase();
        
        // Initialize server manager
        serverManager = new ServerManager(this);
        
        // Initialize GUI manager
        guiManager = new GuiManager(this);
        
        // Register commands
        getProxy().getPluginManager().registerCommand(this, new ServerCommand(this));
        
        // Load existing servers from database
        loadExistingServers();
        
        // Start inactivity checker task
        getProxy().getScheduler().schedule(this, new InactivityChecker(), 1, 1, TimeUnit.MINUTES);
        
        getLogger().info("PlayerServerManager has been enabled!");
    }

    @Override
    public void onDisable() {
        // Save all servers state
        for (PlayerServer server : playerServers.values()) {
            if (server.isRunning()) {
                serverManager.stopServer(server);
            }
        }
        
        // Close database connection
        if (dbConnection != null) {
            try {
                dbConnection.close();
            } catch (SQLException e) {
                getLogger().log(Level.SEVERE, "Error closing database connection", e);
            }
        }
        
        getLogger().info("PlayerServerManager has been disabled!");
    }
    
    private void loadConfig() {
        try {
            if (!getDataFolder().exists()) {
                getDataFolder().mkdir();
            }
            
            File configFile = new File(getDataFolder(), "config.yml");
            
            if (!configFile.exists()) {
                try (InputStream in = getResourceAsStream("config.yml")) {
                    Files.copy(in, configFile.toPath());
                } catch (IOException e) {
                    getLogger().log(Level.SEVERE, "Could not create default config file", e);
                }
            }
            
            config = ConfigurationProvider.getProvider(YamlConfiguration.class).load(configFile);
        } catch (IOException e) {
            getLogger().log(Level.SEVERE, "Could not load config file", e);
        }
    }
    
    private void initDatabase() {
        try {
            String dbType = config.getString("database.type", "sqlite");
            
            if (dbType.equalsIgnoreCase("mysql")) {
                String host = config.getString("database.host", "localhost");
                int port = config.getInt("database.port", 3306);
                String database = config.getString("database.database", "playerservers");
                String username = config.getString("database.username", "root");
                String password = config.getString("database.password", "");
                
                String url = "jdbc:mysql://" + host + ":" + port + "/" + database;
                dbConnection = DriverManager.getConnection(url, username, password);
            } else {
                // SQLite
                File dbFile = new File(getDataFolder(), "playerservers.db");
                String url = "jdbc:sqlite:" + dbFile.getAbsolutePath();
                dbConnection = DriverManager.getConnection(url);
            }
            
            createTables();
            
        } catch (SQLException e) {
            getLogger().log(Level.SEVERE, "Failed to initialize database connection", e);
        }
    }
    
    private void createTables() throws SQLException {
        try (Statement stmt = dbConnection.createStatement()) {
            // Create servers table
            stmt.execute("CREATE TABLE IF NOT EXISTS servers (" +
                    "id INTEGER PRIMARY KEY " + (config.getString("database.type", "sqlite").equalsIgnoreCase("mysql") ? "AUTO_INCREMENT" : "AUTOINCREMENT") + ", " +
                    "player_uuid VARCHAR(36) NOT NULL UNIQUE, " +
                    "player_name VARCHAR(16) NOT NULL, " +
                    "server_name VARCHAR(32) NOT NULL, " +
                    "server_port INTEGER NOT NULL, " +
                    "created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, " +
                    "last_active TIMESTAMP DEFAULT CURRENT_TIMESTAMP)");
            
            // Create server_operators table
            stmt.execute("CREATE TABLE IF NOT EXISTS server_operators (" +
                    "server_id INTEGER NOT NULL, " +
                    "operator_uuid VARCHAR(36) NOT NULL, " +
                    "PRIMARY KEY (server_id, operator_uuid), " +
                    "FOREIGN KEY (server_id) REFERENCES servers(id) ON DELETE CASCADE)");
            
            // Create server_plugins table
            stmt.execute("CREATE TABLE IF NOT EXISTS server_plugins (" +
                    "server_id INTEGER NOT NULL, " +
                    "plugin_name VARCHAR(64) NOT NULL, " +
                    "PRIMARY KEY (server_id, plugin_name), " +
                    "FOREIGN KEY (server_id) REFERENCES servers(id) ON DELETE CASCADE)");
            
            // Create server_settings table
            stmt.execute("CREATE TABLE IF NOT EXISTS server_settings (" +
                    "server_id INTEGER NOT NULL, " +
                    "setting_key VARCHAR(64) NOT NULL, " +
                    "setting_value TEXT NOT NULL, " +
                    "PRIMARY KEY (server_id, setting_key), " +
                    "FOREIGN KEY (server_id) REFERENCES servers(id) ON DELETE CASCADE)");
        }
    }
    
    private void loadExistingServers() {
        try (PreparedStatement stmt = dbConnection.prepareStatement("SELECT * FROM servers");
             ResultSet rs = stmt.executeQuery()) {
            
            while (rs.next()) {
                int id = rs.getInt("id");
                UUID playerUuid = UUID.fromString(rs.getString("player_uuid"));
                String playerName = rs.getString("player_name");
                String serverName = rs.getString("server_name");
                int port = rs.getInt("server_port");
                
                PlayerServer server = new PlayerServer(id, playerUuid, playerName, serverName, port);
                
                // Load operators
                try (PreparedStatement opStmt = dbConnection.prepareStatement("SELECT operator_uuid FROM server_operators WHERE server_id = ?")) {
                    opStmt.setInt(1, id);
                    try (ResultSet opRs = opStmt.executeQuery()) {
                        while (opRs.next()) {
                            server.addOperator(UUID.fromString(opRs.getString("operator_uuid")));
                        }
                    }
                }
                
                // Load plugins
                try (PreparedStatement pluginStmt = dbConnection.prepareStatement("SELECT plugin_name FROM server_plugins WHERE server_id = ?")) {
                    pluginStmt.setInt(1, id);
                    try (ResultSet pluginRs = pluginStmt.executeQuery()) {
                        while (pluginRs.next()) {
                            server.addPlugin(pluginRs.getString("plugin_name"));
                        }
                    }
                }
                
                // Load settings
                try (PreparedStatement settingStmt = dbConnection.prepareStatement("SELECT setting_key, setting_value FROM server_settings WHERE server_id = ?")) {
                    settingStmt.setInt(1, id);
                    try (ResultSet settingRs = settingStmt.executeQuery()) {
                        while (settingRs.next()) {
                            server.setSetting(settingRs.getString("setting_key"), settingRs.getString("setting_value"));
                        }
                    }
                }
                
                playerServers.put(playerUuid, server);
                
                // Register server with BungeeCord if not already registered
                String serverAddress = config.getString("server.host", "localhost") + ":" + port;
                if (!getProxy().getServers().containsKey(serverName)) {
                    ServerInfo serverInfo = getProxy().constructServerInfo(
                            serverName,
                            new InetSocketAddress(config.getString("server.host", "localhost"), port),
                            serverName + " - Owned by " + playerName,
                            false
                    );
                    getProxy().getServers().put(serverName, serverInfo);
                }
            }
            
            getLogger().info("Loaded " + playerServers.size() + " player servers from database");
            
        } catch (SQLException e) {
            getLogger().log(Level.SEVERE, "Failed to load existing servers from database", e);
        }
    }
    
    public boolean createPlayerServer(ProxiedPlayer player) {
        UUID playerUuid = player.getUniqueId();
        
        // Check if player already has a server
        if (playerServers.containsKey(playerUuid)) {
            player.sendMessage(new ComponentBuilder("You already have a server! Use /server join to connect to it.").color(ChatColor.RED).create());
            return false;
        }
        
        // Find an available port
        int basePort = config.getInt("server.start_port", 25566);
        int maxPort = config.getInt("server.max_port", 26000);
        int port = findAvailablePort(basePort, maxPort);
        
        if (port == -1) {
            player.sendMessage(new ComponentBuilder("No available server ports! Please contact an administrator.").color(ChatColor.RED).create());
            return false;
        }
        
        String serverName = "p_" + player.getName().toLowerCase();
        
        // Create database entry
        try (PreparedStatement stmt = dbConnection.prepareStatement(
                "INSERT INTO servers (player_uuid, player_name, server_name, server_port) VALUES (?, ?, ?, ?)",
                Statement.RETURN_GENERATED_KEYS)) {
            
            stmt.setString(1, playerUuid.toString());
            stmt.setString(2, player.getName());
            stmt.setString(3, serverName);
            stmt.setInt(4, port);
            
            int affectedRows = stmt.executeUpdate();
            
            if (affectedRows == 0) {
                player.sendMessage(new ComponentBuilder("Failed to create server! Please try again later.").color(ChatColor.RED).create());
                return false;
            }
            
            int serverId;
            try (ResultSet generatedKeys = stmt.getGeneratedKeys()) {
                if (generatedKeys.next()) {
                    serverId = generatedKeys.getInt(1);
                } else {
                    player.sendMessage(new ComponentBuilder("Failed to create server! Please try again later.").color(ChatColor.RED).create());
                    return false;
                }
            }
            
            // Create PlayerServer object
            PlayerServer server = new PlayerServer(serverId, playerUuid, player.getName(), serverName, port);
            
            // Add owner as operator
            server.addOperator(playerUuid);
            try (PreparedStatement opStmt = dbConnection.prepareStatement(
                    "INSERT INTO server_operators (server_id, operator_uuid) VALUES (?, ?)")) {
                opStmt.setInt(1, serverId);
                opStmt.setString(2, playerUuid.toString());
                opStmt.executeUpdate();
            }
            
            // Set default settings
            Map<String, String> defaultSettings = new HashMap<>();
            defaultSettings.put("max_players", "20");
            defaultSettings.put("whitelist", "false");
            defaultSettings.put("motd", player.getName() + "'s Server");
            defaultSettings.put("gamemode", "survival");
            defaultSettings.put("difficulty", "normal");
            
            for (Map.Entry<String, String> entry : defaultSettings.entrySet()) {
                server.setSetting(entry.getKey(), entry.getValue());
                try (PreparedStatement settingStmt = dbConnection.prepareStatement(
                        "INSERT INTO server_settings (server_id, setting_key, setting_value) VALUES (?, ?, ?)")) {
                    settingStmt.setInt(1, serverId);
                    settingStmt.setString(2, entry.getKey());
                    settingStmt.setString(3, entry.getValue());
                    settingStmt.executeUpdate();
                }
            }
            
            playerServers.put(playerUuid, server);
            
            // Register server with BungeeCord
            ServerInfo serverInfo = getProxy().constructServerInfo(
                    serverName,
                    new InetSocketAddress(config.getString("server.host", "localhost"), port),
                    serverName + " - Owned by " + player.getName(),
                    false
            );
            getProxy().getServers().put(serverName, serverInfo);
            
            // Actually create and start the server
            boolean success = serverManager.createServer(server);
            if (!success) {
                // Clean up if server creation failed
                deletePlayerServer(player);
                player.sendMessage(new ComponentBuilder("Failed to create your server! Please contact an administrator.").color(ChatColor.RED).create());
                return false;
            }
            
            player.sendMessage(new ComponentBuilder("Your server has been created! Use /server join to connect to it.").color(ChatColor.GREEN).create());
            return true;
            
        } catch (SQLException e) {
            getLogger().log(Level.SEVERE, "Failed to create server for player " + player.getName(), e);
            player.sendMessage(new ComponentBuilder("Failed to create server! Please try again later.").color(ChatColor.RED).create());
            return false;
        }
    }
    
    public boolean deletePlayerServer(ProxiedPlayer player) {
        UUID playerUuid = player.getUniqueId();
        
        // Check if player has a server
        if (!playerServers.containsKey(playerUuid)) {
            player.sendMessage(new ComponentBuilder("You don't have a server! Use /server create to create one.").color(ChatColor.RED).create());
            return false;
        }
        
        PlayerServer server = playerServers.get(playerUuid);
        
        // Stop the server if it's running
        if (server.isRunning()) {
            serverManager.stopServer(server);
        }
        
        // Delete actual server files
        serverManager.deleteServer(server);
        
        // Unregister server from BungeeCord
        getProxy().getServers().remove(server.getServerName());
        
        // Delete from database
        try (PreparedStatement stmt = dbConnection.prepareStatement("DELETE FROM servers WHERE id = ?")) {
            stmt.setInt(1, server.getId());
            stmt.executeUpdate();
        } catch (SQLException e) {
            getLogger().log(Level.SEVERE, "Failed to delete server for player " + player.getName(), e);
            player.sendMessage(new ComponentBuilder("Failed to delete server! Please try again later.").color(ChatColor.RED).create());
            return false;
        }
        
        // Remove from memory
        playerServers.remove(playerUuid);
        
        player.sendMessage(new ComponentBuilder("Your server has been deleted!").color(ChatColor.GREEN).create());
        return true;
    }
    
    public boolean joinPlayerServer(ProxiedPlayer player) {
        UUID playerUuid = player.getUniqueId();
        
        // Check if player has a server
        if (!playerServers.containsKey(playerUuid)) {
            player.sendMessage(new ComponentBuilder("You don't have a server! Use /server create to create one.").color(ChatColor.RED).create());
            return false;
        }
        
        PlayerServer server = playerServers.get(playerUuid);
        
        // Start server if it's not running
        if (!server.isRunning()) {
            player.sendMessage(new ComponentBuilder("Starting your server, please wait...").color(ChatColor.YELLOW).create());
            boolean success = serverManager.startServer(server);
            if (!success) {
                player.sendMessage(new ComponentBuilder("Failed to start your server! Please contact an administrator.").color(ChatColor.RED).create());
                return false;
            }
        }
        
        // Update last active time
        updateLastActiveTime(server);
        
        // Connect to server
        player.connect(getProxy().getServerInfo(server.getServerName()));
        return true;
    }
    
    public void listPlayerServers(ProxiedPlayer player) {
        player.sendMessage(new ComponentBuilder("--------- Player Servers ---------").color(ChatColor.GOLD).create());
        
        boolean foundServers = false;
        for (PlayerServer server : playerServers.values()) {
            foundServers = true;
            ServerInfo serverInfo = getProxy().getServerInfo(server.getServerName());
            boolean isOnline = server.isRunning();
            
            ChatColor statusColor = isOnline ? ChatColor.GREEN : ChatColor.RED;
            String status = isOnline ? "ONLINE" : "OFFLINE";
            
            player.sendMessage(new ComponentBuilder(server.getServerName())
                    .color(ChatColor.YELLOW)
                    .append(" - Owner: " + server.getPlayerName())
                    .color(ChatColor.WHITE)
                    .append(" [" + status + "]")
                    .color(statusColor)
                    .create());
        }
        
        if (!foundServers) {
            player.sendMessage(new ComponentBuilder("No player servers available!").color(ChatColor.RED).create());
        }
        
        player.sendMessage(new ComponentBuilder("--------------------------------").color(ChatColor.GOLD).create());
    }
    
    public void openManageGui(ProxiedPlayer player) {
        UUID playerUuid = player.getUniqueId();
        
        // Check if player has a server
        if (!playerServers.containsKey(playerUuid)) {
            player.sendMessage(new ComponentBuilder("You don't have a server! Use /server create to create one.").color(ChatColor.RED).create());
            return;
        }
        
        PlayerServer server = playerServers.get(playerUuid);
        
        // Open the GUI (this would be implemented with a plugin messaging channel to a Spigot plugin)
        guiManager.openManageGui(player, server);
    }
    
    private int findAvailablePort(int start, int max) {
        // Get all used ports
        for (int port = start; port <= max; port++) {
            boolean used = false;
            for (PlayerServer server : playerServers.values()) {
                if (server.getPort() == port) {
                    used = true;
                    break;
                }
            }
            if (!used) {
                return port;
            }
        }
        return -1;
    }
    
    private void updateLastActiveTime(PlayerServer server) {
        try (PreparedStatement stmt = dbConnection.prepareStatement("UPDATE servers SET last_active = CURRENT_TIMESTAMP WHERE id = ?")) {
            stmt.setInt(1, server.getId());
            stmt.executeUpdate();
        } catch (SQLException e) {
            getLogger().log(Level.SEVERE, "Failed to update last active time for server " + server.getServerName(), e);
        }
    }
    
    // Inner classes
    
    private class ServerCommand extends Command {
        private final PlayerServerManager plugin;
        
        public ServerCommand(PlayerServerManager plugin) {
            super("server", "playerserver.command.server", "pserver", "ps");
            this.plugin = plugin;
        }
        
        @Override
        public void execute(CommandSender sender, String[] args) {
            if (!(sender instanceof ProxiedPlayer)) {
                sender.sendMessage(new ComponentBuilder("This command can only be used by players!").color(ChatColor.RED).create());
                return;
            }
            
            ProxiedPlayer player = (ProxiedPlayer) sender;
            
            if (args.length == 0) {
                showHelp(player);
                return;
            }
            
            String subCommand = args[0].toLowerCase();
            
            switch (subCommand) {
                case "create":
                    if (!player.hasPermission("playerserver.create")) {
                        player.sendMessage(new ComponentBuilder("You don't have permission to create a server!").color(ChatColor.RED).create());
                        return;
                    }
                    plugin.createPlayerServer(player);
                    break;
                case "delete":
                    if (!player.hasPermission("playerserver.delete")) {
                        player.sendMessage(new ComponentBuilder("You don't have permission to delete a server!").color(ChatColor.RED).create());
                        return;
                    }
                    plugin.deletePlayerServer(player);
                    break;
                case "join":
                    if (!player.hasPermission("playerserver.join")) {
                        player.sendMessage(new ComponentBuilder("You don't have permission to join a server!").color(ChatColor.RED).create());
                        return;
                    }
                    plugin.joinPlayerServer(player);
                    break;
                case "list":
                    if (!player.hasPermission("playerserver.list")) {
                        player.sendMessage(new ComponentBuilder("You don't have permission to list servers!").color(ChatColor.RED).create());
                        return;
                    }
                    plugin.listPlayerServers(player);
                    break;
                case "manage":
                    if (!player.hasPermission("playerserver.manage")) {
                        player.sendMessage(new ComponentBuilder("You don't have permission to manage a server!").color(ChatColor.RED).create());
                        return;
                    }
                    plugin.openManageGui(player);
                    break;
                default:
                    showHelp(player);
                    break;
            }
        }
        
        private void showHelp(ProxiedPlayer player) {
            player.sendMessage(new ComponentBuilder("--------- Player Server Commands ---------").color(ChatColor.GOLD).create());
            player.sendMessage(new ComponentBuilder("/server create").color(ChatColor.YELLOW).append(" - Create your own server").color(ChatColor.WHITE).create());
            player.sendMessage(new ComponentBuilder("/server delete").color(ChatColor.YELLOW).append(" - Delete your server").color(ChatColor.WHITE).create());
            player.sendMessage(new ComponentBuilder("/server join").color(ChatColor.YELLOW).append(" - Join your server").color(ChatColor.WHITE).create());
            player.sendMessage(new ComponentBuilder("/server list").color(ChatColor.YELLOW).append(" - List all player servers").color(ChatColor.WHITE).create());
            player.sendMessage(new ComponentBuilder("/server manage").color(ChatColor.YELLOW).append(" - Manage your server settings").color(ChatColor.WHITE).create());
            player.sendMessage(new ComponentBuilder("----------------------------------------").color(ChatColor.GOLD).create());
        }
    }
    
    private class InactivityChecker implements Runnable {
        @Override
        public void run() {
            long inactivityThreshold = config.getLong("server.inactivity_minutes", 5);
            
            for (PlayerServer server : playerServers.values()) {
                if (!server.isRunning()) {
                    continue;
                }
                
                // Check if server has players
                ServerInfo serverInfo = getProxy().getServerInfo(server.getServerName());
                if (serverInfo.getPlayers().isEmpty()) {
                    // Check last activity time
                    try (PreparedStatement stmt = dbConnection.prepareStatement("SELECT (CAST(strftime('%s', CURRENT_TIMESTAMP) as INTEGER) - CAST(strftime('%s', last_active) as INTEGER)) / 60 as minutes_inactive FROM servers WHERE id = ?")) {
                        stmt.setInt(1, server.getId());
                        try (ResultSet rs = stmt.executeQuery()) {
                            if (rs.next()) {
                                int minutesInactive = rs.getInt("minutes_inactive");
                                if (minutesInactive >= inactivityThreshold) {
                                    getLogger().info("Stopping inactive server: " + server.getServerName() + " (" + minutesInactive + " minutes inactive)");
                                    serverManager.stopServer(server);
                                }
                            }
                        }
                    } catch (SQLException e) {
                        getLogger().log(Level.SEVERE, "Failed to check inactivity for server " + server.getServerName(), e);
                    }
                } else {
                    // Update last active time if the server has players
                    updateLastActiveTime(server);
                }
            }
        }
    }
    
    // Getter methods
    
    public Configuration getConfig() {
        return config;
    }
    
    public Connection getDbConnection() {
        return dbConnection;
    }
    
    public Map<UUID, PlayerServer> getPlayerServers() {
        return playerServers;
    }
    
    public ServerManager getServerManager() {
        return serverManager;
    }
    
    public GuiManager getGuiManager() {
        return guiManager;
    }
}
