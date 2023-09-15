#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from relationship_city import Base, City
from relationship_state import State
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
    state = State('California')
    session.add(state)

    new_city = City('San Francisco', state=state)
    session.add(new_city)
    session.commit()
