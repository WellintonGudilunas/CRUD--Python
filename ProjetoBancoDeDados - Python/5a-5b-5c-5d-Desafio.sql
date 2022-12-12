select * from detalhes_da_venda;

#1- Total vendido em quantidade e valores de cada produto
SELECT  p.ID,
		p.Nome,
        #ddv.Preco_unitario,
        #ddv.Quantidade
        sum(ddv.Preco_unitario*ddv.Quantidade) as PrecoTotal,
        sum(ddv.Quantidade) as quantidadeTotal
FROM vendas as v
INNER JOIN detalhes_da_venda as ddv ON v.ID = ddv.ID_Venda
INNER JOIN produtos as p ON ddv.ID_Produto = p.ID
GROUP BY p.ID, p.Nome;



#2- Total comprado em produtos, quantidade e valores por cada cliente
SELECT  c.CPF,
		c.Nome,
		p.ID,
		p.Nome,
        #ddv.Preco_unitario,
        #ddv.Quantidade
        sum(ddv.Preco_unitario*ddv.Quantidade) as PrecoTotal,
        sum(ddv.Quantidade) as quantidade
FROM vendas as v
INNER JOIN detalhes_da_venda as ddv ON v.ID = ddv.ID_Venda
INNER JOIN produtos as p ON ddv.ID_Produto = p.ID
INNER JOIN clientes as c ON c.CPF = v.CPF_Cliente
GROUP BY p.ID, p.Nome, c.CPF, c.Nome;


#3- Total comprado por um cliente específico
SELECT
		c.CPF,
		c.Nome,
        #ddv.Preco_unitario,
        #ddv.Quantidade
        sum(ddv.Preco_unitario*ddv.Quantidade) as PrecoTotal
FROM vendas as v
INNER JOIN detalhes_da_venda as ddv ON v.ID = ddv.ID_Venda
INNER JOIN clientes as c ON c.CPF = v.CPF_Cliente
GROUP BY c.Nome, c.CPF;


select * from VENDAS;
select * from detalhes_da_venda;
describe vendas;

#4- Total em vendas com boletos abertos  (que ainda não foram pagos)
SELECT
		#v.Data_Pagamento,
        sum(ddv.Preco_unitario*ddv.Quantidade) as PrecoTotal
FROM vendas as v
INNER JOIN detalhes_da_venda as ddv ON v.ID = ddv.ID_Venda
WHERE v.Data_Pagamento = '0000-00-00' AND v.Tipo_Pagamento = 'Boleto'
GROUP BY v.Data_Pagamento;



