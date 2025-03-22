#
# Title: sql_table.py
# Description: database table definitions
# Development Environment: Ubuntu 22.04.5 LTS/python 3.10.12
# Author: G.S. Cole (guycole at gmail dot com)
#
# import sqlalchemy
# from sqlalchemy import and_
# from sqlalchemy import select

from datetime import datetime, timezone

from sqlalchemy import Column
from sqlalchemy import BigInteger, Boolean, Date, DateTime, Float, Integer, String

from sqlalchemy.orm import registry
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.declarative import declared_attr

mapper_registry = registry()


class Base(DeclarativeBase):
    pass

class Table1(Base):
    __tablename__ = "table1"

    id = Column(Integer, primary_key=True)
    date_stamp = Column(Date)
    random_ivalue = Column(Integer)
    random_string = Column(String)
    time_stamp1 = Column(DateTime)
    time_stamp2 = Column(DateTime)

    def __init__(self, args: dict[str, any]):
        self.date_stamp = args['date_stamp']
        self.random_ivalue = args['random_ivalue']
        self.random_string = args['random_string']
        self.time_stamp1 = args['time_stamp1']
        self.time_stamp2 = args['time_stamp2']
        
class Table2(Base):
    __tablename__ = "table2"

    id = Column(Integer, primary_key=True)
    random_ivalue = Column(Integer)
    random_string = Column(String)
    table1_id = Column(BigInteger)

    def __init__(self, args: dict[str, any]):
        self.date_stamp = args['date_stamp']
        self.random_ivalue = args['random_ivalue']
        self.random_string = args['random_string']
        self.time_stamp1 = args['time_stamp1']
        self.time_stamp2 = args['time_stamp2']
        self.table1_id = args['table1_id']

# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***
