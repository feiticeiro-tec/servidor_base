"""INICIALIZAÇÃO DA APLICAÇÃO"""
import logging
from server import Servidor
from server.config import Config

logging.basicConfig(
    format='%(levelname)s - %(asctime)s - %(name)s - %(funcName)s\n%(message)s\n',
    level=logging.DEBUG
)

conf = Config()
conf.init()
conf.load_env_database(uri='sqlite:///db.db')

app = Servidor(conf)
app.init_config()
app.init_database()
app.init_api()
app.init_blueprints()

app.config_env.show_modo(' ONLINE ')
