CREATE DATABASE Ferreteria_db;
USE Ferreteria_db;

CREATE TABLE usuarios(
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(50) NOT NULL,
    contraseña VARCHAR(50) NOT NULL,
    rol VARCHAR(20) NOT NULL
);

CREATE TABLE productos(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);


INSERT INTO usuarios(usuario, contraseña, rol)
VALUES
('admin', '1234', 'administrador'),
('carlos', '1234', 'usuario');