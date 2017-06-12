#!/usr/bin/env python
import datetime

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import Boolean
from sqlalchemy_utils import URLType
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key = True)
    title = Column(String(250), unique=False, nullable=False)
    description = Column(String(120), unique=False, nullable=False)
    date = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)
    expires = Column(DateTime)
    done = Column(Boolean, nullable=False)
    uri = Column(URLType)


if __name__ == "__main__":
    from sqlalchemy import create_engine
    from config import DB_URI
    engine = create_engine(DB_URI)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
