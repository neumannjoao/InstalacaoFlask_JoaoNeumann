# app/hello/routes.py
from flask import Blueprint, render_template
# Cria um objeto Blueprint. 'hello' é o nome do blueprint.
hello_bp = Blueprint('hello', __name__)
# Define uma rota dentro deste blueprint.
@hello_bp.route('/')
def index():
    usuarios = ['André', 'Rafael', 'Fernando']
    return render_template ('index.html', usuarios = usuarios)