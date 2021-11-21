import os
from Conexao import *

def LimparTerminal():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')
# def LimparTerminal

def LeituraBanco(client):
    db = client.get_database('Registros')
    return db.get_collection('pessoas')
# def LeituraBanco

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
    registros = LeituraBanco(Conexao())
    
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