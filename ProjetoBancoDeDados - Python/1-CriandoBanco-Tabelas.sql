use projetodb;

CREATE DATABASE projetodb;
#-----------------------------------
#CRIANDO TABELA DE clientes
#-----------------------------------
CREATE TABLE clientes
(
	CPF char(14) primary key,
	Nome varchar(255),
	Sobrenome varchar(255),
	Email varchar(255),
	Telefone varchar(13),
	Pais varchar(50),
	Cidade varchar(50),
	Estado varchar(50),
	Endereco varchar(255),
	CEP char (8)
);
#-----------------------------------

#-----------------------------------
#CRIANDO TABELA DE produtos
#-----------------------------------

CREATE TABLE produtos
(
	ID int primary key auto_increment,
	Nome varchar(150),
	Descricao varchar(200),
	Preco_Tabela double,
	Tipo varchar(50)
);
#-----------------------------------
#-----------------------------------
#CRIANDO TABELA DE vendas
#-----------------------------------

CREATE TABLE vendas
(
	ID int primary key auto_increment,
	CPF_Cliente char(14),
	FOREIGN KEY (CPF_Cliente) REFERENCES clientes(CPF),
	Data_Venda datetime,
	Tipo_Pagamento varchar(100),
	Data_Pagamento date,
	Nota_Enviada tinyint,
	Data_Envio date,
	Encerrada boolean,
    Cancelada tinyint NULL
);

#-----------------------------------

#-----------------------------------
#CRIANDO TABELA DE DETALHES DA VENDA
#-----------------------------------
CREATE TABLE detalhes_da_venda
(
	ID int primary key auto_increment,
	ID_Venda int,
	FOREIGN KEY (ID_Venda) REFERENCES vendas(ID),
	ID_Produto int,
	FOREIGN KEY (ID_Produto) REFERENCES produtos(ID),
	Quantidade integer,
	Preco_unitario double,
	Desconto double
);


