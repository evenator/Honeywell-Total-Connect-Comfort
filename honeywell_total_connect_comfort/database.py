from .datatypes import Base

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker()


class Database(object):

    def __init__(self, db_file):
        engine = create_engine('sqlite:///'+db_file, echo=True)
        Base.metadata.create_all(engine)
        Session.configure(bind=engine)

    def add_device_data(self, data):
        session = Session()
        session.add(data)
        session.commit()
