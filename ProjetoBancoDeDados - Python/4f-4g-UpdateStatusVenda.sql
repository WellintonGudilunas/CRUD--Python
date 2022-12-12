select * from vendas;
UPDATE vendas 
SET Data_Pagamento = '2022-11-25',
	Nota_Enviada = '1',
	Data_Envio = '2022-11-29',
	Encerrada = '0'
WHERE vendas.ID = '46';


describe vendas;
