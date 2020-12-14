CREATE TABLE IF NOT EXISTS warns (
    user_id int,
    guild_id,
    reason TEXT,
    warned_at NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS economy (
    guild_id int,
    user_id int,
    bank int DEFAULT 0,
    purse DEFAULT 0
);