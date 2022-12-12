import mysql.connector


opcaoEscolhida = 0
def comprar(mesmaCompra):
    print("Os produtos disponiveis são: ")
    query = 'SELECT ID, Nome, Descricao, Preco_Tabela FROM produtos;'
    adm.execute(query)
    resultadoSelect = adm.fetchall()
    i = 1
    for row in resultadoSelect:
        print(str(i) + " - " + str(row))
        i += 1
    EleQuerNessaLinha = int(input("Qual Produto voce deseja comprar: "))
    quantoselequer = int(str(input(
        "Quantas unidades desse " + str(resultadoSelect[EleQuerNessaLinha - 1][1]) + " que custa R$" + str(
            resultadoSelect[EleQuerNessaLinha - 1][3]) + " voce quer: ")))
    valor = (resultadoSelect[EleQuerNessaLinha - 1][3])
    valor2 = valor * quantoselequer
    print("isso irá custar:  R$" + str(valor2))

    formaPagamento = input("qual será a forma de pagamento? Credito, Débito ou Boleto?: ")
    data = "2022-11-23"
    data_Pagamento = "0000-00-00"
    Nota_Enviada = "0"
    Data_envio = "0000-00-00"
    Encerrada = "0"

    ID_produto = str((resultadoSelect[EleQuerNessaLinha - 1][0]))
    Quantidade = str(quantoselequer)
    Preco_unitario = str(valor)
    Desconto = '0'

    dados = '(\'' + cpfCompador + '\', \'' + data + '\', \'' + formaPagamento + '\', \'' + data_Pagamento + '\', \'' + Nota_Enviada + '\', \'' + Data_envio + '\', \'' + Encerrada + '\');'

    # print(dados)
    # print(dados2)
    if not mesmaCompra:
        declaracao = """INSERT INTO vendas (CPF_Cliente, Data_Venda, Tipo_pagamento, Data_Pagamento, Nota_Enviada, Data_Envio, Encerrada)
                             VALUES
                         """
        sql = declaracao + dados
        adm.execute(sql)
        conexao.commit()

    queryMaxIdVenda = "SELECT MAX(id) FROM vendas"
    adm.execute(queryMaxIdVenda)
    ID_venda = str(adm.fetchone()[0])

    print(ID_venda)
    dados2 = '(\'' + ID_venda + '\', \'' + ID_produto + '\', \'' + Quantidade + '\', \'' + Preco_unitario + '\', \'' + Desconto + '\');'
    declaracao2 = """INSERT INTO detalhes_da_venda (ID_Venda, ID_Produto, Quantidade, Preco_unitario, Desconto)
                             VALUES
                         """

    sql2 = declaracao2 + dados2
    ##print(sql, sql2)
    adm.execute(sql2)
    conexao.commit()
    print("Dados da venda inseridos com sucesso")
