from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app import db

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

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    email = db.Column(db.String(120))
    password = db.Column(db.String(30))

    def __init__(self, name, email, password):
        self.name = name
        self.password = password
        self.email = email

# Create tables.
Base.metadata.drop_all(engine)
Base.metadata.create_all(bind=engine)

'''example = User(name='Ed', email='ed@de.ed', password='1234')
example2 = User(name='Eda', email='eda@de.ed', password='1234')
db_session.add(example)
db_session.add(example2)
our_user = db_session.query(User).filter_by(name='Ed').first()
print(our_user.name) 
our_user2 = db_session.query(User).filter_by(name='Eda').first()
print(our_user2.name) '''
