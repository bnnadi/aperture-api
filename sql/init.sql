-- Create database if it doesn't exist
CREATE DATABASE IF NOT EXISTS aperture;

-- Connect to the newly created or existing database
USE aperture;

CREATE TABLE IF NOT EXISTS users (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(20) NOT NULL,
  email VARCHAR(50) UNIQUE NOT NULL,
  password VARCHAR(20) NOT NULL,
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS math_history (
  id INT NOT NULL AUTO_INCREMENT,
  user_id INT NOT NULL,
  question VARCHAR(120),
  answer VARCHAR(50),
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id)
);