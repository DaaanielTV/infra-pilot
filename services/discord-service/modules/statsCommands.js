const { SlashCommandBuilder } = require('@discordjs/builders');
const { EmbedBuilder } = require('discord.js');
const mysql = require('mysql2/promise');
require('dotenv').config();

class StatsCommands {
    constructor(client) {
        this.client = client;
        this.db = null;
        this.initializeDatabase();
    }

    async initializeDatabase() {
        this.db = await mysql.createConnection({
            host: process.env.DB_HOST,
            user: process.env.DB_USER,
            password: process.env.DB_PASSWORD,
            database: process.env.DB_NAME
        });
    }

    registerCommands() {
        return [
            new SlashCommandBuilder()
                .setName('serverstats')
                .setDescription('View your Minecraft server statistics')
                .addUserOption(option =>
                    option.setName('player')
                        .setDescription('Player to check stats for (staff only)')
                        .setRequired(false)),

            new SlashCommandBuilder()
                .setName('leaderboard')
                .setDescription('View server statistics leaderboard')
                .addStringOption(option =>
                    option.setName('category')
                        .setDescription('Leaderboard category')
                        .setRequired(true)
                        .addChoices(
                            { name: 'Players', value: 'players' },
                            { name: 'Uptime', value: 'uptime' },
                            { name: 'Playtime', value: 'playtime' }
                        ))
        ];
    }

    async handleServerStats(interaction) {
        await interaction.deferReply();
        
        const targetUser = interaction.options.getUser('player');
        const isStaff = interaction.member.roles.cache.some(role => 
            role.name.toLowerCase().includes('staff') || role.name.toLowerCase().includes('admin')
        );

        if (targetUser && !isStaff) {
            return interaction.editReply({
                content: '❌ Only staff members can view other players\' statistics.',
                ephemeral: true
            });
        }

        const userId = targetUser ? targetUser.id : interaction.user.id;

        try {
            const [rows] = await this.db.execute(
                'SELECT * FROM player_statistics WHERE uuid = ?',
                [userId]
            );

            if (rows.length === 0) {
                return interaction.editReply({
                    content: targetUser ? 
                        `❌ No server statistics found for ${targetUser.username}` :
                        '❌ You don\'t have any server statistics yet.',
                    ephemeral: true
                });
            }

            const stats = rows[0];
            const embed = new EmbedBuilder()
                .setTitle(`${targetUser ? targetUser.username + '\'s' : 'Your'} Server Statistics`)
                .setColor('#00ff00')
                .setTimestamp();

            // Format statistics for display
            embed.addFields([
                {
                    name: '📊 Current Status',
                    value: `Server: ${stats.current_status}\nPlayers: ${stats.current_players}\nTPS: ${stats.current_tps.toFixed(2)}`,
                    inline: false
                },
                {
                    name: '⚡ Peak Statistics',
                    value: `Players: ${stats.peak_players}\nMemory: ${this.formatBytes(stats.peak_memory_usage)}\nCPU: ${stats.peak_cpu_usage.toFixed(1)}%`,
                    inline: true
                },
                {
                    name: '⏰ Time Statistics',
                    value: `Total Playtime: ${this.formatTime(stats.total_playtime)}\nUptime: ${stats.uptime_percentage.toFixed(1)}%`,
                    inline: true
                },
                {
                    name: '🔄 Server Events',
                    value: `Total Restarts: ${stats.total_restarts}`,
                    inline: true
                }
            ]);

            await interaction.editReply({ embeds: [embed] });

        } catch (error) {
            console.error('Error fetching server statistics:', error);
            await interaction.editReply({
                content: '❌ An error occurred while fetching server statistics.',
                ephemeral: true
            });
        }
    }

    async handleLeaderboard(interaction) {
        await interaction.deferReply();

        const category = interaction.options.getString('category');
        let query = '';
        let title = '';

        switch (category) {
            case 'players':
                query = 'SELECT uuid, peak_players FROM player_statistics ORDER BY peak_players DESC LIMIT 10';
                title = '👥 Top Servers by Peak Players';
                break;
            case 'uptime':
                query = 'SELECT uuid, uptime_percentage FROM player_statistics ORDER BY uptime_percentage DESC LIMIT 10';
                title = '⚡ Top Servers by Uptime';
                break;
            case 'playtime':
                query = 'SELECT uuid, total_playtime FROM player_statistics ORDER BY total_playtime DESC LIMIT 10';
                title = '⏰ Top Servers by Playtime';
                break;
        }

        try {
            const [rows] = await this.db.execute(query);
            
            if (rows.length === 0) {
                return interaction.editReply('No statistics available for the leaderboard.');
            }

            const embed = new EmbedBuilder()
                .setTitle(title)
                .setColor('#ffd700')
                .setTimestamp();

            let description = '';
            for (let i = 0; i < rows.length; i++) {
                const user = await this.client.users.fetch(rows[i].uuid).catch(() => null);
                const username = user ? user.username : 'Unknown User';
                
                let value = '';
                switch (category) {
                    case 'players':
                        value = `${rows[i].peak_players} players`;
                        break;
                    case 'uptime':
                        value = `${rows[i].uptime_percentage.toFixed(1)}% uptime`;
                        break;
                    case 'playtime':
                        value = this.formatTime(rows[i].total_playtime);
                        break;
                }

                description += `${i + 1}. ${username} - ${value}\n`;
            }

            embed.setDescription(description);
            await interaction.editReply({ embeds: [embed] });

        } catch (error) {
            console.error('Error fetching leaderboard:', error);
            await interaction.editReply({
                content: '❌ An error occurred while fetching the leaderboard.',
                ephemeral: true
            });
        }
    }

    formatBytes(bytes) {
        const sizes = ['B', 'KB', 'MB', 'GB', 'TB'];
        if (bytes === 0) return '0 B';
        const i = parseInt(Math.floor(Math.log(bytes) / Math.log(1024)), 10);
        return `${(bytes / (1024 ** i)).toFixed(1)} ${sizes[i]}`;
    }

    formatTime(hours) {
        const days = Math.floor(hours / 24);
        const remainingHours = hours % 24;
        
        if (days > 0) {
            return `${days}d ${remainingHours}h`;
        }
        return `${hours}h`;
    }
}

module.exports = StatsCommands;