const fs = require('fs');
const path = require('path');
const { Pool } = require('pg');

const SERVER_LIMITS_FILE = path.join(__dirname, '..', 'server_limits.json');
let _dbPool = null;

async function _getDbPool() {
  if (!_dbPool) {
    _dbPool = new Pool({
      host: process.env.DB_HOST || 'localhost',
      port: parseInt(process.env.DB_PORT, 10) || 5432,
      user: process.env.DB_USER || 'infra_pilot',
      password: process.env.DB_PASSWORD || '',
      database: process.env.DB_NAME || 'infra_pilot',
      max: 5,
    });
    try {
      await _dbPool.query(`
        CREATE TABLE IF NOT EXISTS server_limits (
          user_id VARCHAR(255) NOT NULL,
          server_identifier VARCHAR(255) NOT NULL,
          created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
          PRIMARY KEY (user_id, server_identifier)
        )
      `);
    } catch (err) {
      console.error('[DB] server_limits table setup failed:', err.message);
    }
  }
  return _dbPool;
}

async function loadServerLimits() {
  try {
    const pool = await _getDbPool();
    const result = await pool.query(
      'SELECT user_id, server_identifier FROM server_limits'
    );
    const limits = {};
    for (const row of result.rows) {
      if (!limits[row.user_id]) limits[row.user_id] = [];
      limits[row.user_id].push(row.server_identifier);
    }
    return limits;
  } catch (error) {
    console.error('[ServerLimits] DB load failed, trying JSON fallback:', error.message);
  }
  try {
    if (!fs.existsSync(SERVER_LIMITS_FILE)) {
      fs.writeFileSync(SERVER_LIMITS_FILE, JSON.stringify({}));
    }
    return JSON.parse(fs.readFileSync(SERVER_LIMITS_FILE, 'utf8'));
  } catch (error) {
    console.error('[ServerLimits] JSON fallback also failed:', error);
    return {};
  }
}

async function saveServerLimits(userId, serverIdentifier) {
  try {
    const pool = await _getDbPool();
    await pool.query(
      'INSERT INTO server_limits (user_id, server_identifier) VALUES ($1, $2) ON CONFLICT DO NOTHING',
      [userId, serverIdentifier]
    );
  } catch (error) {
    console.error('[ServerLimits] DB save failed, using JSON fallback:', error.message);
    try {
      let limits = {};
      if (fs.existsSync(SERVER_LIMITS_FILE)) {
        limits = JSON.parse(fs.readFileSync(SERVER_LIMITS_FILE, 'utf8'));
      }
      if (!limits[userId]) limits[userId] = [];
      limits[userId].push(serverIdentifier);
      fs.writeFileSync(SERVER_LIMITS_FILE, JSON.stringify(limits, null, 2));
    } catch (fsError) {
      console.error('[ServerLimits] JSON fallback save failed:', fsError.message);
    }
  }
}

module.exports = { loadServerLimits, saveServerLimits };
