""" This are the sqlalchemy ORM classes"""
import enum
from sqlalchemy import Column, Integer, Unicode, TIMESTAMP, TEXT
from sqlalchemy.orm import relationship
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base( metadata=MetaData(schema=''))


class Urls(Base):
    __tablename__ = 'urls'
    url_id = Column(Integer, primary_key=True)
    uid = Column(Unicode)
    link = Column(TEXT)
    created_timestamp = Column(TIMESTAMP)
    updated_timestamp = Column(TIMESTAMP)
