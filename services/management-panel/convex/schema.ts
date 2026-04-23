import { defineSchema, defineTable } from "convex/server";
import { authTables } from "@convex-dev/auth/server";
import { v } from "convex/values";

const applicationTables = {
  pterodactylConfig: defineTable({
    apiKey: v.string(),
    panelUrl: v.string(),
    userId: v.id("users"),
  }).index("by_user", ["userId"]),
  servers: defineTable({
    name: v.string(),
    serverId: v.string(),
    status: v.string(),
    userId: v.id("users"),
  }).index("by_user", ["userId"]),
  // Unified User Profiles - Cross-platform sync
  unifiedProfiles: defineTable({
    email: v.string(),
    discordId: v.optional(v.string()),
    serviceCoreId: v.optional(v.string()),
    displayName: v.string(),
    avatarUrl: v.optional(v.string()),
    roles: v.array(v.string()),
    lastSynced: v.string(),
  }).index("by_email", ["email"]),
  // Unified Permissions
  permissions: defineTable({
    userId: v.id("unifiedProfiles"),
    resource: v.string(),
    action: v.string(),
    granted: v.boolean(),
  }).index("by_user", ["userId"]),
  // Cross-platform notifications
  notifications: defineTable({
    userId: v.id("unifiedProfiles"),
    type: v.string(),
    title: v.string(),
    message: v.string(),
    platforms: v.array(v.string()),
    read: v.boolean(),
    createdAt: v.string(),
  }).index("by_user", ["userId"]),
  // Shared configuration
  sharedConfig: defineTable({
    key: v.string(),
    value: v.any(),
    updatedAt: v.string(),
  }).index("by_key", ["key"]),
};

export default defineSchema({
  ...authTables,
  ...applicationTables,
});
