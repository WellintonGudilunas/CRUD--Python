

INSERT INTO clientes (CPF, Nome, Sobrenome, Email, Telefone, Pais, Cidade, Estado, Endereco, CEP)
VALUES ('<CPF>','<NOME>','<SOBRENOME>','<EMAIL>','<TELEFONE>','<PAIS>','<CIDADE>','<ESTADO>', '<ENDEREÇO>', '<CEP>');

UPDATE clientes 
SET Nome = ''
	#Sobrenome = '',
    #Email = '',
    #Telefone = '',
    #Pais = '',
    #Cidade = '',
    #Estado = '',
    #Endereco = '',
    #CEP = ''
WHERE CPF = '<CPF DO CLIENTE A SER ATUALIZADO>';
