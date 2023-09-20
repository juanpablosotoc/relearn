DROP DATABASE IF EXISTS wayne_foundation;
CREATE DATABASE wayne_foundation;
USE wayne_foundation;
CREATE TABLE users (
id INT UNSIGNED NOT NULL,
email VARCHAR(50) NOT NULL,
password VARCHAR(50) NOT NULL,
PRIMARY KEY (id)
); 
CREATE TABLE data (
user_id INT UNSIGNED NOT NULL,
costo INT,
venta INT,
PRIMARY KEY (user_id)
);

