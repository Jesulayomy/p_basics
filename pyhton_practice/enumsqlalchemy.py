#!/usr/bin/env python3
""" Enumeratiins in sql alchemy """
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Enum
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sys import argv
import enum

Base = declarative_base()

class gender(enum.Enum):
    """ Enum class """
    male = 'm'
    female = 'f'


class User(Base):
    """ Class to map to table """

    __tablename__ = 'my_table'
    id = Column(String(40), primary_key=True)
    name = Column(String(128))
    sex = Column(Enum(gender), default=gender.male)


engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                       .format(argv[1], argv[2], argv[3]), echo=True, pool_pre_ping=True)

session_factory = sessionmaker(bind=engine, expire_on_commit=False)
Session = scoped_session(session_factory)
Base.metadata.create_all(engine)

session = Session()
session.add(User(id='1', name='John', sex='f'))
ssesion.commit()
query = session.query(User)
for row in query:
    print(row)

session.close()
Session.remove()
