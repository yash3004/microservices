import sqlalchemy
import yaml


class Database:
    def __init__(self):
        self._engine: sqlalchemy.Engine = None
        self._session_maker = None

    def init(self, config):
        user = config.get("username")
        pass_ = config.get("password")
        host = config.get("host")
        port = config.get("port")
        name = config.get("database")

        dsn = f"mysql+pymysql://{user}:{pass_}@{host}:{port}/{name}"
        self._engine = sqlalchemy.create_engine(dsn)
        self._session_maker = sqlalchemy.orm.sessionmaker(bind=self._engine)

    def session(self):
        return self._session_maker()


def resolve_config():
    with open('config.yaml', 'r') as cfg_file:
        return yaml.load(cfg_file)
