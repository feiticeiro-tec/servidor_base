"""API DA APLICAÇÃO"""
import logging
from flask_restx import Api
from flask import Flask

api = Api(doc='/api/doc',prefix='/api')


def init_api(app: Flask):
    """INICIALIZAÇÃO DA API"""
    logging.debug("VINCULANDO A API AO APP E CRIANDO OS ROTAS")
    from server.api import routes
    api.init_app(app)
    return api
