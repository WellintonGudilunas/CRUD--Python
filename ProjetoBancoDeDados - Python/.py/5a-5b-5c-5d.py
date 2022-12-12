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