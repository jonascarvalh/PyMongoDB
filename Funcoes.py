import os
from Conexao import *

def LimparTerminal():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')
# def LimparTerminal

def ModeloDados(cod, nome, idade):
    dados = {
        "id": cod,
        "Nome": nome,
        "Idade": idade
    }
    return dados
# def ModeloDados

def EfetuarCadastro(db, cod):
    LimparTerminal()
    print(' 「 Cadastro 」 ')
    nome  = input("Nome: ")
    idade = input("Idade: ")
    dados = ModeloDados(cod,nome,idade)

    # Inserindo dado
    db.pessoas.insert_one(dados)

    print('Dados inseridos com sucesso!')
    input()
    LimparTerminal()
# def EfetuarCadastro

def VisualizarCadastros():
    # Acessando banco para obter os registros
    registros = LeituraBanco(ConexaoBanco())
    
    LimparTerminal()
    print(" 「 Cadastros 」 ")

    for registro in registros.find():
        print("ID:    ", registro.get('id'))
        print("Nome:  ", registro.get('Nome'))
        print("Idade: ", registro.get('Idade'))
        print("")
    # Imprimindo Registros
    
    input()
    LimparTerminal()
# def VisualizarCadastros

def ConsultarCadastro(cod):
    print(" 「 Consulta 」 ")
    registros = LeituraBanco(ConexaoBanco())
    for registro in registros.find({'id': cod}).limit(1):
        if not registro:
            print('Registro não encontrado')
            return False
        else:
            print('ID: ', registro.get('id'))
            print('Nome: ', registro.get('Nome'))
            print('Idade: ', registro.get('Idade'))
    
    input()
    LimparTerminal()
    return registros
# def ConsultarCadastro


def AtualizarCadastro():
    LimparTerminal()
    print(" 「 Alteração 」 ")
    cod = int(input('ID do usuário a ser alterado: '))
    registros = ConsultarCadastro(cod)
    if registros == False:
        print('Registro não encontrado')

    registros.update_one(
        {'id': cod},
        {'$set': {'Nome': input('Nome: ')}}
    ) # Atualizar Nome

    registros.update_one(
        {'id': cod},
        {'$set': {'Idade': input('Idade: ')}}
    ) # Atualizar Idade
    
    print('Dados atulizados')
    input()
    LimparTerminal()
# def AtualizarCadastro

def IdMax():
    registros = LeituraBanco(ConexaoBanco())
    if registros.count_documents({}) != 0:
        for registro in registros.find().sort('_id',-1).limit(1):
            return registro.get('id')+1
    else:
        return 1
# def IdMax

def DeletarCadastro():
    LimparTerminal()
    registros = LeituraBanco(ConexaoBanco())

    cod = int(input('Indique o ID a ser deletado: '))
    
    try:
        registros.delete_one({'id': cod})
        print(f'O registro {cod} foi deletado')
    except:
        print('Houve um erro ao deletar')
