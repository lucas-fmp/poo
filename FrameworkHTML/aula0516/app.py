from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    nome = "Usuário"
    return render_template('index.html', nome=nome)  # Passando a variável 'nome'


@app.route('/saudacao/<nome_usuario>')
def saudacao(nome_usuario):
    return render_template('index.html', nome=nome_usuario)  # Passando outra variável
    # obtida da URL


@app.route('/produtos')
def produtos():
    lista_produtos = [
        {'nome': 'Notebook', 'preco': 3500},
        {'nome': 'Mouse', 'preco': 80},
        {'nome': 'Teclado', 'preco': 150},
        {'nome': 'Tablet', 'preco': 1150},
    ]
    return render_template('produtos.html', produtos=lista_produtos)


@app.route('/home')
def home():
    return render_template('home.html')  # Renderiza o template filho home.html


@app.route('/sobre')
def sobre():
    return render_template('sobre.html')  # Renderiza o template filho sobre.html


if __name__ == '__main__':
    app.run(debug=True)
