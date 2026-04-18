 import net.md_5.bungee.api.ProxyServer;
 import net.md_5.bungee.api.config.ServerInfo;

 import java.io.File;
 import java.io.IOException;
 import java.util.UUID;

 public class ServerManager {

  private final PlayerServerPlugin plugin;

  public ServerManager(PlayerServerPlugin plugin) {
   this.plugin = plugin;
  }

  public void createServer(UUID playerUUID) {
   String serverName = playerUUID.toString().substring(0, 8) + "-server"; // Shortened UUID for server name
   File serverDirectory = new File(plugin.getDataFolder(), "servers/" + serverName);

   if (serverDirectory.exists()) {
    plugin.getLogger().warning("Server directory already exists: " + serverName);
    return;
   }

   serverDirectory.mkdirs();

   // 1. Create server.properties
   ServerPropertiesGenerator.generate(serverDirectory, serverName);

   // 2. Copy a pre-configured Spigot/Paper server jar (you'll need to provide this)
   File serverJar = new File(serverDirectory, "server.jar");
   try {
    // Replace "template-server.jar" with the actual name of your template server jar
    plugin.getResourceAsStream("template-server.jar");
    //Files.copy(plugin.getResourceAsStream("template-server.jar"), serverJar.toPath());
   } catch (Exception e) {
    plugin.getLogger().severe("Error copying server jar: " + e.getMessage());
    // Attempt to delete the directory if creation fails
    deleteDirectory(serverDirectory);
    return;
   }

   // 3. Create a start script (e.g., start.sh or start.bat)
   createStartScript(serverDirectory, serverName);

   // 4. Register the server with BungeeCord
   registerServer(serverName, serverDirectory.getAbsolutePath());

   // 5. Save server information to the database
   plugin.getDatabaseManager().createServerEntry(playerUUID.toString(), serverName);
  }

  private void registerServer(String serverName, String serverAddress) {
   ServerInfo serverInfo = ProxyServer.getInstance().constructServerInfo(
    serverName,
    java.net.InetSocketAddress.createUnresolved("localhost", 25565), // Replace with actual address/port
    "Player Server",
    false // Restricted
   );
   ProxyServer.getInstance().getServers().put(serverName, serverInfo);
  }

  public void startServer(UUID playerUUID) {
   String serverName = plugin.getDatabaseManager().getServerName(playerUUID.toString());
   if (serverName == null) {
    plugin.getLogger().warning("Server name not found for player: " + playerUUID);
    return;
   }

   File serverDirectory = new File(plugin.getDataFolder(), "servers/" + serverName);
   if (!serverDirectory.exists()) {
    plugin.getLogger().warning("Server directory not found: " + serverName);
    return;
   }

   // Execute the start script
   try {
    ProcessBuilder processBuilder = new ProcessBuilder("./start.sh"); // Or "start.bat"
    processBuilder.directory(serverDirectory);
    Process process = processBuilder.start();

    // Optionally, capture the output of the process
    // (This is important for debugging and monitoring)
    // new BufferedReader(new InputStreamReader(process.getInputStream())).lines().forEach(System.out::println);

    plugin.getDatabaseManager().updateServerStatus(playerUUID.toString(), "STARTING");

   } catch (IOException e) {
    plugin.getLogger().severe("Error starting server: " + e.getMessage());
    plugin.getDatabaseManager().updateServerStatus(playerUUID.toString(), "STOPPED");
   }
  }

  public void stopServer(UUID playerUUID) {
   String serverName = plugin.getDatabaseManager().getServerName(playerUUID.toString());
   if (serverName == null) {
    plugin.getLogger().warning("Server name not found for player: " + playerUUID);
    return;
   }

   // Send a shutdown command to the server (e.g., using rcon or a custom plugin)
   // This is a placeholder; implement the actual shutdown logic
   plugin.getLogger().info("Stopping server: " + serverName);
   plugin.getDatabaseManager().updateServerStatus(playerUUID.toString(), "STOPPED");
  }

  public void deleteServer(UUID playerUUID) {
   String serverName = plugin.getDatabaseManager().getServerName(playerUUID.toString());
   if (serverName == null) {
    plugin.getLogger().warning("Server name not found for player: " + playerUUID);
    return;
   }

   File serverDirectory = new File(plugin.getDataFolder(), "servers/" + serverName);
   if (!serverDirectory.exists()) {
    plugin.getLogger().warning("Server directory not found: " + serverName);
    return;
   }

   // 1. Stop the server if it's running
   stopServer(playerUUID);

   // 2. Unregister the server from BungeeCord
   ProxyServer.getInstance().getServers().remove(serverName);

   // 3. Delete the server directory
   if (deleteDirectory(serverDirectory)) {
    plugin.getLogger().info("Server directory deleted: " + serverName);
   } else {
    plugin.getLogger().warning("Failed to delete server directory: " + serverName);
   }

   // 4. Remove server information from the database
   plugin.getDatabaseManager().deleteServerEntry(playerUUID.toString());
  }

  private void createStartScript(File serverDirectory, String serverName) {
   // Create a start.sh (Linux) or start.bat (Windows) script
   // This script will execute the server jar with the appropriate RAM allocation
   // Example (start.sh):
   // #!/bin/bash
   // java -Xms512m -Xmx1024m -jar server.jar nogui
   // Example (start.bat):
   // java -Xms512m -Xmx1024m -jar server.jar nogui
  }

  // Helper method to recursively delete a directory
  private boolean deleteDirectory(File directory) {
   if (directory.exists()) {
    File[] files = directory.listFiles();
    if (null != files) {
     for (File file : files) {
      if (file.isDirectory()) {
       deleteDirectory(file);
      } else {
       file.delete();
      }
     }
    }
   }
   return directory.delete();
  }
 }
