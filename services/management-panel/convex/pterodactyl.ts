import { v } from "convex/values";
import { action, mutation, query } from "./_generated/server";
import { getAuthUserId } from "@convex-dev/auth/server";
import axios from "axios";
import { api } from "./_generated/api";
import { Doc, Id } from "./_generated/dataModel";

type PterodactylConfig = {
  _id: Id<"pterodactylConfig">;
  _creationTime: number;
  apiKey: string;
  panelUrl: string;
  userId: Id<"users">;
};

type PterodactylServer = {
  attributes: {
    name: string;
    identifier: string;
    status: string;
  };
};

type PterodactylResponse = {
  data: PterodactylServer[];
};

export const saveConfig = mutation({
  args: {
    apiKey: v.string(),
    panelUrl: v.string(),
  },
  handler: async (ctx, args) => {
    const userId = await getAuthUserId(ctx);
    if (!userId) throw new Error("Not authenticated");

    await ctx.db.insert("pterodactylConfig", {
      apiKey: args.apiKey,
      panelUrl: args.panelUrl,
      userId,
    });
  },
});

export const getConfig = query({
  args: {},
  handler: async (ctx): Promise<PterodactylConfig | null> => {
    const userId = await getAuthUserId(ctx);
    if (!userId) return null;

    const config = await ctx.db
      .query("pterodactylConfig")
      .withIndex("by_user", (q) => q.eq("userId", userId))
      .first();
    return config;
  },
});

export const fetchServers = action({
  args: {},
  handler: async (ctx): Promise<PterodactylResponse> => {
    const config = await ctx.runQuery(api.pterodactyl.getConfig);
    if (!config) throw new Error("Pterodactyl not configured");

    try {
      const response = await axios.get<PterodactylResponse>(`${config.panelUrl}/api/client`, {
        headers: {
          'Authorization': `Bearer ${config.apiKey}`,
          'Accept': 'Application/vnd.pterodactyl.v1+json',
        },
      });

      await ctx.runMutation(api.pterodactyl.updateServers, {
        servers: response.data.data.map((server) => ({
          name: server.attributes.name,
          serverId: server.attributes.identifier,
          status: server.attributes.status,
        })),
      });

      return response.data;
    } catch (error) {
      throw new Error("Failed to fetch servers");
    }
  },
});

export const updateServers = mutation({
  args: {
    servers: v.array(
      v.object({
        name: v.string(),
        serverId: v.string(),
        status: v.string(),
      })
    ),
  },
  handler: async (ctx, args) => {
    const userId = await getAuthUserId(ctx);
    if (!userId) throw new Error("Not authenticated");

    // Clear existing servers
    const existing = await ctx.db
      .query("servers")
      .withIndex("by_user", (q) => q.eq("userId", userId))
      .collect();
    
    for (const server of existing) {
      await ctx.db.delete(server._id);
    }

    // Insert new servers
    for (const server of args.servers) {
      await ctx.db.insert("servers", {
        ...server,
        userId,
      });
    }
  },
});

export const listServers = query({
  args: {},
  handler: async (ctx) => {
    const userId = await getAuthUserId(ctx);
    if (!userId) return [];

    return await ctx.db
      .query("servers")
      .withIndex("by_user", (q) => q.eq("userId", userId))
      .collect();
  },
});
