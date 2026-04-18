 import net.md_5.bungee.config.Configuration;
 import net.md_5.bungee.config.ConfigurationProvider;
 import net.md_5.bungee.config.YamlConfiguration;

 import java.io.File;
 import java.io.IOException;
 import java.io.InputStream;
 import java.nio.file.Files;

 public class ConfigManager {

  private final PlayerServerPlugin plugin;
  private Configuration config;

  public ConfigManager(PlayerServerPlugin plugin) {
   this.plugin = plugin;
  }

  public void loadConfig() {
   File configFile = new File(plugin.getDataFolder(), "config.yml");
   if (!configFile.exists()) {
    plugin.getDataFolder().mkdirs();
    try (InputStream in = plugin.getResourceAsStream("config.yml")) {
     Files.copy(in, configFile.toPath());
    } catch (IOException e) {
     e.printStackTrace();
    }
   }

   try {
    config = ConfigurationProvider.getProvider(YamlConfiguration.class).load(configFile);
   } catch (IOException e) {
    e.printStackTrace();
   }
  }

  public Configuration getConfig() {
   return config;
  }

  public String getString(String path) {
   return config.getString(path);
  }

  public int getInt(String path) {
   return config.getInt(path);
  }

  // Add more methods for other data types as needed
 }
