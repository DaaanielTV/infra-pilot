import { query, mutation } from "./_generated/server";
import { v } from "convex/values";

export const getSharedConfig = query({
  args: { key: v.optional(v.string()) },
  handler: async (ctx, args) => {
    if (args.key) {
      const config = await ctx.db
        .query("sharedConfig")
        .filter((q) => q.eq("key", args.key!))
        .first();
      return config;
    }
    return await ctx.db.query("sharedConfig").collect();
  },
});

export const setSharedConfig = mutation({
  args: {
    key: v.string(),
    value: v.any(),
  },
  handler: async (ctx, args) => {
    const existing = await ctx.db
      .query("sharedConfig")
      .filter((q) => q.eq("key", args.key))
      .first();

    if (existing) {
      await ctx.db.patch(existing._id, {
        value: args.value,
        updatedAt: new Date().toISOString(),
      });
      return existing._id;
    }

    const configId = await ctx.db.insert("sharedConfig", {
      key: args.key,
      value: args.value,
      updatedAt: new Date().toISOString(),
    });
    return configId;
  },
});

export const deleteSharedConfig = mutation({
  args: { key: v.string() },
  handler: async (ctx, args) => {
    const config = await ctx.db
      .query("sharedConfig")
      .filter((q) => q.eq("key", args.key))
      .first();
    
    if (config) {
      await ctx.db.delete(config._id);
    }
  },
});