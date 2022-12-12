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

comando = """INSERT INTO clientes
            (CPF, Nome, Sobrenome, Email, Telefone, Pais, Cidade, Estado, Endereco, CEP)
            VALUES
            """
sql = comando + dados
print(sql)
print("Dados Inseridos com sucesso")


adm.execute(sql)
conexao.commit()

print("FINALIZANDO CONEXAO COM O BANCO DE DADOS")
conexao.close()
adm.close()






