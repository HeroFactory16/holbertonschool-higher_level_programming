#!/usr/bin/python3
"""Deletes all states with letter 'a' in their name.

Usage: ./script.py <mysql username> <mysql password> <database name>

Connects to a MySQL server running on localhost:3306 and deletes
any state with the letter 'a' in their name attribute.
"""
import sys
from MySQLdb import *
from sqlalchemy import create_engine, insert, select, update, delete
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
        session.execute(
            delete(State)
            .where(State.name.like("%a%"))
            .execution_options(synchronize_session=False)
        )
        session.commit()
