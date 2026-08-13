const { EmbedBuilder } = require('discord.js');
const { query } = require('./db');

const COMMAND_SPECS = [
  {
    name: 'templatecreate',
    description: 'Create a VPS template',
    options: [
      { name: 'name', description: 'Template name', type: 3, required: true },
      { name: 'image', description: 'Docker image', type: 3, required: true },
      { name: 'cpu', description: 'CPU cores', type: 10, required: false },
      { name: 'memory', description: 'Memory MB', type: 4, required: false },
      { name: 'storage', description: 'Storage GB', type: 4, required: false },
    ],
  },
  {
    name: 'templateapply',
    description: 'Apply a template to create a VPS',
    options: [
      { name: 'template_name', description: 'Template name', type: 3, required: true },
      { name: 'version', description: 'Template version (default: latest)', type: 4, required: false },
    ],
  },
  { name: 'templatelist', description: 'List available templates', type: 1 },
];

function toSpec() {
  return COMMAND_SPECS;
}

function isParsed(name) {
  return COMMAND_SPECS.some((c) => c.name === name);
}

async function handle(interaction) {
  const { commandName, options } = interaction;
  if (commandName === 'templatecreate') {
    const name = options.getString('name');
    const image = options.getString('image');
    const cpu = options.getNumber('cpu') ?? 1;
    const memory = options.getInteger('memory') ?? 1024;
    const storage = options.getInteger('storage') ?? 20;
    try {
      await query(
        'INSERT INTO templates (name, version, config, created_by) VALUES ($1, $2, $3, $4)',
        [name, 1, JSON.stringify({ image, cpu, memory, storage }), interaction.user.id]
      );
      const embed = new EmbedBuilder()
        .setTitle('Template Created')
        .setColor(0x28a745)
        .addFields(
          { name: 'Name', value: name, inline: true },
          { name: 'Image', value: image, inline: true },
          { name: 'CPU', value: String(cpu), inline: true },
          { name: 'Memory', value: `${memory}MB`, inline: true },
          { name: 'Storage', value: `${storage}GB`, inline: true }
        );
      return interaction.reply({ embeds: [embed], ephemeral: true });
    } catch (err) {
      return interaction.reply({ content: `❌ Error: ${err.message}`, ephemeral: true });
    }
  }
  if (commandName === 'templateapply') {
    await interaction.deferReply({ ephemeral: true });
    const templateName = options.getString('template_name');
    const version = options.getInteger('version');
    try {
      const sql = version
        ? 'SELECT * FROM templates WHERE name = $1 AND version = $2'
        : 'SELECT * FROM templates WHERE name = $1 ORDER BY version DESC LIMIT 1';
      const params = version ? [templateName, version] : [templateName];
      const result = await query(sql, params);
      if (!result.rows.length) return interaction.editReply({ content: '❌ Template not found.' });
      const template = result.rows[0];
      const cfg = typeof template.config === 'string' ? JSON.parse(template.config) : template.config;
      const vpsManager = require('./vpsManager');
      const created = await vpsManager.createVps(interaction.user.id, {
        cpu: cfg.cpu,
        memory: cfg.memory,
        storage: cfg.storage,
        image: cfg.image,
      });
      if (!created) return interaction.editReply({ content: '❌ Failed to create VPS.' });
      const embed = new EmbedBuilder()
        .setTitle('VPS Created from Template')
        .setColor(0x28a745)
        .addFields(
          { name: 'Template', value: templateName, inline: true },
          { name: 'Container ID', value: `\`${created.containerId.slice(0, 12)}\``, inline: true },
          { name: 'Image', value: cfg.image, inline: true }
        );
      return interaction.editReply({ embeds: [embed] });
    } catch (err) {
      return interaction.editReply({ content: `❌ Error: ${err.message}` });
    }
  }
  if (commandName === 'templatelist') {
    try {
      const result = await query('SELECT * FROM templates ORDER BY name, version DESC');
      const embed = new EmbedBuilder().setTitle('Available Templates').setColor(0x3498db);
      if (!result.rows.length) {
        embed.setDescription('No templates defined.');
      } else {
        const seen = new Set();
        for (const t of result.rows) {
          if (seen.has(t.name)) continue;
          seen.add(t.name);
          const cfg = typeof t.config === 'string' ? JSON.parse(t.config) : t.config;
          embed.addFields({
            name: `${t.name} (v${t.version})`,
            value: `Image: ${cfg.image}\nCPU: ${cfg.cpu} | RAM: ${cfg.memory}MB | Storage: ${cfg.storage}GB`,
            inline: false,
          });
        }
      }
      return interaction.reply({ embeds: [embed], ephemeral: true });
    } catch (err) {
      return interaction.reply({ content: `❌ Error: ${err.message}`, ephemeral: true });
    }
  }
  return null;
}

module.exports = { toSpec, isParsed, handle };