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

idVenda = str(input("Digite o ID da venda que deseja atualizar algum dado: "))
print("""As opções são: 1- Data do pagamento
2- Nota liberada
3- Produto enviado
4- Entrega finalizada
""")
CampoAtualizar = str(input("Digite o Numero que indica o nome do campo que deseja Atualizar: "))
if CampoAtualizar == '1':
    CampoAtualizar = 'Data_Pagamento'
elif CampoAtualizar == '2':
    CampoAtualizar = 'Nota_Enviada'
elif CampoAtualizar == '3':
    CampoAtualizar = 'Data_Envio'
elif CampoAtualizar == '4':
    CampoAtualizar = 'Encerrada'
else:
    print("Ta moscando Escobar, coloca o baguio certo")
    exit()
NovoDado = str(input("Digite o dado a ser atualizado: "))

comando = """UPDATE vendas
                SET """+ CampoAtualizar +"""=""" + """\'"""+ NovoDado+"""\'""" + """
                WHERE ID = """ + """\'"""+ idVenda +"""\'"""+""";"""
adm.execute(comando)
conexao.commit()
print("")
print("")
print("Dados Atualizados com sucesso")
print("FINALIZANDO CONEXAO COM O BANCO DE DADOS")
conexao.close()
adm.close()




