from sqlalchemy import create_engine

engine = None


def load_db(user, password, hostname, dbname):
    global engine
    engine = create_engine('postgresql+psycopg2://{}:{}@{}/{}'.format(user, password, hostname, dbname))
