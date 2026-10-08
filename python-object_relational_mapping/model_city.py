#!/usr/bin/python3
"""
Blueprint for City objects.
"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class City(Base):
    """Map the ``cities`` table to a Python class.

    Attributes:
        id (int): Primary key of the city (auto-incremented).
        state_id (int): Foreign key of the state.
        name (str): Name of the city (max 128 characters).
    """

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False)
