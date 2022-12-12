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
NomeProduto = str(input('Digite o Nome do Produto que deseja cadastrar: '))
Descricao = str(input('Digite uma descrição do produto:  '))
PrecoTabela = str(input('Digite o Preço de tabela do produto: '))
Tipo = str(input('Digite o Tipo do produto: '))

dados = '(\''+ NomeProduto +'\', \''+ Descricao +'\', \'' + PrecoTabela + '\', \'' + Tipo + '\')'

comando = """INSERT INTO produtos
            (Nome, Descricao, Preco_Tabela, Tipo)
            VALUES
            """
sql = comando + dados

adm.execute(sql)
conexao.commit()
print("")
print("")
print("Dados Inseridos com sucesso")
print("FINALIZANDO CONEXAO COM O BANCO DE DADOS")
conexao.close()
adm.close()






