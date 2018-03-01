from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Product, Category, User

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

category1 = Category(name="My first category")
session.add(category1)
session.commit()

product1 = Product(name="My first product", description="Some nice description", category=category1)
session.add(product1)
session.commit()

user1 = User(userid="admin", name="Administrator", password="nimda")
session.add(user1)
session.commit()