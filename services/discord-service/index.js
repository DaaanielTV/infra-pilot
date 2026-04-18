const { Client, GatewayIntentBits, Partials, EmbedBuilder, ActionRowBuilder, ButtonBuilder, ButtonStyle } = require('discord.js');
const axios = require('axios');
const dotenv = require('dotenv');
const fs = require('fs');
const path = require('path');

dotenv.config();

// --- Constants and Configuration ---
const SERVER_LIMITS_FILE = path.join(__dirname, 'server_limits.json');
const DISCORD_TOKEN = process.env.DISCORD_TOKEN;
const PTERODACTYL_API_URL = process.env.PTERODACTYL_API_URL;
const PTERODACTYL_API_KEY = process.env.PTERODACTYL_API_KEY;
const SERVER_CREATION_CHANNEL_ID = process.env.SERVER_CREATION_CHANNEL_ID;
const SERVER_CREATOR_ROLE_ID = process.env.SERVER_CREATOR_ROLE_ID;
const LOCATION_ID = process.env.LOCATION_ID;
const MAX_SERVERS_PER_USER = parseInt(process.env.MAX_SERVERS_PER_USER) || 1;

// --- Server Types Configuration ---
const SERVER_TYPES = {
  'minecraft': {
    name: 'Minecraft Server',
    eggId: process.env.MINECRAFT_EGG_ID,
    memory: 1024,
    dockerImage: 'ghcr.io/pterodactyl/yolks:java_17'
  },
  'nodejs': {
    name: 'Node.js Server',
    eggId: process.env.NODEJS_EGG_ID,
    memory: 256,
    dockerImage: 'ghcr.io/pterodactyl/yolks:nodejs_18'
  },
  'teamspeak': {
    name: 'TeamSpeak Server',
    eggId: process.env.TEAMSPEAK_EGG_ID,
    memory: 256,
    dockerImage: 'ghcr.io/pterodactyl/yolks:teamspeak'
  },
  'database': {
    name: 'MySQL Datenbank',
    eggId: process.env.DATABASE_EGG_ID,
    memory: 256,
    dockerImage: 'ghcr.io/pterodactyl/yolks:mysql'
  },
  'python': {
    name: 'Python Server',
    eggId: process.env.PYTHON_EGG_ID,
    memory: 512,
    dockerImage: 'ghcr.io/pterodactyl/yolks:python_3.10'
  }
};

// --- Utility Functions ---
function loadServerLimits() {
  try {
    if (!fs.existsSync(SERVER_LIMITS_FILE)) {
      fs.writeFileSync(SERVER_LIMITS_FILE, JSON.stringify({}));
    }
    return JSON.parse(fs.readFileSync(SERVER_LIMITS_FILE, 'utf8'));
  } catch (error) {
    console.error('Fehler beim Laden der Serverlimits:', error);
    return {};
  }
}

function saveServerLimits(limits) {
  try {
    fs.writeFileSync(SERVER_LIMITS_FILE, JSON.stringify(limits, null, 2));
  } catch (error) {
    console.error('Fehler beim Speichern der Serverlimits:', error);
  }
}

async function createPterodactylUser(userData) {
  try {
    const response = await axios.post(`${PTERODACTYL_API_URL}/api/application/users`, userData, {
      headers: {
        'Authorization': `Bearer ${PTERODACTYL_API_KEY}`,
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      }
    });
    return response.data.attributes;
  } catch (error) {
    console.error('API Error creating user:', error.response?.data || error.message);
    throw new Error(error.response?.data?.errors?.[0]?.detail || 'Failed to create user');
  }
}

async function createPterodactylServer(serverData) {
  try {
    const response = await axios.post(`${PTERODACTYL_API_URL}/api/application/servers`, serverData, {
      headers: {
        'Authorization': `Bearer ${PTERODACTYL_API_KEY}`,
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      }
    });
    return response.data.attributes;
  } catch (error) {
    console.error('API Error creating server:', error.response?.data || error.message);
    throw new Error(error.response?.data?.errors?.[0]?.detail || 'Failed to create server');
  }
}

function validateEmail(email) {
  const re = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
  return re.test(String(email).toLowerCase());
}

function validateUsername(username) {
  const re = /^[a-zA-Z0-9_]{3,20}$/;
  return re.test(username);
}

function validatePassword(password) {
  return password.length >= 8 &&
    /[A-Za-z]/.test(password) &&
    /[0-9]/.test(password) &&
    /[^A-Za-z0-9]/.test(password);
}

// --- Discord Client Initialization ---
const client = new Client({
  intents: [
    GatewayIntentBits.Guilds,
    GatewayIntentBits.GuildMessages,
    GatewayIntentBits.MessageContent,
    GatewayIntentBits.GuildMembers,
  ],
  partials: [Partials.Channel],
});

