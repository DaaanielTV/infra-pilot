const { Pool } = require('pg');

let _dbPool = null;
let _dbInitPromise = null;

async function _getDbPool() {
  if (_dbInitPromise) return _dbInitPromise;
  _dbInitPromise = (async () => {
    const dbPassword = process.env.DB_PASSWORD;
    if (!dbPassword) {
      throw new Error('DB_PASSWORD is required');
    }
    const pool = new Pool({
      host: process.env.DB_HOST || 'localhost',
      port: parseInt(process.env.DB_PORT, 10) || 5432,
      user: process.env.DB_USER || 'infra_pilot',
      password: dbPassword,
      database: process.env.DB_NAME || 'infra_pilot',
      max: 5,
      ssl: process.env.DB_SSL === 'true' ? { rejectUnauthorized: true } : false,
    });
    pool.on('error', (err) => {
      console.error('[DB] Idle client error:', err.message);
    });
    try {
      await pool.query(`
        CREATE TABLE IF NOT EXISTS server_limits (
          user_id VARCHAR(255) NOT NULL,
          server_identifier VARCHAR(255) NOT NULL,
          created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
          PRIMARY KEY (user_id, server_identifier)
        )
      `);
    } catch (err) {
      _dbInitPromise = null;
      await pool.end().catch(() => {});
      throw err;
    }
    _dbPool = pool;
    return pool;
  })();
  return _dbInitPromise;
}

async function loadServerLimits() {
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
}

async function saveServerLimits(userId, serverIdentifier) {
  const pool = await _getDbPool();
  await pool.query(
    'INSERT INTO server_limits (user_id, server_identifier) VALUES ($1, $2) ON CONFLICT DO NOTHING',
    [userId, serverIdentifier]
  );
}

module.exports = { loadServerLimits, saveServerLimits };
