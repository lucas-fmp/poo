from flask import Flask, render_template, session, request
from opcoes.combos import ComboSetor, ComboLocal
from opcoes.cards import CardServico
from opcoes.tabelas import TabelaServico

app = Flask(__name__)
app.secret_key = 'senha'


@app.route("/")
def index():
    session['usuario'] = 'Administrador'
    return render_template("base.html", titulo="Página de Início", usuario="ADM")


@app.route("/combo_close")
def combo_close():
    cb_setor = ComboSetor()
    cb_setor_filter = ComboSetor()
    return render_template("combos/combo_close.html", titulo="ComboBox Fechada",
                           cb_setor=cb_setor.get_cb_all(),
                           cb_setor_filter=cb_setor_filter.get_cb_filter("Fin"))


@app.route("/combo_open")
def combo_open():
    cb_local = ComboLocal()
    cb_local_filter = ComboLocal()
    return render_template("combos/combo_open.html", titulo="ComboBox Aberta",
                           cb_local=cb_local.get_cb_all(),
                           cb_local_filter=cb_local_filter.get_cb_filter("1"))


@app.route("/cards")
def cards():
    card = CardServico()
    cb_servico = card.get_cb_servico()
    return render_template("cards/cards.html", titulo="Cards de Serviços", cb_servico=cb_servico)


@app.route("/card_aberto", methods=["GET"])
def card_aberto():
    id = request.args.get('value')
    card = CardServico()
    c = card.get_card(id)
    return c


@app.route("/card_fechado", methods=["GET"])
def card_fechado():
    id = request.args.get('value')
    card = CardServico()
    c = card.get_cardDialog(id)
    return c


@app.route("/tabela")
def tabela():
    return render_template("tables/tables.html", titulo="Tabelas de Serviços")


@app.route("/table_basic", methods=["GET"])
def table_basic():
    tabela = TabelaServico()
    return tabela.get_table_basic()


@app.route("/table_striped", methods=["GET"])
def table_striped():
    tabela = TabelaServico()
    return tabela.get_table_striped()


@app.route("/table_hover", methods=["GET"])
def table_hover():
    tabela = TabelaServico()
    return tabela.get_table_hover()


if __name__ == "__main__":
    app.run(debug=True)
