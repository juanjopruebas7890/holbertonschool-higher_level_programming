#!/usr/bin/python3
""" Delte an object """


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
    del = sess.query(State).order_by(State.id).all()
    for row in del:
        if 'a' in row.name:
            sess.delete(row)
    sess.commit()
    sess.close()
