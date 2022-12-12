INSERT INTO vendas (CPF_Cliente, Data_Venda, Tipo_Pagamento, Data_Pagamento, Nota_Enviada, Data_Envio, Encerrada)
VALUES ('5555','2022-09-24','Boleto','0000-00-00','0','0000-00-00','0');

INSERT INTO detalhes_da_venda(ID_Venda, ID_Produto, Quantidade, Preco_unitario, Desconto)
VALUES ('65','4','5','240','0');

INSERT INTO detalhes_da_venda(ID_Venda, ID_Produto, Quantidade, Preco_unitario, Desconto)
VALUES ('65','2','2','40','0');


INSERT INTO vendas (CPF_Cliente, Data_Venda, Tipo_Pagamento, Data_Pagamento, Nota_Enviada, Data_Envio, Encerrada)
VALUES ('4444','2022-09-24','Credito','0000-00-00','0','0000-00-00','0');

INSERT INTO detalhes_da_venda(ID_Venda, ID_Produto, Quantidade, Preco_unitario, Desconto)
VALUES ('66','4','5','240','0');
INSERT INTO detalhes_da_venda(ID_Venda, ID_Produto, Quantidade, Preco_unitario, Desconto)
VALUES ('66','2','2','40','0');

select * from clientes;
select * from vendas;
select * from detalhes_da_venda;