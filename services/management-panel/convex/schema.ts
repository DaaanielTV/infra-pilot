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
};

export default defineSchema({
  ...authTables,
  ...applicationTables,
});
