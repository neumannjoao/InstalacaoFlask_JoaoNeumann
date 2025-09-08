# app/hello/routes.py
from flask import Blueprint, render_template, request, redirect
from ..models import User, db
# Cria um objeto Blueprint. 'hello' é o nome do blueprint.
hello_bp = Blueprint('hello', __name__)
# Define uma rota dentro deste blueprint.
@hello_bp.route('/')
def index():
    usuarios = User.query.all() #['André', 'Rafael', 'Fernando']
    return render_template ('index.html', usuarios = usuarios)

@hello_bp.route('/novousuario', methods=['POST'])
def novoUsuario():
    nome_usuario = request.form('nome_usuario')

    novo_usuario= User(username = nome_usuario)

    db.session.add(novo_usuario)
    db.session.commit()
    return redirect('/')