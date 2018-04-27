from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    'postgresql+psycopg2://catalog:catalog@localhost/catalog')

DBSession = sessionmaker(bind=engine)
session = DBSession()
