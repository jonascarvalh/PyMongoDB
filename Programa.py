from Conexao import *
from Funcoes import *

db = ConexaoBanco()

while(1):
    # Retorna o último ID registrado
    cod = IdMax()
    print("1. Efetuar Cadastro")
    print("2. Visualizar Cadastros")
    print('3. Consultar')
    print("4. Atualizar Cadastro")
    print("5. Deletar Cadastro")
    opcao = int(input(">> "))

    match opcao:
        case 1:
            EfetuarCadastro(db,cod)
            cod += 1
        case 2:
            VisualizarCadastros()
        case 3:
            LimparTerminal()
            cod = int(input('ID a ser consultado: '))
            ConsultarCadastro(cod)
        case 4:
            AtualizarCadastro()
        case 5:
            DeletarCadastro()
        case _:
            print("Opção Inválida!")
# Menu