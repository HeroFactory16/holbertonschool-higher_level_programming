#!/usr/bin/python3
"""List all State objects whose name matches argv[4]
from the database passed as argument.

Usage: ./script.py <mysql username> <mysql password> <database name>

Connects to a MySQL server running on localhost:3306 and prints every
row of the ``states`` table, sorted by id, as ``(id, 'name')``.
"""
import sys

from MySQLdb import *
from sqlalchemy import Column, Integer, String, create_engine, select
from sqlalchemy.orm import declarative_base, sessionmaker

if __name__ == "__main__":
    Base = declarative_base()

    class State(Base):
        """Map the ``states`` table to a Python class.

        Attributes:
            id (int): Primary key of the state (auto-incremented).
            name (str): Name of the state (max 256 characters).
        """

        __tablename__ = "states"
        id = Column(Integer, primary_key=True)
        name = Column(String(256), nullable=False)

    class City(Base):
        """Map the ``city`` table to a Python class.

        Attributes:
            id (int): Primary key of the city (auto-incremented).
            state_id (int): Foreign key from the state table.
            name (str): Name of the state (max 256 characters).
        """

        __tablename__ = "cities"
        id = Column(Integer, primary_key=True)
        state_id = Column(Integer, nullable=False)
        name = Column(String(256), nullable=False)

    # Build the connection URL from the command-line arguments:
    # argv[1] = user, argv[2] = password, argv[3] = database name
    db = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    Session = sessionmaker(bind=db)

    with Session() as session:
        query = (
            select(City.id, City.name, State.name)
            .join(State, City.state_id == State.id)
            .order_by(City.id)
        )
        for city_id, city_name, state_name in session.execute(query):
            print("({}, '{}', '{}')".format(
                    city_id,
                    city_name,
                    state_name
                    ))
