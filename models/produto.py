from models.database import Database

class Produto:
    def __init__(self, nome, descricao, preco, custo, quantidade_estoque):
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.custo = custo
        self.quantidade_estoque = quantidade_estoque

class ProdutoDAO:
    def __init__(self):
        self.db = Database()

    def insere_produto(self, produto):
        cursor = self.db.conexao.cursor()
   
        sql_insert = ("INSERT INTO Produto (Nome, Descricao, Preco, Custo, Quantidade_Estoque) "
                      "VALUES (%s, %s, %s, %s, %s)")
        valores = (produto.nome, produto.descricao, produto.preco, produto.custo, produto.quantidade_estoque)
        cursor.execute(sql_insert, valores)
        self.db.conexao.commit()
        print("Produto inserido com sucesso!")
        return cursor.lastrowid

    def lista_produtos(self):
        cursor = self.db.conexao.cursor()
        cursor.execute("SELECT * FROM Produto;")
        return cursor.fetchall()
