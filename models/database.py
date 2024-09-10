import mysql.connector
from mysql.connector import Error

class Database:
    conexao = None
    def __init__(self):
        try:   
            self.conexao = mysql.connector.connect(
                host="localhost",
                user = "root",
                password= "root753",
                database="farmacia"
            )
            if self.conexao.is_connected():
                print("Conectado ao servidor mysql")
                cursor = self.conexao.cursor()
                cursor.execute("SELECT DATABASE();")
                nome_do_banco = cursor.fetchone()
                print("Conectado ao banco de dados" , nome_do_banco)
        except Error as e:
            print("Erro aoconectar ao Mysql",e)
            
            
    def fechar_conexao(self):
        if self.conexao.is_connected():
            self.conexao.close()
            print("Conexao encerrada")