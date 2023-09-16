#!/usr/bin/python3
"""
Module that contains the class definition of a State
and an instance Base = declarative_base()
"""
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sys import argv

Base = declarative_base()


class State(Base):
    """
    Represents a state in the database.
    """
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(128))
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship('State', back_populates='cities')
