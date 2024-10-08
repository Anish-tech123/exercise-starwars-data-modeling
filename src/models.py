import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False)
    favorites = relationship("Favorite", backref="user")

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
        }
    
class Planet (Base):
    __tablename__ ='planet'
    id = Column(Integer, primary_key=True)
    name=Column(String(50), nullable=False)
    description=Column(String(500))
    planet_image=Column(String(512))
    favorites=relationship("Favorite", backref="planet") 

class Character (Base):
    __tablename__ ='character'
    id = Column(Integer, primary_key=True)
    name=Column(String(50), nullable=False)
    description=Column(String(500))
    character_image=Column(String(512))
    favorites=relationship("Favorite", backref="character")

class Favorite (Base):
    __tablename__ ='favorite'
    id = Column(Integer, primary_key=True)
    
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False) 
    character_id = Column(Integer, ForeignKey("character.id"), nullable=True) 
    planet_id = Column(Integer, ForeignKey("planet.id"), nullable=True) 



    

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
