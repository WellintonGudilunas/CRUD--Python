
select * from produtos;
describe produtos;
INSERT INTO produtos (Nome, Descricao, Preco_Tabela, Tipo)
VALUES ('<NOME>','<DESCRICAO>','<PRECO>','<TIPO>');

UPDATE produtos 
SET Nome = ''
	#Descricao = '',
    #Preco_Tabela = '',
    #Telefone = '',
    #Tipo = '',
    #Cidade = '',
    #Estado = '',
    #Endereco = '',
    #CEP = ''
WHERE ID = '<ID DO PRODUTO A SER ATUALIZADO>';
