# app/__init__.py
from flask import Flask
from .hello.routes import hello_bp # Importa o blueprint que criamos
from .models import db


def create_app():
    # Cria a instância da aplicação Flask
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hello.db'
    db.init_app(app)

    with app.app_context():
        db.create_all()

    # Registra o blueprint na aplicação
    app.register_blueprint(hello_bp)
    # Retorna a aplicação configurada
    return app