"""MODELO DE BLUEPRINTS"""
import logging
from flask import Flask, Blueprint

base = Blueprint('blueprint', __name__,
                 template_folder='templates',
                 static_folder='static')


def init_blueprints(app: Flask) -> None:
    """INICIALIZAÇÃO DAS BLUEPRINTS"""
    logging.info(
        "VINCULANDO A BLUEPRINT BASE AO APP E CRIANDO OS OUTROS BLUEPRINTS")
    from server.blueprints import routes
    app.register_blueprint(base)
