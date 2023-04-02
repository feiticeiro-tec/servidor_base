"""ARQUIVO DA CLASS DE CONFIGURAÇÃO DO SERVIDOR"""
import os
import logging
from urllib.parse import quote_plus
from typing import Any
from dotenv import load_dotenv
from server.exceptions import EnvError


class Config():
    """CLASS DE CONFIGURAÇÃO DO SERVIDOR"""
    SQLALCHEMY_DABASE_URI: str = None
    DESENVOLVIMENTO: bool = None
    COLOR_RESET = "\033[0m"
    COLOR_RED = "\033[1;31m"
    COLOR_YELLOW = "\033[1;33m"
    COLOR_BLUE = "\033[1;34m"
    COLOR_GREEN = "\033[32m"

    def __init__(self) -> None:
        self.set_desenvolvimento()
        self.show_modo()

    def show_modo(self, label=' ') -> None:
        """MOSTRA NO CONSOLE O MODO ATUAL"""
        logging.debug('MOSTRANDO NA TELA O MODO ATUAL')
        msg = '{cor}{message:~^100}{reset}'

        if getattr(self, 'DESENVOLVIMENTO'):
            msg = msg.format(
                cor=self.COLOR_YELLOW,
                message=f" MODO DE DESENVOLVIDOMENTO{label}",
                reset=self.COLOR_RESET
            )
        else:
            msg = msg.format(
                cor=self.COLOR_RED,
                message=f" MODO DE PRODUÇÃO{label}",
                reset=self.COLOR_RESET
            )
        print(msg)

    def load_files_env(self) -> None:
        """LER AS ENVS EM AQUIVOS"""
        if getattr(self, 'DESENVOLVIMENTO'):
            self.color_levels()
            has_file = load_dotenv('.env.dev')
            if not has_file:
                logging.warning(
                    'ARQUIVO DE VARIAVEIS DE DESENVOLVIMENTO NÃO DEFINIDA'
                )
                input('PRECIONE QUALQUER TECLA PARA CONTINUE MESMO ASSIM:\n')
        else:
            has_file = load_dotenv('.env.prod')
            load_dotenv('.env.prod')

        logging.debug(f'FILE ENV READ {has_file}')

    def env_requireds(self) -> None:
        """FAZ A LEITURA DOS"""
        logging.debug('INICIANDO A LEITURA DE ENVS OBRIGATORIAS')
        self.load_env_generic(
            envname='TESTING',
            choices={
                'True': True,
                'False': False
            }
        )

        self.load_env_generic('SECRET_KEY')

        self.show_modo(' REQUIREMENTS CARREGADOS ')

    def init(self) -> None:
        """INICIALIZADOR DAS CONFIGURAÇÕES"""
        self.load_files_env()
        self.env_requireds()

        logging.info('ENV REQUIREMENTS OKAY')

    @staticmethod
    def add_color_level(color: str, level: Any) -> None:
        """COLOCAR A COR NO LEVEL DO LOG"""
        reset = "\033[0m"
        logging.addLevelName(
            level, f'{color}{logging.getLevelName(level)}{reset}')

    def color_levels(self,
                     error: str = None,
                     critical: str = None,
                     warning: str = None,
                     info: str = None,
                     debug: str = None) -> None:
        """COLOCAR AS CORES NO LEVELS DE LOG"""
        logging.debug('DEFININDO AS CORES DE LOG')
        self.add_color_level(error or self.COLOR_RESET, logging.ERROR)
        self.add_color_level(critical or self.COLOR_RESET, logging.CRITICAL)
        self.add_color_level(warning or self.COLOR_YELLOW, logging.WARNING)
        self.add_color_level(info or self.COLOR_BLUE, logging.INFO)
        self.add_color_level(debug or self.COLOR_GREEN, logging.DEBUG)

    @staticmethod
    def value_on_env(envname: str) -> str:
        """PEGA UM VALOR DA ENV SE NAO ACHAR LEVANTA UM ERRO -> EnvError."""
        try:
            return os.environ[envname]
        except Exception as error:
            raise EnvError(f'{envname} NÃO DEFINIDO!') from error

    @staticmethod
    def check_value_in_choice(value: Any, envname: str, choices: list | dict) -> None:
        """VERIFICA SE O VALOR ESTAR NA CHOICE
        SE NAO ESTIVER LEVANTA UM ERROR -> EnvError"""
        if choices and value not in choices:
            raise EnvError(
                f'{envname}:{value} Invalido. CHOICES: {choices}')

    @staticmethod
    def create_connection_string(
            server,
            database,
            username,
            password,
            driver='{ODBC Driver 17 for SQL Server}') -> str:
        """CRIAR A URL DE CONECXÃO COM O BANCO DE DADOS"""
        conn_str = f"Driver={driver};"\
            f"Server={server};"\
            f"Database={database};"\
            f"UID={username};"\
            f"PWD={password}"
        quoted_conn_str = quote_plus(conn_str)
        uri = f'mssql+pyodbc:///?odbc_connect={quoted_conn_str}'

        return uri

    @staticmethod
    def value_on_choice(value: Any, choice: list | dict = None) -> Any:
        """PEGA O VALOR REFERENTE AO CHOICE or raise EnvError"""
        if isinstance(choice, list):
            return value
        elif isinstance(choice, dict):
            return choice[value]
        return value

    def env_valid(self, envname: str, choices: list | dict) -> str:
        """PEGAR O VALOR DA ENV E PEGAR O VALOR VALIDO CORESPONDENTE"""
        value = self.value_on_env(envname=envname)
        self.check_value_in_choice(
            value=value,
            envname=envname,
            choices=choices
        )
        return value

    def load_env(self,
                 envname: str,
                 on_load_value_valid: callable,
                 on_value_in_choice: callable,
                 choices: list | dict = None,
                 ) -> None:
        """FAZ AS CHAMADAS DE PERGAR E CAPTURAR O VALOR E DEFINE NO OBJETO O VALOR"""
        logging.debug(f'LOAD ENV {envname}')
        value = on_load_value_valid(
            envname=envname,
            choices=choices
        )
        value = on_value_in_choice(value, choices)
        setattr(self, envname, value)

    def load_env_generic(self, envname: str, choices: list | dict = None) -> None:
        """FAZ UMA CHAMADA COM A VALIDAÇÃO GENERICA DO OBJETO"""
        logging.debug(f"LOAD GENERIC ENV {envname}")
        return self.load_env(
            envname=envname,
            on_load_value_valid=self.env_valid,
            on_value_in_choice=self.value_on_choice,
            choices=choices
        )

    def set_desenvolvimento(self) -> None:
        """COLOCA O VALOR NA VARIAVEL DESENVOLVIMENTO DE ACORDO COM O VALOR EM AMBIENTE"""
        logging.debug('LEITURA DE AMBIENTE')
        self.load_env_generic('AMBIENTE', ['DESENVOLVIMENTO', 'PRODUCAO'])
        dev = True if getattr(self, 'AMBIENTE') == 'DESENVOLVIMENTO' else False
        setattr(self, 'DESENVOLVIMENTO', dev)

    def load_envs_generic(self, *envnames: str) -> None:
        """PEGAR OS VALORES DA ENV"""
        for envname in envnames:
            self.load_env_generic(envname)

    def load_env_database(self, uri: str = None) -> None:
        """LER AS VARIAVEIS DE AMBIENTE E CRIA A URI DE CONEXÃO DO BANCO."""
        logging.info('GERANDO URI DE CONEXÃO')

        if uri:
            setattr(self, 'SQLALCHEMY_DATABASE_URI', uri)
            os.environ['SQLALCHEMY_DATABASE_URI'] = uri
            logging.info('URI INFORMADA FOI COLOCADA NA ENV!')
            return

        self.load_envs_generic(
            'DB_SERVER',
            'DB_BANCO',
            'DB_USUARIO',
            'DB_SENHA',
            'DB_DRIVER'
        )

        uri = self.create_connection_string(
            server=getattr(self, 'DB_SERVER'),
            database=getattr(self, 'DB_BANCO'),
            username=getattr(self, 'DB_USUARIO'),
            password=getattr(self, 'DB_SENHA'),
            driver=getattr(self, 'DB_DRIVER')
        )
        setattr(self, 'SQLALCHEMY_DATABASE_URI', uri)
        logging.info('URI DE CONEXÃO FOI COLOCADA NA ENV!')
