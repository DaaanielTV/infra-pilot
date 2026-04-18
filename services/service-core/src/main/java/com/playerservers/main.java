 // Main plugin class
 public class PlayerServerPlugin extends Plugin {

  private DatabaseManager databaseManager;
  private ServerManager serverManager;
  private ConfigManager configManager;
  private GUIManager guiManager;

  @Override
  public void onEnable() {
   // Load configuration
   configManager = new ConfigManager(this);
   configManager.loadConfig();

   // Initialize database
   databaseManager = new DatabaseManager(this);
   try {
    databaseManager.connect();
    databaseManager.setupDatabase();
   } catch (SQLException e) {
    getLogger().severe("Failed to connect to the database: " + e.getMessage());
    // Disable the plugin if the database connection fails
    onDisable();
    return;
   }

   // Initialize server manager
   serverManager = new ServerManager(this);

   // Initialize GUI manager
   guiManager = new GUIManager(this);

   // Register commands
   getProxy().getPluginManager().registerCommand(this, new ServerCommand(this));

   // Register listeners (if needed)
   // getProxy().getPluginManager().registerListener(this, new PlayerListener(this));

   getLogger().info("PlayerServerPlugin has been enabled!");
  }

  @Override
  public void onDisable() {
   // Shutdown tasks, close database connections, etc.
   if (databaseManager != null) {
    databaseManager.disconnect();
   }
   getLogger().info("PlayerServerPlugin has been disabled!");
  }

  public DatabaseManager getDatabaseManager() {
   return databaseManager;
  }

  public ServerManager getServerManager() {
   return serverManager;
  }

  public ConfigManager getConfigManager() {
   return configManager;
  }

  public GUIManager getGuiManager() {
   return guiManager;
  }
 }