while opcaoEscolhida != 10:
    print("""O que você deseja fazer, querido usuário 
    As opções são:
    1- Criar o banco de dados e suas respectivas tabelas
    2- Cadastrar um novo cliente
    3- Atualizar o dado de um cliente
    4- Cadastrar um produto
    5- Atualizar o dado de um produto
    6- Efetuar uma venda
    7- Atualizar status da venda
    8- Relatórios
    9- Selects
    10- Sair""")

    opcaoEscolhida = str(input("Digite a opção desejada: "))
    #Conectando com o mysql
    if opcaoEscolhida == '1':
        conexao = mysql.connector.connect(
            host='localhost',
            user='Admin',
            password='3333'
        )
        adm = conexao.cursor()
    #-----------------------------------
    #CRIANDO O BANCO DE DADOS
    #-----------------------------------
        adm.execute("CREATE DATABASE projetodb;")
    #-----------------------------------
    #Conectando com o bando de dados criado acima
        conexao = mysql.connector.connect(
            host='localhost',
            user='Admin',
            database='projetodb',
            password='3333'
        )
        adm = conexao.cursor()

    #-----------------------------------
    #CRIANDO TABELA DE clientes
    #-----------------------------------
        adm.execute\
        (
            """CREATE TABLE clientes
            (
                CPF char(14) primary key,
                Nome varchar(255),
                Sobrenome varchar(255),
                Email varchar(255),
                Telefone varchar(13),
                Pais varchar(50),
                Cidade varchar(50),
                Estado varchar(50),
                Endereco varchar(255),
                CEP char (8)
            );"""
        )
    #-----------------------------------



    #-----------------------------------
    #CRIANDO TABELA DE produtos
    #-----------------------------------
        adm.execute \
        (
            """CREATE TABLE produtos
            (
                ID int primary key auto_increment,
                Nome varchar(150),
                Descricao varchar(200),
                Preco_Tabela double,
                Tipo varchar(50)
            );"""
        )
    #-----------------------------------



    #-----------------------------------
    #CRIANDO TABELA DE vendas
    #-----------------------------------
        adm.execute\
        (
            """CREATE TABLE vendas
            (
                ID int primary key auto_increment,
                CPF_Cliente char(14),
                FOREIGN KEY (CPF_Cliente) REFERENCES clientes(CPF),
                Data_Venda datetime,
                Tipo_Pagamento varchar(100),
                Data_Pagamento date,
                Nota_Enviada tinyint,
                Data_Envio date,
                Encerrada boolean,
                Cancelada tinyint NULL
            );"""
        )
    #-----------------------------------



    #-----------------------------------
    #CRIANDO TABELA DE DETALHES DA VENDA
    #-----------------------------------
        adm.execute\
        (
            """CREATE TABLE detalhes_da_venda
            (
                ID int primary key auto_increment,
                ID_Venda int,
                FOREIGN KEY (ID_Venda) REFERENCES vendas(ID),
                ID_Produto int,
                FOREIGN KEY (ID_Produto) REFERENCES produtos(ID),
                Quantidade integer,
                Preco_unitario double,
                Desconto double
             );"""
        )
        print("")
        print("Banco de dados e suas tabelas criadas com sucesso!!")
    #-----------------------------------
        conexao.close()
        adm.close()

    elif opcaoEscolhida == '2':

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

        dados = '(\'' + CPF + '\', \'' + Nome + '\', \'' + Sobrenome + '\', \'' + Email + '\', \'' + Telefone + '\', \'' + Pais + '\', \'' + Cidade + '\', \'' + Estado + '\', \'' + Endereco + '\', \'' + CEP + '\')'

        declaracao = """INSERT INTO clientes
                    (CPF, Nome, Sobrenome, Email, Telefone, Pais, Cidade, Estado, Endereco, CEP)
                    VALUES
                    """
        sql = declaracao + dados
        print("Dados Inseridos com sucesso")
        adm.execute(sql)
        conexao.commit()

    elif opcaoEscolhida == '3':

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
                        SET """ + CampoAtualizar + """=""" + """\'""" + NovoDado + """\'""" + """
                        WHERE CPF = """ + """\'""" + CPF + """\'""" + """;"""
        adm.execute(comando)
        conexao.commit()
        print("")
        print("")
        print("Dados Atualizados com sucesso")
        print("FINALIZANDO CONEXAO COM O BANCO DE DADOS")
        conexao.close()
        adm.close()

    elif opcaoEscolhida == '4':

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

        dados = '(\'' + NomeProduto + '\', \'' + Descricao + '\', \'' + PrecoTabela + '\', \'' + Tipo + '\')'

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

    elif opcaoEscolhida == '5':

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
                        SET """ + CampoAtualizar + """=""" + """\'""" + NovoDado + """\'""" + """
                        WHERE ID = """ + """\'""" + idProduto + """\'""" + """;"""
        adm.execute(comando)
        conexao.commit()
        print("")
        print("")
        print("Dados Atualizados com sucesso")
        print("FINALIZANDO CONEXAO COM O BANCO DE DADOS")
        conexao.close()
        adm.close()

    elif opcaoEscolhida == '6':

        conexao = mysql.connector.connect(
            host='localhost',
            user='Admin',
            database='projetodb',
            password='3333'
        )
        #comprar = True
        if conexao.is_connected():
            print("Conectado No BANCO DE DADOS")
            adm = conexao.cursor()

        cpfCompador = input("Você escolheu fazer uma compra, para continuar, digite seu CPF:")


        continuar = 1
        mesmaCompra = False
        while continuar != 2:
            comprar(mesmaCompra)
            continuar = int(input("""Deseja continuar comprando?
                   1- Sim 
                   2- Não: """))
            if continuar == 1:
                mesmaCompra = True

    elif opcaoEscolhida == '7':

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
                        SET """ + CampoAtualizar + """=""" + """\'""" + NovoDado + """\'""" + """
                        WHERE ID = """ + """\'""" + idVenda + """\'""" + """;"""
        adm.execute(comando)
        conexao.commit()
        print("")
        print("")
        print("Dados Atualizados com sucesso")
        print("FINALIZANDO CONEXAO COM O BANCO DE DADOS")
        conexao.close()
        adm.close()

    elif  opcaoEscolhida == '8':
        conexao = mysql.connector.connect(
            host='localhost',
            user='Admin',
            database='projetodb',
            password='3333'
        )
        if conexao.is_connected():
            print("Conectado No BANCO DE DADOS")
            adm = conexao.cursor()

        qualRelatorio = int(input(""" Qual relatório você deseja acessar?
            1- Total vendido em quantidade e valores de cada produto
            2- Total comprado em produtos, quantidade e valores por cada cliente
            3- Total comprado por um cliente específico
            4- Total em vendas com boletos abertos  (que ainda não foram pagos)
            Digite a Opção: """))
        if qualRelatorio == 1:
            adm.execute("""SELECT   p.ID,
                                    p.Nome,
                                    #ddv.Preco_unitario,
                                    #ddv.Quantidade
                                    sum(ddv.Preco_unitario*ddv.Quantidade) as PrecoTotal,
                                    sum(ddv.Quantidade) as quantidadeTotal
                            FROM vendas as v
                            INNER JOIN detalhes_da_venda as ddv ON v.ID = ddv.ID_Venda
                            INNER JOIN produtos as p ON ddv.ID_Produto = p.ID
                            GROUP BY p.ID, p.Nome;
                        """)
            print("(ID, Nome, PrecoTotal, quantidadeTotal)")
            resultadoSelect = adm.fetchall()
            for x in resultadoSelect:
                print(x)


        elif qualRelatorio == 2:
            adm.execute("""SELECT   c.CPF,
                                    c.Nome,
                                    p.ID,
                                    p.Nome,
                                    #ddv.Preco_unitario,
                                    #ddv.Quantidade
                                sum(ddv.Preco_unitario*ddv.Quantidade) as PrecoTotal,
                                sum(ddv.Quantidade) as quantidade
                            FROM vendas as v
                            INNER JOIN detalhes_da_venda as ddv ON v.ID = ddv.ID_Venda
                            INNER JOIN produtos as p ON ddv.ID_Produto = p.ID
                            INNER JOIN clientes as c ON c.CPF = v.CPF_Cliente
                            GROUP BY p.ID, p.Nome, c.CPF, c.Nome;
            """)
            print("(CPF, NomeCliente, IdProduto, NomeDoProduto, PrecoTotal, Quantidade)")
            resultadoSelect = adm.fetchall()
            for x in resultadoSelect:
                print(x)


        elif qualRelatorio == 3:
            adm.execute("""SELECT c.CPF,
                                  c.Nome,
                                  #ddv.Preco_unitario,
                                  #ddv.Quantidade
                                  sum(ddv.Preco_unitario*ddv.Quantidade) as PrecoTotal
                            FROM vendas as v
                            INNER JOIN detalhes_da_venda as ddv ON v.ID = ddv.ID_Venda
                            INNER JOIN clientes as c ON c.CPF = v.CPF_Cliente
                            GROUP BY c.Nome, c.CPF;
            """)
            print("CPF, Nome, Valor")
            resultadoSelect = adm.fetchall()
            for x in resultadoSelect:
                print(x)


        elif qualRelatorio == 4:

            adm.execute("""SELECT #v.Data_Pagamento,
                               sum(ddv.Preco_unitario*ddv.Quantidade) as PrecoTotal
                    FROM vendas as v
                    INNER JOIN detalhes_da_venda as ddv ON v.ID = ddv.ID_Venda
                    WHERE v.Data_Pagamento = '0000-00-00' AND v.Tipo_Pagamento = 'Boleto'
                    GROUP BY v.Data_Pagamento;
            """)
            print("valor")
            resultadoSelect = adm.fetchall()
            for x in resultadoSelect:
                print(x)

        else:
            print("Opção inválida")
            exit()


    elif opcaoEscolhida == '9':

        conexao = mysql.connector.connect(
            host='localhost',
            user='Admin',
            database='projetodb',
            password='3333'
        )
        adm = conexao.cursor()
        print("""Digite o numero que representa qual tabela você deseja fazer um Select
        1- Clientes
        2- Produtos
        3- Vendas
        4- Detalhes da venda
        """)
        opcao = input(str("Digite a opção desejada: "))

        if opcao == '1':
            table = 'clientes'
            query = 'SELECT * FROM ' + table + ';'
            adm.execute(query)
            resultadoSelect = adm.fetchall()
            print(query)
            for x in resultadoSelect:
                print(x)

        elif opcao == '2':
            query = 'SELECT * FROM produtos;'
            adm.execute(query)
            resultadoSelect = adm.fetchall()
            print(query)
            for x in resultadoSelect:
                print(x)

        elif opcao == '3':
            query = 'SELECT * FROM vendas;'
            adm.execute(query)
            resultadoSelect = adm.fetchall()
            print(query)
            for x in resultadoSelect:
                print(x)

        elif opcao == '4':
            query = 'SELECT * FROM detalhes_da_venda;'
            adm.execute(query)
            resultadoSelect = adm.fetchall()
            print(query)
            for x in resultadoSelect:
                print(x)
        else:
            print("Opção inválida!!")
            exit()
            conexao.close()
            adm.close()

    elif  opcaoEscolhida == '10':
        print("Volte sempre")
        exit()
    else:
        print("Opção inválida")
        exit()

