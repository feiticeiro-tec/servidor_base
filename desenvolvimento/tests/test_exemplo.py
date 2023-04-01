"""DOCULO DE TESTES"""
import pytest


@pytest.mark.parametrize('a,b,igual', [
    [1, 1, 2],
    [1, 2, 3]
])
def test_soma(number_x: int, number_y: int, igual: int):
    """EXEMPLO DE TESTE"""
    assert number_x + number_y == igual


def test_fixture(on_log):
    """TESTE USANDO FIXTURE. PS: CODIGO COM FALHA"""
    response = on_log()
    assert response == 1
