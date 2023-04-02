"""TIPOS PERSONALIZADOS"""
from uuid import uuid4
from sqlalchemy import Column, String
from sqlalchemy.types import TypeDecorator
from werkzeug.security import generate_password_hash


def column_uuid(primary_key=False, unique=True):
    """Coluna para uuid em um model"""
    return Column(String(36),
                  primary_key=primary_key,
                  unique=unique,
                  default=lambda *_: str(uuid4()))


class Password(TypeDecorator):
    """Tipo de String criptografada"""
    impl = String

    def process_bind_param(self, value, dialect):
        """CRIPTOGRAFIA NA ENTRADA DE DADOS"""
        return generate_password_hash(value)

    def process_result_value(self, value, dialect):
        """OCULTAÇÃO NA INFORMAÇÕES DE SAIDA"""
        return "************"


def column_password():
    """Coluna para password em um model"""
    return Column(Password(160))
