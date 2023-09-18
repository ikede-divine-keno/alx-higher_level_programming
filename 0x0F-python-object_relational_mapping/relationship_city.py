#!/usr/bin/python3
"""model to define the cities table"""
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import *
from relationship_state import Base


class City(Base):
    """ class fto define the states table objects """
    __tablename__ = 'cities'

    id = Column('id', Integer, unique=True, primary_key=True, nullable=False)
    name = Column('name', String(128), nullable=False)
    state_id = Column('state_id', Integer,
                      ForeignKey("states.id"), nullable=False)
