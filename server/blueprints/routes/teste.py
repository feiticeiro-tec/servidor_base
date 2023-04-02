from flask import Blueprint,render_template
from server.blueprints import base

teste = Blueprint('teste',__name__)

base.register_blueprint(teste)

@teste.route('/')
def view():
    return render_template('teste.html')