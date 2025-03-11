from flask import Flask, render_template, request
from filtros.datas import fmt_dta_br
from util.datas import html_to_python

app = Flask(__name__)

app.jinja_env.filters['fmt_dta_br'] = fmt_dta_br  # Registra o filtro de formatação de data para BR


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


# Rota para mostrar o formulário que recebe duas datas para processamento
@app.route('/form_datas')
def form_datas():
    return render_template('form_datas.html')


# Rota para mostrar os resultados do processamento de datas
@app.route('/datas', methods=['POST'])
def datas():
    dias = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
    data_ini = html_to_python(request.form['data_ini'])
    data_fim = html_to_python(request.form['data_fim'])
    diferenca = data_fim - data_ini
    numero_dias = diferenca.days
    dia_semana_ini = dias[data_ini.weekday()]
    dia_semana_fim = dias[data_fim.weekday()]
    return render_template('datas.html', data_ini=data_ini,
                           data_fim=data_fim,
                           dia_semana_ini=dia_semana_ini, dia_semana_fim=dia_semana_fim,
                           numero_dias=numero_dias)


# Rota para mostrar o formulário que recebe 3 nomes para processamento
@app.route('/form_ordenar')
def form_ordenar():
    return render_template('form_ordenar.html')


# Rota para mostrar nomes ordenados em ordem alfabética
@app.route('/ordenar', methods=['POST'])
def ordenar():
    nomes = [request.form['n1'].lower(), request.form['n2'].lower(), request.form['n3'].lower()]
    nomes_ordenados = sorted(nomes)
    return render_template('ordenar.html', nomes_ordenados=nomes_ordenados)

if __name__ == '__main__':
    app.run(debug=True)
