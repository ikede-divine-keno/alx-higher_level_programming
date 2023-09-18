#!/usr/bin/python3
"""module to define the states table"""
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import *

_metadata = MetaData()
Base = declarative_base(metadata=_metadata)


class State(Base):
    """ class fto define the states table objects """
    __tablename__ = 'states'

    id = Column('id', Integer, unique=True, primary_key=True, nullable=False)
    name = Column('name', String(128), nullable=False)
    cities = relationship("City",  backref="states")
