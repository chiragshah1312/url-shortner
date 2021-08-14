"""Single place to write all ORM related queries"""

import datetime
from models import *


from dal.ddl import CREATE_TABLES


class DAL:
    def __init__(self, session, log):
        self.session = session
        self.log = log
        self.create_tables()

    def create_tables(self):
        try:
            for query in CREATE_TABLES:
                self.session.bind.engine.execute(query)
            self.commit()
        except Exception as ex:

            print('Failed to create tables')
            print(ex)

    def set_one_row(self, row):
        self.session.add(row)
        self.session.flush()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()

    def close_session(self):
        self.session.close()
        self.session.bind.engine.dispose()

    def insert_url(self, uuid, url):
        try:
            obj_url = Urls()
            obj_url.link = url
            obj_url.uid = uuid
            obj_url.created_timestamp = datetime.datetime.utcnow()
            self.set_one_row(obj_url)
            self.commit()
            return True
        except Exception as ex:
            self.rollback()
            return False

    def get_url(self, url):
        try:
            return self.session.query(Urls).filter(Urls.link == url).all(), True
        except Exception as ex:
            self.rollback()
            return None, False
