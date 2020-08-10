#!/usr/bin/python3
""" Adds a state object """

import sqlalchemy
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import (create_engine)


if __name__ == '__main__':
    user = argv[1]
    password = argv[2]
    database = argv[3]

    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                        (user, password, database), pool_pre_ping=True)

    Base.metadata.create_all(eng)
    sess = Session(eng)
    new_state = State(name="Louisiana")
    sess.add(new_state)
    sess.commit()
    print(new_state.id)
    sess.close()
