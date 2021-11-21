from pymongo import MongoClient

def Conexao():
    # Estabelecendo conexão: client
    porta = 27017
    return MongoClient("localhost", porta)
# def Connexao

def ConexaoBanco():
    # Conectando ao banco
    client = Conexao()
    return client
# def ConexaoBanco