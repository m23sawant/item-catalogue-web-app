import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    """
    Registered user information is stored in db
    """
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    
    @property
    def serialize(self):
        return{
                'name':self.name,
                'email':self.email,
                'id':self.id,
                
                
                }


class Categories(Base):
    """
    Different categories are stored in the database
    """
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        return {
            'name': self.name,
            'id': self.id,
        }


class CategoryItem(Base):
    """
    Items in the categories are stored in the databse
    """
    __tablename__ = 'category_item'
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    categories_id = Column(Integer, ForeignKey('categories.id'))
    categories = relationship(Categories, single_parent=True,cascade="delete")
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
        }

engine = create_engine('sqlite:///catalogs.db')


Base.metadata.create_all(engine)
