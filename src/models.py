import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}


class Usuario(Base):
    __tablename__ = 'Usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_name = Column(String(250), nullable=False)
    phone = Column(String(250), nullable=False)
    mail = Column(String(250), nullable=False)


class Post(Base):
    __tablename__ = 'Post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    post_description = Column(String(250), nullable=False)
    post_omment = Column(String(250), nullable=False)
    post_counterlikes = Column(Integer, primary_key=True)
    post_date = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('Usuario.id'))
    person = relationship(Usuario)


class Comment(Base):
    __tablename__ = 'Comment'
    id = Column(Integer, primary_key=True)
    user_comment = Column(String(250), nullable=False)
    post_comment = Column(String(250), nullable=False)
    date_comment = Column(Integer, primary_key=True)
    user_like = Column(String(250), nullable=False)
    text_comment = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('Usuario.id'))
    person = relationship(Usuario)


class Recomment(Base):
    __tablename__ = 'Recomment'
    id = Column(Integer, primary_key=True)
    user_recomment = Column(String(250), nullable=False)
    text_recomment = Column(String(250), nullable=False)
    date_recomment = Column(Integer, primary_key=True)
    user_like = Column(String(250), nullable=False)
    user_datelike = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('Usuario.id'))
    person = relationship(Usuario)

    def to_dict(self):
        return {}

# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
