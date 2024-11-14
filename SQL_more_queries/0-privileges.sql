-- Create user_0d_1 if it doesn't exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
-- Grant root privileges to user_0d_1
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Create user_0d_2 if it doesn't exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';
-- Grant specific privileges (SELECT and INSERT on user_2_db) to user_0d_2
GRANT SELECT, INSERT ON user_2_db.* TO 'user_0d_2'@'localhost';

-- Apply the privilege changes
FLUSH PRIVILEGES;

-- Show privileges for user_0d_1 if the user exists
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Show privileges for user_0d_2 if the user exists
SHOW GRANTS FOR 'user_0d_2'@'localhost';

