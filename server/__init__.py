"""MODULO DO SERVIDOR"""
from flask import Flask


class Servidor(Flask):
    """EXTENÇÃO DA CLASS FLASK"""

    def __init__(self, config):
        super().__init__(__name__)
        self._config = config

    def init_config(self):
        """INICIALIZAÇÃO DE CONFIGURAÇÕES DO SERVIDOR"""
        self.config.update({
            "DEBUG": self._config.DESENVOLVIMENTO,
            "SQLLACHEMY_DATABASE_URI": self._config.SQLALCHEMY_DATABASE_URI,
            "TESTING": self._config.TESTING,
            "SECRET_KEY": self._config.SECRET_KEY
        })
