import { query, mutation } from "./_generated/server";
import { v } from "convex/values";

export const getPermissions = query({
  args: { userId: v.id("unifiedProfiles") },
  handler: async (ctx, args) => {
    return await ctx.db
      .query("permissions")
      .filter((q) => q.eq("userId", args.userId))
      .collect();
  },
});

export const checkPermission = query({
  args: {
    userId: v.id("unifiedProfiles"),
    resource: v.string(),
    action: v.string(),
  },
  handler: async (ctx, args) => {
    const perms = await ctx.db
      .query("permissions")
      .filter((q) =>
        q.and(
          q.eq("userId", args.userId),
          q.eq("resource", args.resource),
          q.eq("action", args.action)
        )
      )
      .first();
    return perms?.granted ?? false;
  },
});

export const grantPermission = mutation({
  args: {
    userId: v.id("unifiedProfiles"),
    resource: v.string(),
    action: v.string(),
    granted: v.boolean(),
  },
  handler: async (ctx, args) => {
    const permId = await ctx.db.insert("permissions", args);
    return permId;
  },
});

export const revokePermission = mutation({
  args: { permId: v.id("permissions") },
  handler: async (ctx, args) => {
    await ctx.db.delete(args.permId);
  },
});