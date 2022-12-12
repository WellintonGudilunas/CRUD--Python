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
("""UPDATE vendas
        SET Cancelada = '1'
        WHERE Tipo_Pagamento = 'Boleto' AND
        datediff(NOW(), vendas.Data_Venda) > 5;
        
"""
)
conexao.commit()
print("Agora todos os boletos abertos por mais de 5 dias estão com o status: CANCELADO")
#set sql_safe_updates = 0;
