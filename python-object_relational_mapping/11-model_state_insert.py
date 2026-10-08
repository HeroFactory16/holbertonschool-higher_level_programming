#!/usr/bin/python3
"""List all State objects from the database passed as argument.

Usage: ./script.py <mysql username> <mysql password> <database name>

Connects to a MySQL server running on localhost:3306 and prints every
row of the ``states`` table, sorted by id, as ``id: name``.
"""
import sys
from MySQLdb import *
from sqlalchemy import create_engine, insert, select
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

if __name__ == "__main__":

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
            insert(State)
            .values(name="Louisiana")
        )

        session.execute(query)
        session.commit()

        query = (
            select(State.id)
            .where(State.name == "Louisiana")
        )

        result = session.execute(query).fetchone()
        print(f"{result[0]}")
