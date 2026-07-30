const axios = require('axios');

const PTERODACTYL_API_URL = process.env.PTERODACTYL_API_URL;
const PTERODACTYL_API_KEY = process.env.PTERODACTYL_API_KEY;

if (!PTERODACTYL_API_URL || !PTERODACTYL_API_KEY) {
  throw new Error(
    `Missing required Pterodactyl configuration: ${!PTERODACTYL_API_URL ? 'PTERODACTYL_API_URL ' : ''}${!PTERODACTYL_API_KEY ? 'PTERODACTYL_API_KEY' : ''}`
  );
}

const pterodactylClient = axios.create({
  baseURL: PTERODACTYL_API_URL,
  timeout: 30000,
  headers: {
    'Authorization': `Bearer ${PTERODACTYL_API_KEY}`,
    'Content-Type': 'application/json',
    'Accept': 'application/json'
  }
});

async function createUser(userData) {
  const response = await pterodactylClient.post('/api/application/users', userData);
  if (!response.data || !response.data.attributes || !response.data.attributes.id) {
    throw new Error('Invalid response from Pterodactyl API: missing user identifier');
  }
  return response.data.attributes;
}

async function createServer(serverData) {
  const response = await pterodactylClient.post('/api/application/servers', serverData);
  if (!response.data || !response.data.attributes || !response.data.attributes.identifier) {
    throw new Error('Invalid response from Pterodactyl API: missing server identifier');
  }
  return response.data.attributes;
}

module.exports = { createUser, createServer };
