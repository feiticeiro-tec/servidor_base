"""BANCO DE DADOS"""
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_db(app: Flask):
    """INICIALIZAÇÃO E VINCULO DO BANCO DE DADOS"""
    from server.database import models
    logging.debug("VINCULANDO O BANCO AO APP E CRIANDO OS TABELAS")
    db.init_app(app)
    db.create_all()
    return db
