 import net.md_5.bungee.api.CommandSender;
 import net.md_5.bungee.api.connection.ProxiedPlayer;
 import net.md_5.bungee.api.plugin.Command;

 import java.util.UUID;

 public class ServerCommand extends Command {

  private final PlayerServerPlugin plugin;

  public ServerCommand(PlayerServerPlugin plugin) {
   super("server", "playerserver.command.server", "pserver"); // Name, permission, aliases
   this.plugin = plugin;
  }

  @Override
  public void execute(CommandSender sender, String[] args) {
   if (!(sender instanceof ProxiedPlayer)) {
    sender.sendMessage("This command can only be used by players.");
    return;
   }

   ProxiedPlayer player = (ProxiedPlayer) sender;
   UUID playerUUID = player.getUniqueId();

   if (args.length == 0) {
    sender.sendMessage("Usage: /server <create|delete|join|list|manage>");
    return;
   }

   switch (args[0].toLowerCase()) {
    case "create":
     handleCreate(player, playerUUID);
     break;
    case "delete":
     handleDelete(player, playerUUID);
     break;
    case "join":
     handleJoin(player, playerUUID);
     break;
    case "list":
     handleList(player);
     break;
    case "manage":
     handleManage(player);
     break;
    default:
     sender.sendMessage("Unknown subcommand: " + args[0]);
   }
  }

  private void handleCreate(ProxiedPlayer player, UUID playerUUID) {
   if (plugin.getDatabaseManager().hasServer(playerUUID.toString())) {
    player.sendMessage("You already have a server!");
    return;
   }

   plugin.getServerManager().createServer(playerUUID);
   player.sendMessage("Creating your server...");
  }

  private void handleDelete(ProxiedPlayer player, UUID playerUUID) {
   if (!plugin.getDatabaseManager().hasServer(playerUUID.toString())) {
    player.sendMessage("You don't have a server to delete!");
    return;
   }

   plugin.getServerManager().deleteServer(playerUUID);
   player.sendMessage("Deleting your server...");
  }

  private void handleJoin(ProxiedPlayer player, UUID playerUUID) {
   String serverName = plugin.getDatabaseManager().getServerName(playerUUID.toString());
   if (serverName == null) {
    player.sendMessage("You don't have a server to join!");
    return;
   }

   player.connect(plugin.getProxy().getServerInfo(serverName));
  }

  private void handleList(ProxiedPlayer player) {
   // Implement logic to list available player servers
   player.sendMessage("Listing available servers (not implemented yet)...");
  }

  private void handleManage(ProxiedPlayer player) {
   plugin.getGuiManager().openMainMenu(player);
  }
 }
