from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)


# Rota principal será chamada quando digitar http://localhost:5000 no Browser

@app.route('/')
def index():
    dh = datetime.now()
    saida_dh = dh.isoformat(" ", timespec='seconds')
    hora = dh.hour
    cumprimento = "Bom dia"
    if 11 < hora < 19:
        cumprimento = "Boa tarde"
    elif 18 < hora < 24:
        cumprimento = "Boa noite"

    return render_template('index.html', data_hora=saida_dh, cumprimento=cumprimento)


# Rota para mostrar a tabuada de um número passado via URL: http://localhost:5000/tabuada?numero=7
@app.route('/tabuada/<numero>')
def tabuada(numero):
    if not numero.isdigit():
        return "Erro: Informe um número na URL!"

    n = int(numero)
    dados = []
    for contar in range(1, 11):
        dados.append([n, contar, n * contar])

    return render_template('tabuada.html', numero=numero, dados=dados)


@app.route('/imprimir/<nome>')
def imprimir(nome):
    numero_caracteres = len(nome)

    return render_template('imprimir.html', nome=nome, numero_caracteres=numero_caracteres)


@app.route('/fatorial/<numero>')
def fatorial(numero):
    if not numero.isdigit():
        return "Erro: Informe um número na URL!"

    n = int(numero)
    total = 1
    numeros = []
    for num in range(1, n + 1):
        numeros.append([num])
        total *= num

        if num != n:
            numeros.append(['x'])
        else: numeros.append(['='])

    return render_template('fatorial.html', numero=n, numeros=numeros, total=total)


if __name__ == '__main__':
    app.run(debug=True)
