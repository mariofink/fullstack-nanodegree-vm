from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(250))


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    userid = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    password = Column(Text, nullable=False)


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    updated = Column(DateTime)
    name = Column(String(250), nullable=False)
    description = Column(Text)
    user_id = Column(Integer, ForeignKey('user.userid'))
    user = relationship(User)
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)

    @property
    def serialize(self):
        """Return object data in easily serialisable format"""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'user': self.user.userid,
            'category': self.category.name
        }


engine = create_engine('sqlite:///catalog.db')

Base.metadata.create_all(engine)
