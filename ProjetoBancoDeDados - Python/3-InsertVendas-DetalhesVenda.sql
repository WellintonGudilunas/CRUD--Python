
INSERT INTO vendas (CPF_Cliente, Data_Venda, Tipo_Pagamento, Data_Pagamento, Nota_Enviada, Data_Envio, Encerrada)
VALUES ('5555','2022-11-23','Crédito','0000-00-00','0','0000-00-00','0');

INSERT INTO detalhes_da_venda(ID_Venda, ID_Produto, Quantidade, Preco_unitario, Desconto)
VALUES ('1','1','63','40','0');

describe vendas;
describe detalhes_da_venda;
select * from produtos;
select * from vendas;
select * from detalhes_da_venda;