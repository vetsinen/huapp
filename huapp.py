# from flask import Flask, jsonify
# from flasgger import Swagger
#
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////hubank.db'
# db = SQLAlchemy(app)
# swagger = Swagger(app)
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation, sessionmaker

engine = create_engine('sqlite:///bank.db')
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    firstname = Column(String(50), nullable=False)

    def __init__(self, name=None):
        self.firsname = name

    def __repr__(self):
        return '<User %r>' % self.firsname


class Account(Base):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True)
    type = Column(Boolean)

    def amount(self):
        return None


class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True)
    amount = Column(Float)

    def __init__(self, amount, from_account=None, to_account=None, currency=None):
        self.amount = amount


class Bank(Base):
    __tablename__ = 'banks'
    id = Column(Integer, primary_key=True)


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

john = User('John')
sean = User('Sean')
# acc = Account()
# t = Transaction(amount=42.0)

try:
    session.add(john)
    session.add(sean)
    session.commit()
except:
    session.rollback()


# @app.route('/')
# def hello_world():
#     # return jsonify(acc is not None)
#     return jsonify(john.id)
#
#
# @app.route('/user')
# def users():
#     return jsonify(t.amount)
#
#
# # if __name__ == '__main__':
# #     app.run(debug=True)
