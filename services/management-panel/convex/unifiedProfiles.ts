import { query, mutation } from "./_generated/server";
import { v } from "convex/values";

export const getUnifiedProfile = query({
  args: { email: v.string() },
  handler: async (ctx, args) => {
    const profiles = await ctx.db
      .query("unifiedProfiles")
      .filter((q) => q.eq("email", args.email))
      .first();
    return profiles;
  },
});

export const listUnifiedProfiles = query({
  handler: async (ctx) => {
    return await ctx.db.query("unifiedProfiles").collect();
  },
});

export const createUnifiedProfile = mutation({
  args: {
    email: v.string(),
    discordId: v.optional(v.string()),
    serviceCoreId: v.optional(v.string()),
    displayName: v.string(),
    avatarUrl: v.optional(v.string()),
    roles: v.array(v.string()),
  },
  handler: async (ctx, args) => {
    const profileId = await ctx.db.insert("unifiedProfiles", {
      ...args,
      lastSynced: new Date().toISOString(),
    });
    return profileId;
  },
});

export const syncUnifiedProfile = mutation({
  args: {
    email: v.string(),
    platform: v.string(),
    platformUserId: v.string(),
  },
  handler: async (ctx, args) => {
    const existing = await ctx.db
      .query("unifiedProfiles")
      .filter((q) => q.eq("email", args.email))
      .first();

    if (!existing) {
      throw new Error("Profile not found");
    }

    const updates: Record<string, string> = {
      lastSynced: new Date().toISOString(),
    };

    if (args.platform === "discord") {
      updates.discordId = args.platformUserId;
    } else if (args.platform === "service_core") {
      updates.serviceCoreId = args.platformUserId;
    }

    await ctx.db.patch(existing._id, updates);
    return existing._id;
  },
});

export const updateUnifiedProfile = mutation({
  args: {
    profileId: v.id("unifiedProfiles"),
    displayName: v.optional(v.string()),
    avatarUrl: v.optional(v.string()),
    roles: v.optional(v.array(v.string())),
  },
  handler: async (ctx, args) => {
    const { profileId, ...updates } = args;
    await ctx.db.patch(profileId, updates);
    return profileId;
  },
});