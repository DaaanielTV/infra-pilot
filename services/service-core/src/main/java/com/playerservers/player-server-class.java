package com.playerservers;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.UUID;

public class PlayerServer {
    private int id;
    private UUID playerUuid;
    private String playerName;
    private String serverName;
    private int port;
    private boolean running;
    private List<UUID> operators;
    private List<String> plugins;
    private Map<String, String> settings;
    
    public PlayerServer(int id, UUID playerUuid, String playerName, String serverName, int port) {
        this.id = id;
        this.playerUuid = playerUuid;
        this.playerName = playerName;
        this.serverName = serverName;
        this.port = port;
        this.running = false;
        this.operators = new ArrayList<>();
        this.plugins = new ArrayList<>();
        this.settings = new HashMap<>();
    }
    
    public int getId() {
        return id;
    }
    
    public UUID getPlayerUuid() {
        return playerUuid;
    }
    
    public String getPlayerName() {
        return playerName;
    }
    
    public String getServerName() {
        return serverName;
    }
    
    public int getPort() {
        return port;
    }
    
    public boolean isRunning() {
        return running;
    }
    
    public void setRunning(boolean running) {
        this.running = running;
    }
    
    public List<UUID> getOperators() {
        return operators;
    }
    
    public void addOperator(UUID uuid) {
        if (!operators.contains(uuid)) {
            operators.add(uuid);
        }
    }
    
    public void removeOperator(UUID uuid) {
        operators.remove(uuid);
    }
    
    public boolean isOperator(UUID uuid) {
        return operators.contains(uuid);
    }
    
    public List<String> getPlugins() {
        return plugins;
    }
    
    public void addPlugin(String pluginName) {
        if (!plugins.contains(pluginName)) {
            plugins.add(pluginName);
        }
    }
    
    public void removePlugin(String pluginName) {
        plugins.remove(pluginName);
    }
    
    public boolean hasPlugin(String pluginName) {
        return plugins.contains(pluginName);
    }
    
    public Map<String, String> getSettings() {
        return settings;
    }
    
    public String getSetting(String key) {
        return settings.getOrDefault(key, "");
    }
    
    public void setSetting(String key, String value) {
        settings.put(key, value);
    }
}
