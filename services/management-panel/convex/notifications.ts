import { query, mutation } from "./_generated/server";
import { v } from "convex/values";

export const getNotifications = query({
  args: { userId: v.id("unifiedProfiles"), unreadOnly: v.optional(v.boolean()) },
  handler: async (ctx, args) => {
    let q = ctx.db
      .query("notifications")
      .filter((q) => q.eq("userId", args.userId));
    
    if (args.unreadOnly) {
      q = q.filter((q) => q.eq("read", false));
    }
    
    return await q.collect();
  },
});

export const createNotification = mutation({
  args: {
    userId: v.id("unifiedProfiles"),
    type: v.string(),
    title: v.string(),
    message: v.string(),
    platforms: v.array(v.string()),
  },
  handler: async (ctx, args) => {
    const notifId = await ctx.db.insert("notifications", {
      ...args,
      read: false,
      createdAt: new Date().toISOString(),
    });
    return notifId;
  },
});

export const markNotificationRead = mutation({
  args: { notifId: v.id("notifications") },
  handler: async (ctx, args) => {
    await ctx.db.patch(args.notifId, { read: true });
  },
});

export const markAllNotificationsRead = mutation({
  args: { userId: v.id("unifiedProfiles") },
  handler: async (ctx, args) => {
    const notifs = await ctx.db
      .query("notifications")
      .filter((q) =>
        q.and(
          q.eq("userId", args.userId),
          q.eq("read", false)
        )
      )
      .collect();
    
    for (const notif of notifs) {
      await ctx.db.patch(notif._id, { read: true });
    }
  },
});

export const deleteNotification = mutation({
  args: { notifId: v.id("notifications") },
  handler: async (ctx, args) => {
    await ctx.db.delete(args.notifId);
  },
});