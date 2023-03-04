from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import os

load_dotenv()

DATABASE_URL = os.getenv("URL_DATA_BASE")

engine = create_engine(DATABASE_URL)

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




