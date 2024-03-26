import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable = False)
    password = Column(String(250),nullable = False)
    fecha_suscripcion = Column(DateTime)
    nro_maximo = Column(Integer)

class Planeta(Base):
    __tablename__ = 'planeta'
    id = Column(Integer, primary_key = True)
    name = Column(String(250),nullable = False)
    descripcion = Column(String(250), nullable = False)

    # user_id = Column(Integer, ForeignKey('user.id'))
    # user = relationship(User)
    

class FavoritePlaneta(Base):
     __tablename__ = 'favorite_planeta'
     id = Column(Integer, primary_key = True)

     user_id = Column(Integer, ForeignKey('user.id'))
     user = relationship('User')


     planeta_id = Column(Integer, ForeignKey('planeta.id'), nullable=True)
     planeta = relationship('Planeta') 


class FavoritePersonaje(Base):
     __tablename__ = 'favorite_personaje'
     id = Column(Integer, primary_key = True)

     user_id = Column(Integer, ForeignKey('user.id'))
     user = relationship('User')


     personaje_id = Column(Integer, ForeignKey('personaje.id'), nullable=True)
     personaje = relationship('Personaje') 

class Personaje(Base):
    __tablename__ = 'personaje' 
    id = Column(Integer, primary_key = True)
    name = Column(String(250),nullable = False)
    especie = Column(String(250), nullable = True)

    # user_id = Column(Integer, ForeignKey('user.id'))
    # user = relationship(User)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
