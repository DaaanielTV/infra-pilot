const { EmbedBuilder, ButtonBuilder, ActionRowBuilder, ButtonStyle, PermissionsBitField } = require('discord.js');

class TicketSystem {
    constructor(client) {
        this.client = client;
        this.tickets = new Map();
        this.ticketCounter = 0;
    }

    async createTicketPanel(channel, options = {}) {
        const embed = new EmbedBuilder()
            .setTitle(options.title || '📝 Support Tickets')
            .setDescription(options.description || 'Click the button below to create a support ticket')
            .setColor(options.color || '#00ff00')
            .setTimestamp();

        const button = new ButtonBuilder()
            .setCustomId('create_ticket')
            .setLabel(options.buttonLabel || 'Create Ticket')
            .setStyle(ButtonStyle.Primary)
            .setEmoji('🎫');

        const row = new ActionRowBuilder().addComponents(button);

        return await channel.send({
            embeds: [embed],
            components: [row]
        });
    }

    async handleTicketCreate(interaction) {
        if (interaction.customId !== 'create_ticket') return;

        const ticketId = ++this.ticketCounter;
        const ticketChannel = await this.createTicketChannel(interaction, ticketId);
        
        if (!ticketChannel) {
            await interaction.reply({
                content: '❌ Failed to create ticket channel. Please contact an administrator.',
                ephemeral: true
            });
            return;
        }

        this.tickets.set(ticketChannel.id, {
            id: ticketId,
            userId: interaction.user.id,
            status: 'open',
            createdAt: new Date(),
            messages: []
        });

        await interaction.reply({
            content: `✅ Ticket created! Please check ${ticketChannel}`,
            ephemeral: true
        });

        await this.sendTicketWelcomeMessage(ticketChannel, interaction.user);
    }

    async createTicketChannel(interaction, ticketId) {
        const guild = interaction.guild;
        const category = await this.getTicketCategory(guild);

        try {
            return await guild.channels.create({
                name: `ticket-${ticketId}`,
                type: 0, // Text channel
                parent: category?.id,
                permissionOverwrites: [
                    {
                        id: guild.id,
                        deny: [PermissionsBitField.Flags.ViewChannel]
                    },
                    {
                        id: interaction.user.id,
                        allow: [
                            PermissionsBitField.Flags.ViewChannel,
                            PermissionsBitField.Flags.SendMessages,
                            PermissionsBitField.Flags.ReadMessageHistory
                        ]
                    },
                    {
                        id: this.client.user.id,
                        allow: [
                            PermissionsBitField.Flags.ViewChannel,
                            PermissionsBitField.Flags.SendMessages,
                            PermissionsBitField.Flags.ReadMessageHistory,
                            PermissionsBitField.Flags.ManageChannels
                        ]
                    }
                ]
            });
        } catch (error) {
            console.error('Error creating ticket channel:', error);
            return null;
        }
    }

    async getTicketCategory(guild) {
        let category = guild.channels.cache.find(c => 
            c.type === 4 && c.name.toLowerCase() === 'tickets'
        );

        if (!category) {
            try {
                category = await guild.channels.create({
                    name: 'Tickets',
                    type: 4
                });
            } catch (error) {
                console.error('Error creating tickets category:', error);
                return null;
            }
        }

        return category;
    }

    async sendTicketWelcomeMessage(channel, user) {
        const embed = new EmbedBuilder()
            .setTitle('🎫 Support Ticket')
            .setDescription(`Hello ${user}, welcome to your support ticket!\nPlease describe your issue and our staff will assist you shortly.`)
            .setColor('#00ff00')
            .setTimestamp();

        const closeButton = new ButtonBuilder()
            .setCustomId('close_ticket')
            .setLabel('Close Ticket')
            .setStyle(ButtonStyle.Danger)
            .setEmoji('🔒');

        const row = new ActionRowBuilder().addComponents(closeButton);

        await channel.send({
            embeds: [embed],
            components: [row]
        });
    }

    async handleTicketClose(interaction) {
        if (interaction.customId !== 'close_ticket') return;

        const ticket = this.tickets.get(interaction.channelId);
        if (!ticket) return;

        // Create transcript
        const messages = await interaction.channel.messages.fetch();
        const transcript = await this.createTranscript(messages);

        // Notify user
        const user = await this.client.users.fetch(ticket.userId);
        if (user) {
            const embed = new EmbedBuilder()
                .setTitle('Ticket Closed')
                .setDescription(`Your ticket #${ticket.id} has been closed.`)
                .setColor('#ff0000')
                .setTimestamp();

            await user.send({ embeds: [embed] }).catch(() => {});
        }

        // Delete channel
        await interaction.channel.delete();
        this.tickets.delete(interaction.channelId);

        // Save transcript to logs channel
        await this.saveTranscript(interaction.guild, ticket, transcript);
    }

    async createTranscript(messages) {
        let transcript = '=== Ticket Transcript ===\n\n';
        
        messages.reverse().forEach(msg => {
            const timestamp = msg.createdAt.toLocaleString();
            transcript += `[${timestamp}] ${msg.author.tag}: ${msg.content}\n`;
            
            msg.attachments.forEach(attachment => {
                transcript += `[Attachment: ${attachment.url}]\n`;
            });
            
            msg.embeds.forEach(embed => {
                transcript += `[Embed: ${embed.title || 'Untitled'}]\n`;
            });
            
            transcript += '\n';
        });
        
        return transcript;
    }

    async saveTranscript(guild, ticket, transcript) {
        const logsChannel = guild.channels.cache.find(c => 
            c.name.toLowerCase() === 'ticket-logs'
        );

        if (logsChannel) {
            const embed = new EmbedBuilder()
                .setTitle(`Ticket #${ticket.id} Transcript`)
                .setDescription('Ticket has been closed and archived')
                .addFields([
                    { name: 'Ticket ID', value: `#${ticket.id}`, inline: true },
                    { name: 'Created By', value: `<@${ticket.userId}>`, inline: true },
                    { name: 'Created At', value: ticket.createdAt.toLocaleString(), inline: true }
                ])
                .setColor('#ff0000')
                .setTimestamp();

            await logsChannel.send({
                embeds: [embed],
                files: [{
                    attachment: Buffer.from(transcript),
                    name: `ticket-${ticket.id}-transcript.txt`
                }]
            });
        }
    }

    async addStaffToTicket(channel, staffMember) {
        await channel.permissionOverwrites.edit(staffMember, {
            ViewChannel: true,
            SendMessages: true,
            ReadMessageHistory: true
        });
    }

    async removeStaffFromTicket(channel, staffMember) {
        await channel.permissionOverwrites.delete(staffMember);
    }
}

module.exports = TicketSystem;