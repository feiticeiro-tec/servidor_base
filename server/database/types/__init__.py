"""TIPOS PERSONALIZADOS"""
from uuid import uuid4
from sqlalchemy import Column, String


def column_uuid(primary_key=False, unique=True):
    return Column(String(36), primary_key=primary_key, unique=unique, default=lambda *_: str(uuid4()))
