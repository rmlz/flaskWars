from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
#from app import db

engine = create_engine('sqlite:///db/db.teste', echo=True)
'''
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
                                         '''
db_session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()
#Base.query = db_session.query_property()

# Set your classes here.


class User(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True)
    name = Column(String(120))
    email = Column(String(120))
    password = Column(String(30))

    def __init__(self, name, email, password):
        self.name = name
        self.password = password
        self.email = email

# Create tables.
Base.metadata.drop_all(engine)
Base.metadata.create_all(bind=engine)
