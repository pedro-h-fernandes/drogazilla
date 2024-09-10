from models.database import Database

class Produto:
    def __init__(self, nome, telefone, email, senha, cpf):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.senha = senha
        self.cpf = cpf

class ProdutoDAO:
    def __init__(self):
        self.db = Database()

    def cadastra_cliente(self, cliente):
        cursor = self.db.conexao.cursor()
        
        sql_insert = ("INSERT INTO cliente (Nome, Telefone, Email, Senha, Cpf) "
                      "VALUES (%s, %s, %s, %s, %s)")
        valores = (cliente.nome, cliente.telefone, cliente.email, cliente.senha, cliente.cpf)
        cursor.execute(sql_insert, valores)
        self.db.conexao.commit()
        print("Cliente cadastrado com sucesso!")
        return cursor.lastrowid

    def lista_produtos(self):
        cursor = self.db.conexao.cursor()
        cursor.execute("SELECT * FROM cliente;")
        return cursor.fetchall()
