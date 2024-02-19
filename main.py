from flask import *
import dao
app = Flask(__name__)


@app.route('/cadastrar', methods=["POST"])
def cadastrar_usuario():
    nome = str(request.form.get('nome'))
    senha = str(request.form.get('senha'))
    if dao.verificar_login(nome, senha):
        return render_template('verificado.html', login=nome.upper())
    else:
        return render_template('index.html')


@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/enviar_pedido', methods=["POST"])
def enviar_pedido():
    tamanho_pedido = request.form.get('tamanho')
    numero_pedido = request.form.get('numero')
    qtde_arroz = request.form.get('quantidade')
    qtde_feijao = request.form.get('feijao')
    proteina = request.form.get('proteina')

    dao.salvar_pedido(numero_pedido,tamanho_pedido,qtde_arroz,qtde_feijao,proteina)

    return render_template('confirmacao_pedido.html')


app.run(debug=True)
