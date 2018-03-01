from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(250))


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(Text)
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    userid = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    password = Column(Text, nullable=False)

engine = create_engine('sqlite:///catalog.db')

Base.metadata.create_all(engine)
