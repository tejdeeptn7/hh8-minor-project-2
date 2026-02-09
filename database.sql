CREATE DATABASE iam_rbac;
USE iam_rbac;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE roles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    role_name VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE user_roles (
    user_id INT,
    role_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (role_id) REFERENCES roles(id)
);

--roles
INSERT INTO roles (role_name) VALUES ('admin'), ('manager'), ('user');

--Sample users (password = 1234)
INSERT INTO users (username, password) VALUES ('admin1','1234'), ('user1','1234');

--Assign roles
INSERT INTO user_roles VALUES (1,1); -- admin
INSERT INTO user_roles VALUES (2,3); -- user
