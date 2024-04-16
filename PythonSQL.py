import pyodbc
import os

def consultar_registros(Vcursor):
    # Comando SQL para selecionar todos os registros da tabela Vendas
    comando_selecionar = "SELECT * FROM Vendas"

    # Executando o comando SQL para selecionar registros
    Vcursor.execute(comando_selecionar)

    # Recuperando os registros selecionados
    registros = Vcursor.fetchall()

    # Exibindo os registros recuperados
    print("Registros na tabela Vendas:")
    for Indice in registros:
        print(Indice)
#----------------------------------------------------------------------------------------------------

def adicionar_registro(Vcursor):
    idVenda = input("Digite o ID do Client: ")
    nomeCliente = input("Digite o Nome do Client: ")

    # Comando SQL para inserir dados na tabela Vendas
    comando_inserir = f"""INSERT INTO Vendas(id_venda, cliente)
    VALUES
        ({idVenda}, '{nomeCliente}')"""

    # Executando o comando SQL para inserir dados
    Vcursor.execute(comando_inserir)

    # Efetuando o commit para confirmar as alterações no banco de dados
    Vcursor.commit()
    print("Registro adicionado com sucesso.")
#----------------------------------------------------------------------------------------------------

def excluir_registro(Vcursor):
    idVenda = input("Digite o ID do cliente que deseja excluir: ")

    # Comando SQL para excluir um registro da tabela Vendas
    comando_excluir = f"DELETE FROM Vendas WHERE id_venda = {idVenda}"

    # Executando o comando SQL para excluir o registro
    Vcursor.execute(comando_excluir)

    # Efetuando o commit para confirmar as alterações no banco de dados
    Vcursor.commit()
    print("Registro excluído com sucesso.")
#----------------------------------------------------------------------------------------------------

# Configuração da conexão com o banco de dados SQL Server
dados_conexao = (
    "Driver={SQL Server};" 
    "Server=DESKTOP-6BAHABT;" 
    "Database=PythonSQL;")

# Estabelecendo a conexão com o banco de dados
conexao = pyodbc.connect(dados_conexao)
print("Conexão Bem Sucedida")

# Criando um cursor para executar comandos SQL
Vcursor = conexao.cursor()
#----------------------------------------------------------------------------------------------------

# Menu de opções
while True:
    print("\nMenu:")
    print("1. Consultar registros")
    print("2. Adicionar registro")
    print("3. Excluir registro")
    print("4. Limpar")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        consultar_registros(Vcursor)
    elif opcao == "2":
        adicionar_registro(Vcursor)
    elif opcao == "3":
        excluir_registro(Vcursor)
    elif opcao == "4":
        os.system('CLS')
    elif opcao == "5":
        break
    else:
        print("Opção inválida. Tente novamente.")
#----------------------------------------------------------------------------------------------------

# Fechando o cursor e a conexão
Vcursor.close()
conexao.close()
#----------------------------------------------------------------------------------------------------