package com.playerservers;

import net.md_5.bungee.api.ChatColor;
import net.md_5.bungee.api.chat.ComponentBuilder;
import net.md_5.bungee.api.config.ServerInfo;
import net.md_5.bungee.api.connection.ProxiedPlayer;
import net.md_5.bungee.api.connection.Server;
import net.md_5.bungee.config.Configuration;

import java.io.ByteArrayOutputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.util.List;
import java.util.UUID;
import java.util.logging.Level;

public class GuiManager {
    private final PlayerServerManager plugin;
    private static final String CHANNEL_NAME = "PlayerServer:GUI";
    
    public GuiManager(PlayerServerManager plugin) {
        this.plugin = plugin;
        
        // Register plugin messaging channel
        plugin.getProxy().registerChannel(CHANNEL_NAME);
        
        // Register listener for plugin messages
        plugin.getProxy().getPluginManager().registerListener(plugin, new PluginMessageListener(plugin));
    }
    
    public void openManageGui(ProxiedPlayer player, PlayerServer server) {
        ServerInfo hubServer = getHubServer();
        if (hubServer == null) {
            player.sendMessage(new ComponentBuilder("Unable to open management GUI. Please contact an administrator.").color(ChatColor.RED).create());
            return;
        }
        
        // Connect to hub server if not already connected
        if (player.getServer() == null || !player.getServer().getInfo().equals(hubServer)) {
            player.connect(hubServer);
            
            // Schedule opening GUI after player connects
            plugin.getProxy().getScheduler().schedule(plugin, () -> sendOpenGuiMessage(player, server), 1, java.util.concurrent.TimeUnit.SECONDS);
        } else {
            sendOpenGuiMessage(player, server);
        }
    }
    
    private ServerInfo getHubServer() {
        Configuration config = plugin.getConfig();
        String hubServerName = config.getString("gui.hub_server", "lobby");
        return plugin.getProxy().getServerInfo(hubServerName);
    }
    
    private void sendOpenGuiMessage(ProxiedPlayer player, PlayerServer server) {
        if (player.getServer() == null) {
            return;
        }
        
        try {
            ByteArrayOutputStream stream = new ByteArrayOutputStream();
            DataOutputStream out = new DataOutputStream(stream);
            
            // Write action type
            out.writeUTF("OPEN_GUI");
            
            // Write server info
            out.writeUTF(server.getServerName());
            out.writeUTF(server.getPlayerName());
            out.writeBoolean(server.isRunning());
            out.writeInt(server.getOperators().size());
            
            for (UUID uuid : server.getOperators()) {
                out.writeUTF(uuid.toString());
            }
            
            // Write plugins
            List<String> allowedPlugins = plugin.getConfig().getStringList("server.allowed_plugins");
            out.writeInt(allowedPlugins.size());
            
            for (String pluginName : allowedPlugins) {
                out.writeUTF(pluginName);
                out.writeBoolean(server.hasPlugin(pluginName));
            }
            
            // Write settings
            out.writeInt(server.getSettings().size());
            
            for (String key : server.getSettings().keySet()) {
                out.writeUTF(key);
                out.writeUTF(server.getSetting(key));
            }
            
            // Send message
            player.getServer().sendData(CHANNEL_NAME, stream.toByteArray());
            
        } catch (IOException e) {
            plugin.getLogger().log(Level.SEVERE, "Failed to send GUI message to player " + player.getName(), e);
            player.sendMessage(new ComponentBuilder("Failed to open management GUI. Please try again later.").color(ChatColor.RED).create());
        }
    }
    
