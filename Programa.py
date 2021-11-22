from Conexao import *
from Funcoes import *

# O nome do meu banco é "Registros"
banco = 'Registros'
db = ConexaoBanco()

while(1):
    # Retorna o último ID registrado
    cod = IdMax()
    print("1. Efetuar Cadastro")
    print("2. Visualizar Cadastros")
    opcao = int(input(">> "))

    if opcao == 1:
        EfetuarCadastro(db,cod)
        cod += 1
    elif opcao == 2:
        VisualizarCadastros()
    else:
        print("Opção Inválida!")
# Menu