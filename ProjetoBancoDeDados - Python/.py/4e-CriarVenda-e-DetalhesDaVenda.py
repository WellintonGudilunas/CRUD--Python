import mysql.connector
conexao = mysql.connector.connect(
    host='localhost',
    user='Admin',
    database='projetodb',
    password='3333'
)

if conexao.is_connected():
    print("Conectado No BANCO DE DADOS")
    adm = conexao.cursor()

adm.execute\
(
    """INSERT INTO vendas (CPF_Cliente, Data_Venda, Tipo_Pagamento, Data_Pagamento, Nota_Enviada, Data_Envio, Encerrada)
        VALUES  ('123','2022-09-24','Boleto','0000-00-00','0','0000-00-00','0'),
                ('123','2022-09-24','Credito','0000-00-00','0','0000-00-00','0');
    """
)
conexao.commit()


adm.execute\
(
    """INSERT INTO detalhes_da_venda(ID_Venda, ID_Produto, Quantidade, Preco_unitario, Desconto)
        VALUES  ('59','4','5','240','0'),
                ('59','2','2','40','0'),
                ('60','4','5','240','0'),
                ('60','2','2','40','0');
    """
)
print("Dados de venda inseridos com sucesso")
conexao.commit()

