-- This script creates a new user in a database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Creating a new user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Granting all privileges on the database
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- Granting SELECT privileges on the database
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
