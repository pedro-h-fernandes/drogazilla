import mysql.connector
from mysql.connector import Error
from flask import Flask, render_template, request, redirect, url_for, flash, session
import bcrypt
app = Flask(__name__)
app.secret_key = '1234'

class Database:
    #conetando o banco de dados
    conexao = None
    def __init__(self):
        try:
            self.conexao = mysql.connector.connect(
                host = "localhost",
                database = "farmacia",
                user = "root",
                password = "root753"
            )
            if self.conexao.is_connected():
                print("conectado ao servidor")
                cursor = self.conexao.cursor()
                cursor.execute("SELECT DATABASE();")
                nome_do_banco = cursor.fetchone()
                print("conectado ao banco de dados",nome_do_banco)
        except Error as e : 
            print ("Erro de conexao ao banco de dados", e)
    #fechando o banco de dados     
    def fecha(self):
        if self.conexao.is_connected():
            self.conexao.close()
            print("conexão ao banco de dados encerrada")
#clientes            
    def cadastraCliente(self, cliente):
        if self.conexao.is_connected():
            cursor = self.conexao.cursor()
            sql_insert = "INSERT INTO cliente (username, password, cpf, email, endereco, telefone) VALUES(%s, %s, %s ,%s, %s ,%s)"
            valores = (cliente.username, cliente.password, cliente.cpf , cliente.email, cliente.endereco , cliente.telefone)
            cursor.execute(sql_insert, valores)
            self.conexao.commit()
            print("Commit efetuado com sucesso")

    def cadastraFuncionario(self, funcionario):
        if self.conexao.is_connected():
            cursor = self.conexao.cursor()
            sql_insert = "INSERT INTO funcionario (username, password, cpf, email, endereco, telefone) VALUES(%s, %s, %s ,%s, %s ,%s)"
            valores = (funcionario.username, funcionario.password, funcionario.cpf , funcionario.email, funcionario.endereco , funcionario.telefone)
            cursor.execute(sql_insert, valores)
            self.conexao.commit()
            print("Commit efetuado com sucesso")

    def verifica_cliente_existente(self, cpf):
        if self.conexao.is_connected():
            cursor = self.conexao.cursor()
            sql_select = "SELECT COUNT(*) FROM cliente WHERE cpf = %s"
            cursor.execute(sql_select, (cpf,))
            count = cursor.fetchone()[0]
            return count > 0   
        
    def verifica_login(self, username, password):
        if self.conexao.is_connected():
            cursor = self.conexao.cursor()
            sql_select = "SELECT password FROM cliente WHERE username = %s"
            cursor.execute(sql_select, (username,))
            result = cursor.fetchone()
            if result:
                stored_password = result[0]
                return bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8'))
            return False 

    def verifica_funcionario_existente(self, cpf):
        if self.conexao.is_connected():
            cursor = self.conexao.cursor()
            sql_select = "SELECT COUNT(*) FROM funcionario WHERE cpf = %s"
            cursor.execute(sql_select, (cpf,))
            count = cursor.fetchone()[0]
            return count > 0   
        
    def verifica_login_funcionario(self, username, password):
        if self.conexao.is_connected():
            cursor = self.conexao.cursor()
            sql_select = "SELECT password FROM funcionario WHERE username = %s"
            cursor.execute(sql_select, (username,))
            result = cursor.fetchone()
            if result:
                stored_password = result[0]
                return bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8'))
            return False 
#produto
    def cadastraProduto(self, produto):
        if self.conexao.is_connected():
            cursor = self.conexao.cursor()
            sql_insert = (
                "INSERT INTO produto (nome, descricao, valor_custo, valor_venda, id_fornecedor) "
                "VALUES (%s, %s, %s, %s, %s)"
            )
            valores = (produto.nome, produto.descricao, produto.valor_custo, produto.valor_venda, produto.id_fornecedor)
            cursor.execute(sql_insert, valores)
            self.conexao.commit()
            print("Commit efetuado com sucesso")

    def lista_produtos(self):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM produto;")
        return cursor.fetchall()
    
    def consultaProdutoPorID(self, produto_id):
        if self.conexao.is_connected():
            cursor = self.conexao.cursor(dictionary=True)
            sql_select = "SELECT * FROM produto WHERE id = %s"
            cursor.execute(sql_select, (produto_id,))
            resultado = cursor.fetchone()
            cursor.close()
            return resultado
        
    def consultaProdutoPorNome(self, nome):
        if self.conexao.is_connected():
            cursor = self.conexao.cursor(dictionary=True)
            sql_select = "SELECT * FROM produto WHERE nome LIKE %s"
            cursor.execute(sql_select, (f"%{nome}%",))
            resultados = cursor.fetchall()
            cursor.close()
            return resultados
        
    def consultaProdutoPorFornecedor(self, fornecedor_id):
        if self.conexao.is_connected():
            cursor = self.conexao.cursor(dictionary=True)
            sql_select = "SELECT * FROM produto WHERE id_fornecedor = %s"
            cursor.execute(sql_select, (fornecedor_id,))
            resultados = cursor.fetchall()
            cursor.close()
            return resultados
            
#funcionario           
def cadastraFuncionario(self, funcionario):
    if self.conexao.is_connected():
        cursor = self.conexao.cursor()
        sql_insert = (
            "INSERT INTO funcionario (username, password, email, cpf, telefone, endereco, data_nascimento) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s)"
        )
        valores = (funcionario.username, funcionario.password, funcionario.email, funcionario.cpf, funcionario.telefone, funcionario.endereco, funcionario.data_nascimento)
        cursor.execute(sql_insert, valores)
        self.conexao.commit()
        print("Commit efetuado com sucesso")
        
