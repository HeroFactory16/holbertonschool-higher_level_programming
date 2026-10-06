#!/usr/bin/python3

import sys
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    Base = declarative_base()

    class State(Base):
        __tablename__ = "states"
        id = Column(Integer, primary_key=True)
        name = Column(String(256), nullable=False)

    db = create_engine(f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}", pool_pre_ping=True)
    Session = sessionmaker(bind=db)

    with Session() as session:
        for state in session.query(State).order_by(State.id).all():
            print(f"({state.id}, '{state.name}')")
