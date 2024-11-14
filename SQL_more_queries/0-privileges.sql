-- Check if user_0d_1 exists and create if not
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
-- Check if user_0d_2 exists and create if not
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';

-- Grant root privileges to user_0d_1
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Grant specific privileges (SELECT and INSERT on user_2_db) to user_0d_2
GRANT SELECT, INSERT ON user_2_db.* TO 'user_0d_2'@'localhost';

-- Apply changes
FLUSH PRIVILEGES;

-- Display grants for user_0d_1
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Display grants for user_0d_2
SHOW GRANTS FOR 'user_0d_2'@'localhost';

