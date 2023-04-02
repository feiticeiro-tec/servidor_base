"""MODELOS DE REPRESENTAÇÃO DO BANCO DE DADOS"""
from sqlalchemy import Column, String
from server.database import db
from server.database.models.model_class import ParanoicoModel
from server.database.types import column_password


class Usuario(ParanoicoModel, db.Model):
    """MODEL DE EXEMPLO"""
    __tablename__ = 'Usuario'

    username = Column(String(100), unique=True)
    password = column_password()

    def __init__(self) -> None:
        super().__init__()

    def insert_login(self, username, password):
        self.password = password
        self.username = username
