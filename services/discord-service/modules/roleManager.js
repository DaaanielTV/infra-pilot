const { EmbedBuilder, PermissionsBitField } = require('discord.js');

class RoleManager {
    constructor(client) {
        this.client = client;
        this.roleMenus = new Map();
    }

    async createRoleMenu(channel, options) {
        const embed = new EmbedBuilder()
            .setTitle('Role Selection Menu')
            .setDescription('React with the emojis below to get or remove roles!')
            .setColor('#00ff00')
            .setTimestamp();

        const roleFields = options.map((option, index) => ({
            name: `${option.emoji} ${option.role.name}`,
            value: option.description || 'Click the reaction to toggle this role',
            inline: true
        }));

        embed.addFields(roleFields);

        const message = await channel.send({ embeds: [embed] });
        
        // Add reactions
        for (const option of options) {
            await message.react(option.emoji);
        }

        // Store role menu configuration
        this.roleMenus.set(message.id, {
            roles: options.map(opt => ({
                emoji: opt.emoji,
                roleId: opt.role.id
            }))
        });

        return message;
    }

    async handleReaction(reaction, user, added) {
        if (user.bot) return;

        const menuConfig = this.roleMenus.get(reaction.message.id);
        if (!menuConfig) return;

        const roleConfig = menuConfig.roles.find(r => r.emoji === reaction.emoji.name);
        if (!roleConfig) return;

        const guild = reaction.message.guild;
        const member = await guild.members.fetch(user.id);
        const role = guild.roles.cache.get(roleConfig.roleId);

        if (!role) {
            console.error(`Role ${roleConfig.roleId} not found`);
            return;
        }

        try {
            if (added) {
                if (!member.roles.cache.has(role.id)) {
                    await member.roles.add(role);
                    await this.sendRoleUpdateMessage(member, role, true);
                }
            } else {
                if (member.roles.cache.has(role.id)) {
                    await member.roles.remove(role);
                    await this.sendRoleUpdateMessage(member, role, false);
                }
            }
        } catch (error) {
            console.error('Error updating roles:', error);
            await user.send('There was an error updating your roles. Please contact an administrator.').catch(() => {});
        }
    }

    async sendRoleUpdateMessage(member, role, added) {
        const embed = new EmbedBuilder()
            .setTitle('Role Update')
            .setDescription(`${added ? '✅ Added' : '❌ Removed'} role: ${role.name}`)
            .setColor(added ? '#00ff00' : '#ff0000')
            .setTimestamp();

        try {
            await member.send({ embeds: [embed] });
        } catch (error) {
            // User might have DMs disabled, ignore
        }
    }

    async createCustomRole(guild, options) {
        try {
            const role = await guild.roles.create({
                name: options.name,
                color: options.color || '#000000',
                permissions: options.permissions || [],
                reason: options.reason || 'Custom role created through role manager'
            });

            return role;
        } catch (error) {
            console.error('Error creating custom role:', error);
            throw error;
        }
    }

    async editRole(role, options) {
        try {
            await role.edit({
                name: options.name,
                color: options.color,
                permissions: options.permissions,
                reason: options.reason || 'Role edited through role manager'
            });

            return role;
        } catch (error) {
            console.error('Error editing role:', error);
            throw error;
        }
    }

    async getGuildRoleInfo(guild) {
        const roles = await guild.roles.fetch();
        const totalRoles = roles.size;
        const managedRoles = roles.filter(role => role.managed).size;
        const customRoles = totalRoles - managedRoles;

        const embed = new EmbedBuilder()
            .setTitle('Guild Role Information')
            .setColor('#00ff00')
            .addFields([
                { name: 'Total Roles', value: totalRoles.toString(), inline: true },
                { name: 'Custom Roles', value: customRoles.toString(), inline: true },
                { name: 'Managed Roles', value: managedRoles.toString(), inline: true }
            ])
            .setTimestamp();

        return embed;
    }

    validateRoleHierarchy(member, role) {
        // Check if the member has permission to manage this role
        if (!member.permissions.has(PermissionsBitField.Flags.ManageRoles)) {
            return false;
        }

        // Check if the member's highest role is higher than the target role
        return member.roles.highest.position > role.position;
    }

    async bulkAssignRole(role, members, reason = 'Bulk role assignment') {
        const results = {
            successful: [],
            failed: []
        };

        for (const member of members) {
            try {
                await member.roles.add(role, reason);
                results.successful.push(member.id);
            } catch (error) {
                results.failed.push({
                    memberId: member.id,
                    error: error.message
                });
            }
        }

        return results;
    }
}

module.exports = RoleManager;