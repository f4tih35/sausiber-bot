import json
from sqlalchemy import create_engine
from cogs.utils import models


def load_db_config():
    with open('postgresql.json') as f:
        return json.load(f)


def main():
    db = load_db_config()
    print ('Connecting to DB')
    engine = create_engine('postgresql+psycopg2://{}:{}@{}/{}'.format(db['user'], db['password'], db['hostname'], db['database']), echo=True)
    models.Entry.__table__.create(engine, checkfirst=True)


if __name__ == '__main__':
    main()
