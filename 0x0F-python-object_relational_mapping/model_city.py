#!/usr/bin/python3
"""Start link class to table in database
"""
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer
from sqlalchemy.orm import declarative_base, relationship
from model_state import Base


class City(Base):
    """Defines the state class"""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(128))
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship('State')

    def __init__(self, name, state_id):
        self.name = name
        self.state_id = state_id

    def __repr__(self):
        return f'{self.state.name}: ({self.id}) {self.name}'
