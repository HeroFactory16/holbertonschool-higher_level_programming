#!/usr/bin/python3
"""List all State objects whose name matches argv[4]
from the database passed as argument.

Usage: ./script.py <mysql username> <mysql password> <database name>

Connects to a MySQL server running on localhost:3306 and prints every
row of the ``states`` table, sorted by id, as ``(id, 'name')``.
"""
import sys

from MySQLdb import *
from sqlalchemy import Column, Integer, String, create_engine
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
        for state in session.query(State).order_by(State.id).all():
            if state.name == sys.argv[4]:
                print("({}, '{}')".format(state.id, state.name))
