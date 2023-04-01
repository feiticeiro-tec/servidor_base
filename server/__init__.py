"""MODULO DO SERVIDOR"""
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from server.database import init_db


class Servidor(Flask):
    """EXTENÇÃO DA CLASS FLASK"""
    database: SQLAlchemy

    def __init__(self, config):
        super().__init__(__name__)
        self.config_env = config

    def init_config(self):
        """INICIALIZAÇÃO DE CONFIGURAÇÕES DO SERVIDOR"""
        logging.info("CONFIGURANDO O SERVIDOR...")
        self.config.update({
            "DEBUG": self.config_env.DESENVOLVIMENTO,
            "SQLALCHEMY_DATABASE_URI": self.config_env.SQLALCHEMY_DATABASE_URI,
            "TESTING": self.config_env.TESTING,
            "SECRET_KEY": self.config_env.SECRET_KEY
        })

    def init_database(self):
        """INICIALIZAÇÃO DO BANCO DE DADOS"""
        logging.info("INICIALIZANDO O BANCO DE DADOS...")
        with self.app_context():
            self.database = init_db(self)
