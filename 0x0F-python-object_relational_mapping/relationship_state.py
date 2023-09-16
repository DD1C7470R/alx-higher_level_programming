#!/usr/bin/python3
"""Start link class to table in database
"""
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class State(Base):
    """Defines the state class"""
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(128))
    cities = relationship('City', back_populates='state')
