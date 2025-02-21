DROP DATABASE IF EXISTS examen_ruben;
CREATE DATABASE examen_ruben;
USE examen_ruben;

CREATE TABLE users (
    id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255),
    password VARCHAR(255),
    fullname VARCHAR(255)
);

CREATE TABLE contacts (
    id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    fullname VARCHAR(255),
    number VARCHAR(255),
    email VARCHAR(255),
    user_id INT UNSIGNED,
    FOREIGN KEY (user_id) REFERENCES users(id)
);