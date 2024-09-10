from flask import Blueprint, render_template, request, redirect, url_for
from models.produto import Produto, ProdutoDAO

produto_bp = Blueprint('produto', __name__)

@produto_bp.route('/produtos', methods=['GET'])
def listar_produtos():
    produto_dao = ProdutoDAO()
    produtos = produto_dao.lista_produtos()
    return render_template('lista_produtos.html', produtos=produtos)

@produto_bp.route('/produto/novo', methods=['GET', 'POST'])
def novo_produto():
    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        preco = request.form['preco']
        custo = request.form['custo']
        quantidade_estoque = request.form['quantidade_estoque']

        produto = Produto(nome, descricao, preco, custo, quantidade_estoque)
        produto_dao = ProdutoDAO()
        produto_dao.insere_produto(produto)
        return redirect(url_for('produto.listar_produtos'))
    return render_template('cadastro_produto.html')
