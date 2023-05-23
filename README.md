create database cad_cliente;

create table cliente(
id_cliente int  auto_increment primary key,
nome varchar(50) not null,
cpf varchar(11) not null,
email varchar(50) not null 
);