#fornecedor
def cadastraFornecedor(self, fornecedor):
    if self.conexao.is_connected():
        cursor = self.conexao.cursor()
        sql_insert = (
            "INSERT INTO fornecedor (username, password, email, cnpj, telefone, endereco) "
            "VALUES (%s, %s, %s, %s, %s, %s)"
        )
        valores = (fornecedor.username, fornecedor.password, fornecedor.email, fornecedor.cnpj, fornecedor.telefone, fornecedor.endereco)
        cursor.execute(sql_insert, valores)
        self.conexao.commit()
        print("Commit efetuado com sucesso")
            
class Cliente:
    def __init__(self, username: str, password: str, email: str, cpf: str, telefone: str, endereco: str) -> None:
        self.__id: int = None  
        self.__username: str = username
        self.__password: str = password
        self.__email: str = email
        self.__cpf: str = cpf
        self.__telefone: str = telefone
        self.__endereco: str = endereco

    @property
    def id(self):
        return self.__id

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    @property
    def email(self):
        return self.__email

    @property
    def cpf(self):
        return self.__cpf

    @property
    def telefone(self):
        return self.__telefone

    @property
    def endereco(self):
        return self.__endereco

class Produto:
    def __init__(self, nome: str, descricao: str, valor_custo: float, valor_venda: float, id_fornecedor: int) -> None:
        self.__id: int = None
        self.__nome: str = nome
        self.__descricao: str = descricao
        self.__valor_custo: float = valor_custo
        self.__valor_venda: float = valor_venda
        self.__id_fornecedor: int = id_fornecedor

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @property
    def descricao(self):
        return self.__descricao

    @property
    def valor_custo(self):
        return self.__valor_custo

    @property
    def valor_venda(self):
        return self.__valor_venda

    @property
    def id_fornecedor(self):
        return self.__id_fornecedor

class Funcionario:
    def __init__(self, username: str, password: str, email: str, cpf: str, telefone: str, endereco: str) -> None:
        self.__id: int = None
        self.__username: str = username
        self.__password: str = password
        self.__email: str = email
        self.__cpf: str = cpf
        self.__telefone: str = telefone
        self.__endereco: str = endereco
    

    @property
    def id(self):
        return self.__id

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    @property
    def email(self):
        return self.__email

    @property
    def cpf(self):
        return self.__cpf

    @property
    def telefone(self):
        return self.__telefone

    @property
    def endereco(self):
        return self.__endereco





class Pedido:
    def __init__(self, id_cliente: int, id_produto: int, quantidade: int) -> None:
        self.__id: int = None
        self.__id_cliente: int = id_cliente
        self.__id_produto: int = id_produto
        self.__quantidade: int = quantidade

    @property
    def id(self):
        return self.__id

    @property
    def id_cliente(self):
        return self.__id_cliente

    @property
    def id_produto(self):
        return self.__id_produto

    @property
    def quantidade(self):
        return self.__quantidade
   
db = Database()
@app.route('/')
def index():
    produto = Database().lista_produtos()
    return render_template('index.html', produtos = produto)

@app.route('/home')
def home():
    if 'username' not in session:
        flash('Você deve estar logado para acessar esta página.')
        return redirect(url_for('login'))
    produto = Database().lista_produtos()
    return render_template('home.html', produtos = produto)

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('cpf', None)
    flash('Você foi desconectado!')
    return redirect(url_for('login'))



@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        cpf = request.form['cpf']
        telefone = request.form['telefone']
        endereco = request.form['endereco']
        
        if db.verifica_cliente_existente(cpf):
            flash('Cliente já cadastrado com este CPF!')
            return redirect(url_for('cadastro'))
        
        # Hash da senha
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        
        cliente = Cliente(username, hashed_password.decode('utf-8'), email, cpf, telefone, endereco)
        db.cadastraCliente(cliente)
        
        flash('Cadastro realizado com sucesso!')
        
        return redirect(url_for('login')) 

    return render_template('cadastro.html')

@app.route('/funcionario', methods=['GET', 'POST'])
def funcionario():
    if request.method == 'POST':
        Nome_produto = request.form['Nome_produto']
        descricao = request.form['descricao']
        valor_custo = request.form['valor_custo']
        valor_venda = request.form['valor_venda']
        id_fornecedor = request.form['id_fornecedor']

        produto = Produto(Nome_produto, descricao, valor_custo, valor_venda, id_fornecedor)
        db.cadastraProduto(produto)
        
        flash('Cadastro realizado com sucesso!')
        
        return redirect(url_for('funcionario')) 
    return render_template('funcionario.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if db.verifica_login(username, password):
            # Armazena as informações do usuário na sessão
            session['username'] = username
            cursor = db.conexao.cursor()
            cursor.execute("SELECT cpf FROM cliente WHERE username = %s", (username,))
            result = cursor.fetchone()
            session['cpf'] = result[0] if result else 'Desconhecido'
            
            flash('Login bem-sucedido!')
            return redirect(url_for('home'))  # Redireciona para a página inicial
        
        if db.verifica_login_funcionario(username, password):
            # Armazena as informações do usuário na sessão
            session['username'] = username
            cursor = db.conexao.cursor()
            cursor.execute("SELECT cpf FROM funcionario WHERE username = %s", (username,))
            result = cursor.fetchone()
            session['cpf'] = result[0] if result else 'Desconhecido'
            
            flash('Login bem-sucedido!')
            print("Funcionario entrou")
            return redirect(url_for('funcionario'))  # Redireciona para a página inicial
        else:
            flash('Nome de usuário ou senha incorretos!')
            return redirect(url_for('login'))
    
    return render_template('login.html')
if __name__ == '__main__':
    app.run(debug=True)
