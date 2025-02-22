from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)


# Rota principal será chamada quando digitar http://localhost:5000 no Browser
@app.route('/')
def index():
    return render_template('index.html')


# Rota para mostrar o formulário que recebe dois números para fazer os cálculos aritméticos
@app.route('/form_calc')
def form_calc():
    return render_template('form_calc.html')


# Rota para mostrar os resultados da calculadora
@app.route('/calc', methods=['POST'])
def calc():
    n1 = int(request.form['n1'])
    n2 = int(request.form['n2'])
    soma = n1 + n2
    subtracao = n1 - n2
    multiplicacao = n1 * n2
    divisao = n1 / n2
    return render_template('calc.html', n1=n1, n2=n2, soma=soma, subtracao=subtracao,
                           multiplicacao=multiplicacao, divisao=divisao)


@app.route('/form_texto')
def form_texto():
    return render_template('form_texto.html')


# Rota para mostrar os resultados da calculadora
@app.route('/texto', methods=['POST'])
def texto():
    texto = request.form['texto']
    # processamentos
    num_caracteres = len(texto)
    maiusculo = texto.upper()
    minusculo = texto.lower()
    return render_template('texto.html', texto=texto, num_caracteres=num_caracteres, maiusculo=maiusculo,
                           minusculo=minusculo)


if __name__ == '__main__':
    app.run(debug=True)
