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

idProduto = str(input("Digite o ID do produto que deseja atualizar algum dado: "))
print("""Qual campo você deseja alterar?
As opções são:
1- Nome
2- Descrição 
3- Preço de tabela
4- Tipo
""")
CampoAtualizar = str(input("Digite o Numero que indica o nome do campo que deseja Atualizar: "))


if CampoAtualizar == '1':
    CampoAtualizar = 'Nome'
elif CampoAtualizar == '2':
    CampoAtualizar = 'Descricao'
elif CampoAtualizar == '3':
    CampoAtualizar = 'Preco_Tabela'
elif CampoAtualizar == '4':
    CampoAtualizar = 'Tipo'
else:
    print("Ta moscando Escobar, coloca o baguio certo")
    exit()
NovoDado = str(input("Digite o novo dado do produto: "))

comando = """UPDATE produtos
                SET """+ CampoAtualizar +"""=""" + """\'"""+ NovoDado+"""\'""" + """
                WHERE ID = """ + """\'"""+idProduto +"""\'"""+""";"""
adm.execute(comando)
conexao.commit()
print("")
print("")
print("Dados Atualizados com sucesso")
print("FINALIZANDO CONEXAO COM O BANCO DE DADOS")
conexao.close()
adm.close()




