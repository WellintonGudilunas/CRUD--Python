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

CPF = str(input("Digite o CPF do cliente que deseja atualizar algum dado: "))
print("""As opções são: 1- Nome
2- Sobrenome
3- Email
4- Telefone
5- Pais
6- Cidade
7- Estado
8- Endereço
9- CEP)""")
CampoAtualizar = str(input("Digite o Numero que indica o nome do campo que deseja Atualizar: "))


if CampoAtualizar == '1':
    CampoAtualizar = 'Nome'
elif CampoAtualizar == '2':
    CampoAtualizar = 'Sobrenome'
elif CampoAtualizar == '3':
    CampoAtualizar = 'Email'
elif CampoAtualizar == '4':
    CampoAtualizar = 'Telefone'
elif CampoAtualizar == '5':
    CampoAtualizar = 'Pais'
elif CampoAtualizar == '6':
    CampoAtualizar = 'Cidade'
elif CampoAtualizar == '7':
    CampoAtualizar = 'Estado'
elif CampoAtualizar == '8':
    CampoAtualizar = 'Endereco'
elif CampoAtualizar == '9':
    CampoAtualizar = 'CEP'
else:
    print("Ta moscando Escobar, coloca o baguio certo")
    exit()
NovoDado = str(input("Digite o Novo dado do cliente: "))

comando = """UPDATE clientes
                SET """+ CampoAtualizar +"""=""" + """\'"""+ NovoDado+"""\'""" + """
                WHERE CPF = """ + """\'"""+ CPF+"""\'"""+""";"""
adm.execute(comando)
conexao.commit()
print("")
print("")
print("Dados Atualizados com sucesso")
print("FINALIZANDO CONEXAO COM O BANCO DE DADOS")
conexao.close()
adm.close()