// --- State Management ---
const userRegistrationState = new Map();

// --- Helper Functions for Message Handling ---
async function handleEmailInput(message, userState) {
  if (!validateEmail(message.content)) {
    await message.reply({
      content: 'Ungültige E-Mail-Adresse. Bitte gib eine gültige E-Mail-Adresse ein.',
      ephemeral: true
    });
    return false;
  }

  userState.data.email = message.content;
  userState.step = 'username';

  const usernameEmbed = new EmbedBuilder()
    .setTitle('Server-Erstellung')
    .setDescription('E-Mail gespeichert. Bitte gib nun deinen gewünschten Benutzernamen ein:')
    .setColor('#007bff')
    .setFooter({ text: 'Schritt 2 von 3: Benutzername' });

  await message.reply({ embeds: [usernameEmbed], ephemeral: true });
  return true;
}

async function handleUsernameInput(message, userState) {
  if (!validateUsername(message.content)) {
    await message.reply({
      content: 'Ungültiger Benutzername. Der Benutzername muss 3-20 Zeichen lang sein und darf nur Buchstaben, Zahlen und Unterstriche enthalten.',
      ephemeral: true
    });
    return false;
  }

  userState.data.username = message.content;
  userState.step = 'password';

  const passwordEmbed = new EmbedBuilder()
    .setTitle('Server-Erstellung')
    .setDescription('Benutzername gespeichert. Bitte gib nun dein gewünschtes Passwort ein.\n\n**Sicherheitshinweis**: Dein Passwort sollte mindestens 8 Zeichen lang sein und eine Kombination aus Buchstaben, Zahlen und Sonderzeichen enthalten.')
    .setColor('#007bff')
    .setFooter({ text: 'Schritt 3 von 3: Passwort' });

  await message.reply({ embeds: [passwordEmbed], ephemeral: true });
  return true;
}

async function handlePasswordInput(message, userState) {
  if (!validatePassword(message.content)) {
    await message.reply({
      content: 'Passwort zu schwach. Es sollte mindestens 8 Zeichen lang sein und Buchstaben, Zahlen und Sonderzeichen enthalten.',
      ephemeral: true
    });
    return false;
  }

  userState.data.password = message.content;
  userState.step = 'processing';

  const processingEmbed = new EmbedBuilder()
    .setTitle('Server-Erstellung')
    .setDescription('Alle Informationen gesammelt. Erstelle deinen Account und Server...')
    .setColor('#ffc107')
    .setFooter({ text: 'Wird verarbeitet...' });

  const processingMsg = await message.reply({ embeds: [processingEmbed], ephemeral: true });
  return { processingMsg }; // Return the processingMsg for further use
}

async function processServerCreation(message, userState, processingMsg) {
  try {
    const userData = {
      username: userState.data.username,
      email: userState.data.email,
      first_name: userState.data.username,
      last_name: 'User',
      password: userState.data.password,
      root_admin: false,
      language: 'en'
    };

    const userResponse = await createPterodactylUser(userData);
    const userId = userResponse.id;

    const serverType = userState.data.serverType;
    const serverConfig = SERVER_TYPES[serverType];

    const serverData = {
      name: `${userState.data.username}'s ${serverConfig.name}`,
      user: userId,
      egg: parseInt(serverConfig.eggId),
      docker_image: serverConfig.dockerImage,
      startup: serverType === 'nodejs' ? 'npm start' : '',
      environment: serverType === 'nodejs'
        ? {
          STARTUP_CMD: 'npm start',
          NODE_VERSION: '18'
        }
        : {},
      limits: {
        memory: serverConfig.memory,
        swap: 0,
        disk: 1024,
        io: 500,
        cpu: 100
      },
      feature_limits: {
        databases: 0,
        allocations: 1,
        backups: 1
      },
      allocation: {
        default: null
      },
      deploy: {
        locations: [parseInt(LOCATION_ID)],
        dedicated_ip: false,
        port_range: []
      }
    };

    const serverResponse = await createPterodactylServer(serverData);

    const serverLimits = loadServerLimits();
    const userServers = serverLimits[message.author.id] || [];
    userServers.push(serverResponse.identifier);
    serverLimits[message.author.id] = userServers;
    saveServerLimits(serverLimits);

    try {
      const member = await message.guild.members.fetch(message.author.id);
      await member.roles.add(SERVER_CREATOR_ROLE_ID);
    } catch (roleError) {
      console.error('Fehler beim Zuweisen der Rolle:', roleError);
    }

    const successEmbed = new EmbedBuilder()
      .setTitle('✅ Server-Erstellung erfolgreich')
      .setDescription(`Glückwunsch! Dein ${serverConfig.name} wurde erfolgreich erstellt.

**Serverdetails:**
- Name: ${serverResponse.name}
- Typ: ${serverConfig.name}
- Speicher: ${serverConfig.memory} MB
- Server-ID: ${serverResponse.identifier}

Du kannst dich nun mit deiner E-Mail und dem Passwort im Pterodactyl-Panel anmelden.`)
      .setColor('#28a745')
      .setFooter({ text: 'Einrichtung abgeschlossen' });

    await processingMsg.edit({ embeds: [successEmbed] });
  } catch (error) {
    console.error('Fehler bei der Server-Erstellung:', error);

    const errorEmbed = new EmbedBuilder()
      .setTitle('❌ Server-Erstellung fehlgeschlagen')
      .setDescription(`Es gab einen Fehler bei der Erstellung deines Accounts oder Servers: ${error.message || 'Unbekannter Fehler'}

Bitte versuche es später erneut oder kontaktiere einen Administrator.`)
      .setColor('#dc3545')
      .setFooter({ text: 'Fehler' });

    await processingMsg.edit({ embeds: [errorEmbed] });
  } finally {
    userRegistrationState.delete(message.author.id);
  }
}

