#DESAFIO
UPDATE vendas
	SET Cancelada = '1'
WHERE Tipo_Pagamento = 'Boleto' AND
datediff(NOW(), vendas.Data_Venda) > 5;
set sql_safe_updates = 0;