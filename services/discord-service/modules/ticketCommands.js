const { SlashCommandBuilder } = require('@discordjs/builders');
const { PermissionFlagsBits } = require('discord.js');

class TicketCommands {
    constructor(ticketSystem) {
        this.ticketSystem = ticketSystem;
        this.commands = this.createCommands();
    }

    createCommands() {
        return [
            new SlashCommandBuilder()
                .setName('setuptickets')
                .setDescription('Set up the ticket system in the current channel')
                .setDefaultMemberPermissions(PermissionFlagsBits.Administrator),

            new SlashCommandBuilder()
                .setName('addstaff')
                .setDescription('Add a staff member to the current ticket')
                .addUserOption(option =>
                    option.setName('user')
                        .setDescription('The staff member to add')
                        .setRequired(true)
                )
                .setDefaultMemberPermissions(PermissionFlagsBits.ManageChannels),

            new SlashCommandBuilder()
                .setName('removestaff')
                .setDescription('Remove a staff member from the current ticket')
                .addUserOption(option =>
                    option.setName('user')
                        .setDescription('The staff member to remove')
                        .setRequired(true)
                )
                .setDefaultMemberPermissions(PermissionFlagsBits.ManageChannels),

            new SlashCommandBuilder()
                .setName('ticketstats')
                .setDescription('View ticket statistics')
                .setDefaultMemberPermissions(PermissionFlagsBits.ManageChannels)
        ].map(command => command.toJSON());
    }

    async handleCommand(interaction) {
        if (!interaction.isCommand()) return;

        switch (interaction.commandName) {
            case 'setuptickets':
                await this.handleSetupCommand(interaction);
                break;
            case 'addstaff':
                await this.handleAddStaffCommand(interaction);
                break;
            case 'removestaff':
                await this.handleRemoveStaffCommand(interaction);
                break;
            case 'ticketstats':
                await this.handleStatsCommand(interaction);
                break;
        }
    }

    async handleSetupCommand(interaction) {
        await interaction.deferReply({ ephemeral: true });

        try {
            await this.ticketSystem.createTicketPanel(interaction.channel, {
                title: '🎫 Support Tickets',
                description: 'Need help? Click the button below to create a support ticket!\n\nOur staff team will assist you as soon as possible.',
                buttonLabel: 'Open Ticket'
            });

            await interaction.editReply({
                content: '✅ Ticket system has been set up successfully!',
                ephemeral: true
            });
        } catch (error) {
            console.error('Error setting up ticket system:', error);
            await interaction.editReply({
                content: '❌ Failed to set up the ticket system. Please check the bot permissions and try again.',
                ephemeral: true
            });
        }
    }

    async handleAddStaffCommand(interaction) {
        if (!interaction.channel.name.startsWith('ticket-')) {
            await interaction.reply({
                content: '❌ This command can only be used in ticket channels!',
                ephemeral: true
            });
            return;
        }

        const staffMember = interaction.options.getUser('user');
        if (!staffMember) return;

        try {
            await this.ticketSystem.addStaffToTicket(interaction.channel, staffMember);
            await interaction.reply({
                content: `✅ Added ${staffMember} to the ticket.`,
                ephemeral: true
            });
        } catch (error) {
            console.error('Error adding staff to ticket:', error);
            await interaction.reply({
                content: '❌ Failed to add staff member to the ticket.',
                ephemeral: true
            });
        }
    }

    async handleRemoveStaffCommand(interaction) {
        if (!interaction.channel.name.startsWith('ticket-')) {
            await interaction.reply({
                content: '❌ This command can only be used in ticket channels!',
                ephemeral: true
            });
            return;
        }

        const staffMember = interaction.options.getUser('user');
        if (!staffMember) return;

        try {
            await this.ticketSystem.removeStaffFromTicket(interaction.channel, staffMember);
            await interaction.reply({
                content: `✅ Removed ${staffMember} from the ticket.`,
                ephemeral: true
            });
        } catch (error) {
            console.error('Error removing staff from ticket:', error);
            await interaction.reply({
                content: '❌ Failed to remove staff member from the ticket.',
                ephemeral: true
            });
        }
    }

    async handleStatsCommand(interaction) {
        await interaction.deferReply();

        const stats = {
            total: this.ticketSystem.ticketCounter,
            open: Array.from(this.ticketSystem.tickets.values()).filter(t => t.status === 'open').length,
            closed: this.ticketSystem.ticketCounter - Array.from(this.ticketSystem.tickets.values()).filter(t => t.status === 'open').length
        };

        const fields = [
            { name: 'Total Tickets', value: stats.total.toString(), inline: true },
            { name: 'Open Tickets', value: stats.open.toString(), inline: true },
            { name: 'Closed Tickets', value: stats.closed.toString(), inline: true }
        ];

        await interaction.editReply({
            embeds: [{
                title: '📊 Ticket Statistics',
                fields,
                color: 0x00ff00,
                timestamp: new Date()
            }]
        });
    }
}

module.exports = TicketCommands;