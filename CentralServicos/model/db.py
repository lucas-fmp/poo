from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base


class Database:
    # mysql+pymysql://<usuario>:<senha>@<host>:<porta>/<nome_do_banco>?charset=utf8mb4
    USER = 'root'
    PASSWORD = 'ceub123456'
    HOST = 'localhost'
    PORT = 3306
    DATABASE = 'db_central_servicos'

    DB_URL = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}?charset=utf8mb4"

    # Criar o mapeamento do banco de dados db_central_servico
    def __init__(self):
        self.engine = create_engine(self.DB_URL)
        self.DB = automap_base()
        self.DB.prepare(autoload_with=self.engine)
        self.session_factory = sessionmaker(bind=self.engine)
        self.ses = self.session_factory()

    def get_session(self):
        return self.ses
