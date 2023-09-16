#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State("Louisiana")
    session.add(new_state)
    session.commit()
    first_state = (
            session.query(State.id)
            .filter(State.name == "Louisiana").first()[0]
        )
    if first_state is None:
        print('Nothing')
    else:
        print(first_state)