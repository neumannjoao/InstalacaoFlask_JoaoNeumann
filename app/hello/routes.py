# app/hello/routes.py
from flask import Blueprint, render_template
from ..models import User, db
# Cria um objeto Blueprint. 'hello' é o nome do blueprint.
hello_bp = Blueprint('hello', __name__)
# Define uma rota dentro deste blueprint.
@hello_bp.route('/')
def index():
    usuarios = User.query.all() #['André', 'Rafael', 'Fernando']
    return render_template ('index.html', usuarios = usuarios)