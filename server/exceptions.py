"""ARQUIVOS DE EXCEPTIONS"""


class ExceptionBase(Exception):
    """Exeção Base Para Colorir o Error jhbskdgvjashksmdgvajshgdvajolasdahsgdvajshdgvajsgdvjahsgdv"""
    COLOR = '\033[1;31m'
    RESET = '\033[0m'

    def __str__(self) -> str:
        return f"{self.COLOR}{self.__class__.__name__}"\
            "{self.RESET}: {self.args[0]}"


class EnvError(ExceptionBase):
    """ERROR NAS VARIAVEIS DE AMBIENTE"""

    def __init__(self, *args: object) -> None:
        super().__init__(*args)
