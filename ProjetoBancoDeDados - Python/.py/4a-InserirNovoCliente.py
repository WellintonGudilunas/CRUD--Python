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
CPF = str(input('Digite o CPF do usuário que deseja cadastrar: '))
Nome = str(input('Digite o Nome do usuário que deseja cadastrar: '))
Sobrenome = str(input('Digite o Sobrenome do usuário que deseja cadastrar: '))
Email = str(input('Digite o Email do usuário que deseja cadastrar: '))
Telefone = str(input('Digite o Telefone do usuário que deseja cadastrar: '))
Pais = str(input('Digite o Pais do usuário que deseja cadastrar: '))
Cidade = str(input('Digite a Cidade do usuário que deseja cadastrar: '))
Estado = str(input('Digite o Estado do usuário que deseja cadastrar: '))
Endereco = str(input('Digite o Endereco do usuário que deseja cadastrar: '))
CEP = str(input('Digite o CEP do usuário que deseja cadastrar: '))

dados = '(\''+ CPF +'\', \''+ Nome +'\', \'' + Sobrenome + '\', \'' + Email + '\', \''+Telefone+ '\', \''+Pais+'\', \''+Cidade+'\', \''+ Estado + '\', \''+ Endereco + '\', \'' + CEP+'\')'
print(dados)

declaracao = """INSERT INTO clientes
            (CPF, Nome, Sobrenome, Email, Telefone, Pais, Cidade, Estado, Endereco, CEP)
            VALUES
            """
sql = declaracao + dados
print(sql)
print("Dados Inseridos com sucesso")


inserir_cliente = sql
adm.execute(inserir_cliente)
conexao.commit()

#insert de um jeito diferente
#-------------------------------------------------------------------------------------------------------
# comand = "INSERT INTO clientes (CPF, Nome, Sobrenome, Email, Telefone, Pais, Cidade, Estado, Endereco, CEP) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
# values = ('55473357', 'Jair Messias', 'Lula', 'jairlula@gmail.com','4199543543', 'BR', 'Joinville', 'SC', 'Ilhota', '676556')
# adm.execute(comand, values)
# conexao.commit()
#
# print("Dados Inseridos com sucesso")

print("FINALIZANDO CONEXAO COM O BANCO DE DADOS")
conexao.close()
adm.close()






