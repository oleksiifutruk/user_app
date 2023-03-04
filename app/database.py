from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import os



DB_USER = os.environ['DB_USER']
DB_PASSWORD = os.environ['DB_PASSWORD']
DB_NAME = os.environ['DB_NAME']
DB_HOST = os.environ['DB_HOST']
DB_PORT = os.environ['DB_PORT']

engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')



SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()



data_folder = os.path.join(os.path.dirname(__file__), '..', 'data')
db_sql = os.path.join(data_folder, 'db.sql')
users_sql = os.path.join(data_folder, 'users.sql')

def sql_table():
    with open(db_sql, "r") as f:
        sql_tabl = f.read()
    with engine.connect() as connection:
        connection.execute(sql_tabl)

def sql_add_data_users():
    with open(users_sql, "r") as f:
        sql_add = f.read()
    with engine.connect() as connection:
        result = connection.execute('SELECT COUNT(*) FROM users')
        count = result.scalar()
        if count == 0:
            connection.execute(sql_add)




