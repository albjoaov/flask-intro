from flask import Blueprint, request, render_template
from markupsafe import escape

example_bp = Blueprint("example", __name__, url_prefix="/example")

@example_bp.route("/exemplo")
def hello_world():
    return "<p>Olá, mundo!</p>"

# Usando o operador `<>` para pegar o caminho da rota como variavel
@example_bp.route("/user/<nome>")
def dinamica(nome):
    return f"Olá, {nome}!"


@example_bp.route("/soma/<int:a>/<int:b>")
def soma(a, b):
    return str(a + b)


@example_bp.route("/soma-com-query-params")
def soma_query_params():
    query_params = request.args
    soma = int(query_params["a"]) + int(query_params["b"])
    return str(soma)


# The return type must be a string, dict, list, tuple
@example_bp.route("/exemplo-erro")
def exemplo_erro():
    return 110

# Lidando com segurança
@example_bp.route('/insecure-path/<path:subpath>')
def show_insecure_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {(subpath)}'


@example_bp.route('/secure-path/<path:subpath>')
def show_secure_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'


# Lidando com novos métodos HTTP
@example_bp.route("/post", methods=["POST"])
def post():
    body = request.json
    return body

# Lidando com novos métodos HTTP
@example_bp.route("/put", methods=["PUT"])
def put():
    body = request.json
    return body


@example_bp.route("/template")
def template():
    args = request.args
    nome = args["nome"]
    empresa = args["empresa"] == "True"
    return render_template("home.html", nome=nome, empresa=empresa)