    public void handleGuiAction(ProxiedPlayer player, String action, String... args) {
        UUID playerUuid = player.getUniqueId();
        PlayerServer server = plugin.getPlayerServers().get(playerUuid);
        
        if (server == null) {
            player.sendMessage(new ComponentBuilder("You don't have a server!").color(ChatColor.RED).create());
            return;
        }
        
        ServerManager serverManager = plugin.getServerManager();
        
        switch (action) {
            case "START_SERVER":
                if (!server.isRunning()) {
                    player.sendMessage(new ComponentBuilder("Starting your server...").color(ChatColor.YELLOW).create());
                    boolean success = serverManager.startServer(server);
                    if (success) {
                        player.sendMessage(new ComponentBuilder("Server started successfully!").color(ChatColor.GREEN).create());
                    } else {
                        player.sendMessage(new ComponentBuilder("Failed to start server!").color(ChatColor.RED).create());
                    }
                } else {
                    player.sendMessage(new ComponentBuilder("Your server is already running!").color(ChatColor.YELLOW).create());
                }
                break;
                
            case "STOP_SERVER":
                if (server.isRunning()) {
                    player.sendMessage(new ComponentBuilder("Stopping your server...").color(ChatColor.YELLOW).create());
                    boolean success = serverManager.stopServer(server);
                    if (success) {
                        player.sendMessage(new ComponentBuilder("Server stopped successfully!").color(ChatColor.GREEN).create());
                    } else {
                        player.sendMessage(new ComponentBuilder("Failed to stop server!").color(ChatColor.RED).create());
                    }
                } else {
                    player.sendMessage(new ComponentBuilder("Your server is not running!").color(ChatColor.YELLOW).create());
                }
                break;
                
            case "INSTALL_PLUGIN":
                if (args.length < 1) {
                    return;
                }
                
                String pluginName = args[0];
                player.sendMessage(new ComponentBuilder("Installing plugin " + pluginName + "...").color(ChatColor.YELLOW).create());
                
                boolean installSuccess = serverManager.installPlugin(server, pluginName);
                if (installSuccess) {
                    player.sendMessage(new ComponentBuilder("Plugin installed successfully!").color(ChatColor.GREEN).create());
                } else {
                    player.sendMessage(new ComponentBuilder("Failed to install plugin!").color(ChatColor.RED).create());
                }
                break;
                
            case "UNINSTALL_PLUGIN":
                if (args.length < 1) {
                    return;
                }
                
                String pluginToRemove = args[0];
                player.sendMessage(new ComponentBuilder("Uninstalling plugin " + pluginToRemove + "...").color(ChatColor.YELLOW).create());
                
                boolean uninstallSuccess = serverManager.uninstallPlugin(server, pluginToRemove);
                if (uninstallSuccess) {
                    player.sendMessage(new ComponentBuilder("Plugin uninstalled successfully!").color(ChatColor.GREEN).create());
                } else {
                    player.sendMessage(new ComponentBuilder("Failed to uninstall plugin!").color(ChatColor.RED).create());
                }
                break;
                
            case "ADD_OPERATOR":
                if (args.length < 1) {
                    return;
                }
                
                String playerName = args[0];
                ProxiedPlayer targetPlayer = plugin.getProxy().getPlayer(playerName);
                
                if (targetPlayer == null) {
                    player.sendMessage(new ComponentBuilder("Player not found!").color(ChatColor.RED).create());
                    return;
                }
                
                UUID targetUuid = targetPlayer.getUniqueId();
                if (server.isOperator(targetUuid)) {
                    player.sendMessage(new ComponentBuilder(playerName + " is already an operator!").color(ChatColor.YELLOW).create());
                    return;
                }
                
                server.addOperator(targetUuid);
                
                try (java.sql.PreparedStatement stmt = plugin.getDbConnection().prepareStatement(
                        "INSERT INTO server_operators (server_id, operator_uuid) VALUES (?, ?)")) {
                    stmt.setInt(1, server.getId());
                    stmt.setString(2, targetUuid.toString());
                    stmt.executeUpdate();
                    
                    player.sendMessage(new ComponentBuilder(playerName + " has been added as an operator!").color(ChatColor.GREEN).create());
                } catch (java.sql.SQLException e) {
                    plugin.getLogger().log(Level.SEVERE, "Failed to update database for operator addition", e);
                    player.sendMessage(new ComponentBuilder("Failed to add operator! Please try again later.").color(ChatColor.RED).create());
                }
                break;
                
            case "REMOVE_OPERATOR":
                if (args.length < 1) {
                    return;
                }
                
                String opName = args[0];
                UUID opUuid = null;
                
                // Find the UUID from the operator name
                for (ProxiedPlayer p : plugin.getProxy().getPlayers()) {
                    if (p.getName().equalsIgnoreCase(opName)) {
                        opUuid = p.getUniqueId();
                        break;
                    }
                }
                
                if (opUuid == null) {
                    player.sendMessage(new ComponentBuilder("Player not found!").color(ChatColor.RED).create());
                    return;
                }
                
                if (!server.isOperator(opUuid)) {
                    player.sendMessage(new ComponentBuilder(opName + " is not an operator!").color(ChatColor.YELLOW).create());
                    return;
                }
                
                server.removeOperator(opUuid);
                
                try (java.sql.PreparedStatement stmt = plugin.getDbConnection().prepareStatement(
                        "DELETE FROM server_operators WHERE server_id = ? AND operator_uuid = ?")) {
                    stmt.setInt(1, server.getId());
                    stmt.setString(2, opUuid.toString());
                    stmt.executeUpdate();
                    
                    player.sendMessage(new ComponentBuilder(opName + " has been removed as an operator!").color(ChatColor.GREEN).create());
                } catch (java.sql.SQLException e) {
                    plugin.getLogger().log(Level.SEVERE, "Failed to update database for operator removal", e);
                    player.sendMessage(new ComponentBuilder("Failed to remove operator! Please try again later.").color(ChatColor.RED).create());
                }
                break;
                
            case "UPDATE_SETTING":
                if (args.length < 2) {
                    return;
                }
                
                String key = args[0];
                String value = args[1];
                
                player.sendMessage(new ComponentBuilder("Updating setting " + key + "...").color(ChatColor.YELLOW).create());
                
                boolean updateSuccess = serverManager.updateServerSetting(server, key, value);
                if (updateSuccess) {
                    player.sendMessage(new ComponentBuilder("Setting updated successfully!").color(ChatColor.GREEN).create());
                } else {
                    player.sendMessage(new ComponentBuilder("Failed to update setting!").color(ChatColor.RED).create());
                }
                break;
                
            default:
                plugin.getLogger().warning("Unknown GUI action: " + action);
                break;
        }
    }
}
