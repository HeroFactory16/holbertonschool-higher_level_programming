#!/usr/bin/python3
"""List all State objects from the database passed as argument.

Usage: ./script.py <mysql username> <mysql password> <database name>

Connects to a MySQL server running on localhost:3306 and prints every
row of the ``states`` table, sorted by id, as ``(id, 'name')``.
"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class State(Base):
    """Map the ``states`` table to a Python class.

    Attributes:
        id (int): Primary key of the state (auto-incremented).
        name (str): Name of the state (max 128 characters).
    """

    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
