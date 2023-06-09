"""MODULO DO SERVIDOR"""
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
from server.database import init_db
from server.api import init_api
from server.blueprints import init_blueprints


class Servidor(Flask):
    """EXTENÇÃO DA CLASS FLASK"""
    database: SQLAlchemy
    api: Api

    def __init__(self, config) -> None:
        super().__init__(__name__)
        self.config_env = config

    def init_config(self) -> None:
        """INICIALIZAÇÃO DE CONFIGURAÇÕES DO SERVIDOR"""
        logging.info("CONFIGURANDO O SERVIDOR...")
        self.config.update({
            "DEBUG": self.config_env.DESENVOLVIMENTO,
            "SQLALCHEMY_DATABASE_URI": self.config_env.SQLALCHEMY_DATABASE_URI,
            "TESTING": self.config_env.TESTING,
            "SECRET_KEY": self.config_env.SECRET_KEY
        })

    def init_database(self) -> None:
        """INICIALIZAÇÃO DO BANCO DE DADOS"""
        logging.info("INICIALIZANDO O BANCO DE DADOS...")
        with self.app_context():
            self.database = init_db(self)

    def init_api(self) -> None:
        """INICIALIZAÇÃO DA API JUNTO AS SUAS ROTAS """
        logging.info("INICIALIZANO A API")
        with self.app_context():
            self.api = init_api(self)

    def init_blueprints(self) -> None:
        """INICIALIZAÇÃO DAS BLUEPRINTS"""
        logging.info("INICIANDO AS BLUEPRINT")
        with self.app_context():
            init_blueprints(self)
