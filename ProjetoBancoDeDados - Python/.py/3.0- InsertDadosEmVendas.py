import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='Admin',
    database='projetodb',
    password='3333'
)

if conexao.is_connected():
    print("Conectado")
    adm = conexao.cursor()
#-------------------------------------------------------------------------------------------------------
adm.execute\
(
    """insert into
	    vendas(CPF_Cliente, Data_Venda, Tipo_Pagamento, Data_Pagamento, Pagamento_Realizado, Nota_Enviada, Data_Envio, Encerrada)
        values ('khjhjk', '2022-11-03', '2', '2022-11-05','1', '0', '2022-11-03', '0');"""
)
conexao.commit()

#-------------------------------------------------------------------------------------------------------
#insert de um jeito diferente
#-------------------------------------------------------------------------------------------------------
# comand = "INSERT INTO vendas (CPF_Cliente, Data_Venda, Tipo_Pagamento, Data_Pagamento, Pagamento_Realizado, Nota_Enviada, Data_Envio, Encerrada) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
# values = ('72477', '2022-11-03', '2', '2022-11-05','1', '0', '2022-11-03', '0')
# adm.execute(comand, values)
# conexao.commit()

# comand = "INSERT INTO vendas (ID, CPF_Cliente, Data_Venda, Tipo_Pagamento, Data_Pagamento, Pagamento_Realizado, Nota_Enviada, Data_Envio, Encerrada) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
# values = ('12389', '72477', '2022-11-03', '2', '2022-11-05','1', '0', '2022-11-03', '0')
# adm.execute(comand, values)
# conexao.commit()
#-------------------------------------------------------------------------------------------------------

conexao.close()
adm.close()






