#!/usr/bin/env python3
""" Enumerations in sql alchemy """
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Enum
from sqlalchemy import create_engine
from  uuid import uuid4
from sqlalchemy.orm import sessionmaker, scoped_session
# from sys import argv
import enum
from hashlib import md5

Base = declarative_base()

class Gender(enum.Enum):
    """ Enum class """
    male = 'male'
    female = 'female'


class User(Base):
    """ Class to map to table """

    __tablename__ = 'my_table'
    id = Column(String(40), primary_key=True, unique=True)
    name = Column(String(128))
    gender = Column(Enum(Gender), default='male')
    password = Column(String(128))

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != 'id':
                    setattr(self, key, value)
            self.id = str(uuid4())

    def __str__(self):
        return "User({}): {} {}".format(
            self.id,
            self.name,
            self.gender)

    def __setattr__(self, name, value):
        if name == 'password':
            hashed = md5()
            hashed.update(value.encode('utf-8'))
            value = hashed.hexdigest()
        super().__setattr__(name, value)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'gender': self.gender.name,
        }


# uname = "schub_dev"
# passwd = "schub_dev_pwd"
# dbname = "mydb"
# engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
#                        .format(uname, passwd, dbname), echo=True, pool_pre_ping=True)
""" this engine contains the connection pool
    using username, password and database name respectively
"""

# session_factory = sessionmaker(bind=engine, expire_on_commit=False)
# Session = scoped_session(session_factory)
# Base.metadata.drop_all(engine)
# Base.metadata.create_all(engine)

# session = Session()

# session.add(User(id='1', name='Toby', gender='male', password='123456'))
# session.add(User(id='2', name='John', gender='male', password='1234567'))
# session.add(User(id='3', name='Feline', gender='female', password='12345678'))
# session.commit()

# query = session.query(User)
# for row in query:
#     print(row)
#     print(row.to_dict())

# session.close()
# Session.remove()
