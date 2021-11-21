from Conexao import *
from Funcoes import *

# O nome do meu banco é "Registros"
db = Conexao().Registros
cod = 1

while(1):
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

# Coisas Importantes que faltam:
# retornar o ID do último cadastrado
# Assim não terão ID's repetidos