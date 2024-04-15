import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server=Your Desktop;"
    "Database=Teste;"
    )

conexao = pyodbc.connect(dados_conexao)
print("Conexão Bem Sucedida")

cursor = conexao.cursor()

comando = """INSERT INTO Vendas(id_venda, cliente, produto, data_venda, preco, quantidade)
VALUES
    (3, 'Alan', 'Notebook', '01/05/2024', 2000, 1)"""

cursor.execute(comando)
cursor.commit()