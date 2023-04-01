"""MODELOS DE REPRESENTAÇÃO DO BANCO DE DADOS"""
from .. import db
from .model_class import ParanoicoModel


class Teste(ParanoicoModel, db.Model):
    """MODEL DE EXEMPLO"""

    def __init__(self) -> None:
        super().__init__()
