from flask import Blueprint, render_template, request, redirect, url_for
from models.cliente import Cliente, ClienteDAO

cliente_bp = Blueprint('cliente', __name__)

@cliente_bp.route('/produtos', methods=['GET'])
def listar_produtos():
    cliente_dao = ClienteDAO()
    clientes = cliente_dao.lista_clientes()
    return render_template('lista_produtos.html', produtos=clientes)

#completar essa classe. 