// --- Event Handlers ---
client.once('ready', () => {
  console.log(`Bot ist online als ${client.user.tag}`);

  client.application.commands.create({
    name: 'server',
    description: 'Server-Verwaltungsbefehle',
    options: [
      {
        name: 'create',
        description: 'Erstelle einen neuen Server',
        type: 1,
      }
    ]
  });
});

client.on('interactionCreate', async (interaction) => {
  if (!interaction.isCommand()) return;

  if (interaction.channelId !== SERVER_CREATION_CHANNEL_ID) {
    return interaction.reply({
      content: `Dieser Befehl kann nur im festgelegten Server-Erstellungskanal verwendet werden.`,
      ephemeral: true
    });
  }

  if (interaction.commandName === 'server') {
    const subcommand = interaction.options.getSubcommand();

    if (subcommand === 'create') {
      const serverLimits = loadServerLimits();
      const userServers = serverLimits[interaction.user.id] || [];

      if (userServers.length >= MAX_SERVERS_PER_USER) {
        return interaction.reply({
          content: `Du hast bereits die maximale Anzahl von ${MAX_SERVERS_PER_USER} Servern erreicht.`,
          ephemeral: true
        });
      }

      const row = new ActionRowBuilder()
        .addComponents(
          Object.entries(SERVER_TYPES).filter(([key, type]) => key !== 'debian').map(([key, type]) =>
            new ButtonBuilder()
              .setCustomId(`servertype_${key}`)
              .setLabel(type.name)
              .setStyle(ButtonStyle.Primary)
          )
        );

      const embed = new EmbedBuilder()
        .setTitle('Server-Erstellung')
        .setDescription('Wähle den Typ des Servers, den du erstellen möchtest:')
        .setColor('#007bff');

      await interaction.reply({
        embeds: [embed],
        components: [row],
        ephemeral: true
      });
    }
  }
});

client.on('interactionCreate', async (interaction) => {
  if (!interaction.isButton()) return;

  if (interaction.customId.startsWith('servertype_')) {
    const serverType = interaction.customId.split('_')[1];

    userRegistrationState.set(interaction.user.id, {
      step: 'email',
      data: { serverType },
      messageId: null
    });

    const embed = new EmbedBuilder()
      .setTitle('Server-Erstellung')
      .setDescription(`Du hast ${SERVER_TYPES[serverType].name} ausgewählt.\n\nBitte gib deine E-Mail-Adresse ein:`)
      .setColor('#007bff')
      .setFooter({ text: 'Schritt 1 von 3: E-Mail' });

    await interaction.update({
      embeds: [embed],
      components: []
    });
  }
});

client.on('messageCreate', async (message) => {
  if (message.author.bot || message.channelId !== SERVER_CREATION_CHANNEL_ID) return;

  const userState = userRegistrationState.get(message.author.id);
  if (!userState) return;

  try {
    await message.delete();
  } catch (error) {
    console.error('Fehler beim Löschen der Nachricht:', error);
  }

  switch (userState.step) {
    case 'email':
      if (await handleEmailInput(message, userState) === false) return;
      break;
    case 'username':
      if (await handleUsernameInput(message, userState) === false) return;
      break;
    case 'password':
      const { processingMsg } = await handlePasswordInput(message, userState);
      await processServerCreation(message, userState, processingMsg);
      break;
  }
});

// --- Discord Bot Login ---
client.login(DISCORD_TOKEN);