"""MODELOS DE CLASS"""
import logging
from datetime import datetime
from sqlalchemy import Column, Integer, DateTime
from server.database.types import column_uuid
from server.database import db


class ModelBase:
    """MODELO BASE DE METHODS"""

    def save(self):
        """FAZ UM COMMIT NO BANCO"""
        logging.debug(f'COMMIT NO BANCO {self}')
        db.session.commit()

    def add(self):
        """ADICIONA O OBJETO NA SESSAO QUE ATUALIZA A SESSAO"""
        logging.debug(f"ADD {self} NA SESSAO.")
        db.session.add(self)
        db.session.flush()

    def add_save(self):
        """A UNIÃO DO METHODS ADD E SAVE"""
        self.add()
        self.save()


class RestreioModel(ModelBase):
    """MODELO DE RATREIO DE CRIAÇÃO E ATUALIZAÇÃO"""
    dta_criado = Column(DateTime, default=datetime.utcnow)
    dta_update = Column(DateTime,
                        default=datetime.utcnow,
                        onupdate=datetime.utcnow)


class GenericModel(RestreioModel):
    """MODELO GENERICO"""

    id = Column(Integer, primary_key=True)


class ParanoicoModel(RestreioModel):
    """MODELO COM UUID"""
    uuid = column_uuid(primary_key=True)
