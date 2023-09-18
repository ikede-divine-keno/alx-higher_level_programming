#!/usr/bin/python3
""" all State objects from the database hbtn_0e_6_usa"""
import sys
from sqlalchemy.orm import *
from sqlalchemy import *
from model_state import State, Base
from model_city import City


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    session = Session(bind=engine)
    city_alias = aliased(City)
    query = session.query(State.name, city_alias.id, city_alias.name)\
                   .filter(State.id == city_alias.state_id)\
                   .order_by(city_alias.id)
    for row in query:
        print(f"{row[0]}: ({row[1]}) {row[2]}")
