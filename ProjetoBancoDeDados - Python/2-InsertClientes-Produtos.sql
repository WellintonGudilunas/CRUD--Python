use projetodb;

describe clientes;
select * from clientes;

INSERT INTO clientes (CPF, Nome, Sobrenome, Email, Telefone, Pais, Cidade, Estado, Endereco, CEP)
VALUES  ('1111','Daddy','Bengala','daddybengala@gmail.com','41911111111','BR','Curitiba','Paraná', 'BANGU', '74233322'),
		('2222','Kaik','Wrld','kaikwrld@gmail.com','41922222222','BR','Curitiba','SP', 'gueto', '856734'),
        ('3333','Leon','Piolho','leopiolho@gmail.com','41933333333','BR','Gramados','RS', 'Alphaville', '576234'),
        ('4444','Cleiton','Rasta','cleirtonrasta@gmail.com','41944444444','BR','Ilhota','SC', 'ponte', '12345612'),
        ('6666','Gepeto','GP','gepeto@gmail.com','41966666666','BR','Curitiba','Paraná', 'BANGU', '768923');

describe produtos;
select * from produtos;

INSERT INTO produtos (Nome, Descricao, Preco_Tabela, Tipo)
VALUES  ('Mouse Gamer','Mouse Husky blizzard 16000dpi','240','reciclavel'),
		('Memoria RAM','Memoria RAM 8gb, RGB 3200mhz','170','reciclavel'),
        ('Fonte 650w','Fonte XPG core reactor 650w','400','reciclavel'),
        ('SSD 512gb','SSD XPG 512gb, m2, NVME, pcie 4.0','350','reciclavel'),
        ('Ventoinhas RGB','3x Ventoinhas RGB DeepCool 67,5 CFM','129','reciclavel');
		