drop DATABASE if exists juego;

create DATABASE juego;

use juego;

create table jugadores(
    idJ int auto_increment PRIMARY KEY,
    nombre VARCHAR(50),
    puntaje int
);