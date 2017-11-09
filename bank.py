from sqlalchemy import create_engine

from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation, sessionmaker

import os
if os.path.exists("bank.db"):
    os.remove("bank.db")

engine = create_engine('sqlite:///bank.db')
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    firstname = Column(String(255), nullable=False)

    def __init__(self, firstname=None):
        self.firstname = firstname

# engine = create_engine('sqlite:///:memory:')
# engine = create_engine('mysql+mysqlconnector://test:12345678@localhost/test')

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

m1 = User("Robocop")
d1 = User("George Lucas")

try:
    session.add(m1)
    session.add(d1)
    session.commit()
except:
    session.rollback()


