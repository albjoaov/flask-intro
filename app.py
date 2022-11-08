from re import X
from unicodedata import name
from flask import Flask, request, render_template
from markupsafe import escape


app = Flask(__name__)

@app.route("/exemplo")
def hello_world():
    return "<p>Olá, mundo!</p>"

# Usando o operador `<>` para pegar o caminho da rota como variavel
@app.route("/user/<nome>")
def dinamica(nome):
    return f"Olá, {nome}!"


@app.route("/soma/<int:a>/<int:b>")
def soma(a, b):
    return str(a + b)


@app.route("/soma-com-query-params")
def soma_query_params():
    query_params = request.args
    soma = int(query_params["a"]) + int(query_params["b"])
    return str(soma)


# The return type must be a string, dict, list, tuple
@app.route("/exemplo-erro")
def exemplo_erro():
    return 110

# Lidando com segurança
@app.route('/insecure-path/<path:subpath>')
def show_insecure_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {(subpath)}'


@app.route('/secure-path/<path:subpath>')
def show_secure_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'


# Lidando com novos métodos HTTP
@app.route("/post", methods=["POST"])
def post():
    body = request.json
    return body

# Lidando com novos métodos HTTP
@app.route("/put", methods=["PUT"])
def put():
    body = request.json
    return body


@app.route("/template")
def template():
    args = request.args
    nome = args["nome"]
    empresa = args["empresa"] == "True"
    return render_template("home.html", nome=nome, empresa=empresa)



if __name__ == "__main__":
    app.run(debug=True)
