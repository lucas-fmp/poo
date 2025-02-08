from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///produtos.db'
db = SQLAlchemy(app)


class Produto(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   nome = db.Column(db.String(50), nullable=False)
   preco = db.Column(db.Float, nullable=False)


with app.app_context():
   db.create_all()


   if not Produto.query.first():
       db.session.add_all([
           Produto(nome='Camiseta', preco=39.90),
           Produto(nome='Calça Jeans', preco=99.90),
           Produto(nome='Tênis', preco=329.90)
       ])
       db.session.commit()


@app.route('/')
def index():
   produtos = Produto.query.all()
   return render_template('lista_produtos.html', produtos=produtos)


if __name__ == '__main__':
   app.run(debug=True)
