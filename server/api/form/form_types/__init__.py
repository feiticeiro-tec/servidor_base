"""TYPOS E TRATAMENTOS DE ENTRADA"""

def string(strip: bool = True) -> callable:
    """TYPE DE STRING PARA O FORM"""
    def inner(value: str) -> None | str:
        """VALIDAÇÃO DA STRING"""
        value = str(value)
        if strip:
            value = value.strip()
        if not value:
            return
        return value
    return inner
