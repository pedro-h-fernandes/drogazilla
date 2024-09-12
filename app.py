from flask import Flask, render_template
from models.produto import ProdutoDAO
from routes.produto import produto_bp

app = Flask(__name__)

# Registro do blueprint de produtos
app.register_blueprint(produto_bp)

@app.route('/')
def home():
    produto_dao = ProdutoDAO()
    produtos = produto_dao.lista_produtos()
    print("aqui")
    return render_template('home.html', produtos=produtos)
if __name__ == '__main__':
    app.run(debug=True)
