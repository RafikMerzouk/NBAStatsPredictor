from sqlalchemy.ext.declarative import declarative_base
import os

Base = declarative_base()

db_host = os.getenv('POSTGRES_HOST')
db_name = os.getenv('POSTGRES_DB')
db_user = os.getenv('POSTGRES_USER')
db_pass = os.getenv('POSTGRES_PASSWORD')

connection_string = f'postgresql://{db_user}:{db_pass}@{db_host}/{db_name}'