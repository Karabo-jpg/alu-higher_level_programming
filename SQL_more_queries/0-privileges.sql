-- Create user_0d_1 if it doesn't exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
-- Grant all privileges to user_0d_1
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Create user_0d_2 if it doesn't exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';
-- Grant SELECT and INSERT privileges to user_0d_2 on database user_2_db
GRANT SELECT, INSERT ON user_2_db.* TO 'user_0d_2'@'localhost';

-- Apply the privilege changes
FLUSH PRIVILEGES;

-- Show privileges for user_0d_1
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Show privileges for user_0d_2
SHOW GRANTS FOR 'user_0d_2'@'localhost';

