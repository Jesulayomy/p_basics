#!/usr/bin/env python3
from flask import Flask, session
from flask import redirect, url_for, request
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask import jsonify, make_response

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Enum
from sqlalchemy import create_engine
from  uuid import uuid4
from sqlalchemy.orm import sessionmaker, scoped_session
# from sys import argv
import enum
from hashlib import md5

from datetime import datetime, timedelta

""" This module contains the class for storage """

from contextlib import contextmanager
# from dotenv.main import load_dotenv
# from os import getenv, environ
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.pool import QueuePool


# load_dotenv()

Base = declarative_base()

class Gender(enum.Enum):
    """ Enum class """
    male = 'male'
    female = 'female'


class User(Base, UserMixin):
    """ Class to map to table """

    __tablename__ = 'my_table'
    id = Column(String(40), primary_key=True, unique=True)
    name = Column(String(128))
    gender = Column(Enum(Gender), default='male')
    password = Column(String(128))

    def get_id(self):
        """ returns the id of the object """
        return self.id

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


class Storage:
    """ database storage class """

    __engine = None

    def __init__(self):
        """ initializes self """

        uname = "schub_dev"
        passwd = "schub_dev_pwd"
        dbname = "mydb"
        self.__engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                       .format(uname, passwd, dbname),
                       echo=True, pool_pre_ping=True,
                       poolclass=QueuePool, pool_size=10)
        self.session_factory = sessionmaker(bind=self.__engine,
                                            expire_on_commit=False)
        self.Session = scoped_session(self.session_factory)

        # if is_test:
        #     Base.metadata.drop_all(self.__engine)

    def reload(self):
        """ Reloads the session and create tables """

        Base.metadata.create_all(self.__engine)

    @contextmanager
    def session_scope(self):
        """
            Creates a session, and tearsDown after control
            is transferred back
        """

        session = self.Session()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise Exception
        finally:
            session.close()

    def all(self, cls=None):
        """ gets all objects """

        objects = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            with self.session_scope() as session:
                query = session.query(cls)
                for obj in query:
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    objects[key] = obj
        else:
            for model in [User]:
                with self.session_scope() as session:
                    query = session.query(model)
                    for obj in query:
                        key = "{}.{}".format(obj.__class__.__name__, obj.id)
                        objects[key] = obj

        return objects

    def get(self, cls, id):
        """ gets a particular object """

        if type(cls) is str:
            cls = eval(cls)

        with self.session_scope() as session:
            try:
                obj = session.query(cls).filter(cls.id == id).one()
            except Exception:
                obj = None

        return obj

    def count(self, cls=None):
        """ Returns the number of objects of a class """

        return len(self.all(cls))

    def new(self, obj):
        """ Adds an object to the current session """

        with self.session_scope() as session:
            session.add(obj)

    def save(self):
        """ commits the current session """

        with self.session_scope() as session:
            session.commit()

    def delete(self, obj):
        """ deletes an object from the current session """

        with self.session_scope() as session:
            session.delete(obj)

    def close(self):
        """ removes the current session """

        self.Session.remove()

storage = Storage()
storage.reload()

app = Flask(__name__)
app.secret_key = b'256438e0bbcb880cf8eb2e61ed4955728aa018cccfdf3d398d87b2439c7d9a58'
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    """ loads user """
    return storage.get(User, user_id)

@app.teardown_appcontext
def teardown_db(exception):
    """ closes the storage """
    storage.close()

@app.errorhandler(404)
def page_not_found(e):
    return '<h1>404</h1><p>Page Not Found</p>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=text name=gender>
            <p><input type=password name=password>
            <p><input type=submit value=Login>
        </form>
    '''
    if request.method == 'POST':
        name = request.form['username']
        passwd = request.form['password']

        users = storage.all(User)
        user = None
        for obj in users.values():
            if obj.name == name:
                md5_hash = md5()
                md5_hash.update(passwd.encode("utf-8"))
                password_hash = md5_hash.hexdigest()
                if obj.password == password_hash:
                    user = obj
                    break
                else:
                    return form, '<p>Incorrect Password</p>'
        if user is None:
            storage.new(User(
                name=request.form['username'],
                password=request.form['password'],
                gender=request.form['gender']))
            users = storage.all(User)
            user = [obj for obj in users.values() if obj.name == name][0]

        login_user(user, remember=True, duration=timedelta(days=30))
        return redirect(url_for('index'))
    return form

@app.route('/')
@login_required
def index():
    return '<h1>Hello World</h1><p> Lets Play</p>'

@app.route('/maths', methods=['GET'])
def maths():
    return f'Two plus two is four'

@app.route('/books', methods=['GET'])
@login_required
def books():
    return '<p>Books are great {}</p>'.format(current_user.name)

@app.route('/users', methods=['GET'], strict_slashes=False)
@login_required
def users():
    all_users = storage.all(User)
    return make_response(jsonify(
        [user.to_dict() for user in all_users.values()]
    ))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
