from pymongo import MongoClient

def Conexao():
    # Estabelecendo conexão: client
    porta = 27017
    return MongoClient("localhost", porta)
# def Connexao

def ConexaoBanco():
    # Conectando ao banco
    nome_banco = 'Registros'
    client = Conexao().get_database(nome_banco)
    return client
# def ConexaoBanco

def LeituraBanco(db):
    return db.get_collection('pessoas')
# def LeituraBanco