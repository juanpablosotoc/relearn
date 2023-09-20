DROP DATABASE IF EXISTS wayne_foundation;
CREATE DATABASE wayne_foundation;
USE wayne_foundation;
CREATE TABLE currencies (
name VARCHAR(50) NOT NULL,
symbol CHAR(1) NOT NULL,
PRIMARY KEY (name)
);
INSERT INTO currencies
VALUES ('Euro', '€'), ('US dollar', '$'), ('MX peso', '$');
CREATE TABLE users (
id INT UNSIGNED AUTO_INCREMENT NOT NULL, 
company_name VARCHAR(50) NOT NULL,
password VARCHAR(50) NOT NULL,
currency VARCHAR(50) NOT NULL,
PRIMARY KEY (id),
FOREIGN KEY (currency) REFERENCES currencies (name)
);
CREATE TABLE statement_types (
statement_id VARCHAR(50) NOT NULL,
PRIMARY KEY (statement_id)
);
INSERT INTO statement_types
VALUES ('Ventas', 'Descuento sobre ventas', 'Costo', 'Préstamo Largo plazo', '');
CREATE TABLE users_data (
user_id INT UNSIGNED AUTO_INCREMENT NOT NULL,
statement_id VARCHAR(50) NOT NULL,
amount BIGINT NOT NULL,
PRIMARY KEY (user_id, statement_id),
FOREIGN KEY (user_id) REFERENCES users (id),
FOREIGN KEY (statement_id) REFERENCES statement_types(statement_id)
);
