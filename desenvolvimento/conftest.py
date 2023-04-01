"""CONFIGURAÇÃO DO PYTEST"""
import logging
import pytest


@pytest.fixture
def on_log():
    """Fixture Exemplo"""
    return lambda *x:logging.info('Log Fixure')
