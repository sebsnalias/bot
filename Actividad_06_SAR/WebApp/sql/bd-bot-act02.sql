CREATE DATABASE brawlbot;

USE brawlbot;

CREATE TABLE jugadores(
    numero int NOT NULL PRIMARY KEY,
    nombre varchar(50) NOT NULL,
    pais varchar(30) NOT NULL,
    posicion varchar(30) NOT NULL,
    equipo varchar(50) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


INSERT INTO jugadores (numero, nombre, pais, posicion, equipo) VALUES 
(1, 'Nitta', 'Africa', 'Cazador', 'serpientes'),
(2, 'El Primo ', 'Mexico', 'Guerrero', 'Luchadores'),
(3, 'Bull', 'EUA', 'Arquero', 'serpientes');

SHOW TABLES;
DESCRIBE jugadores;

SELECT * FROM jugadores;

CREATE USER 'brawlbot1'@'localhost' IDENTIFIED BY 'brawlbot.2019';
GRANT ALL PRIVILEGES ON brawlbot.* TO 'brawlbot1'@'localhost';
FLUSH PRIVILEGES;
