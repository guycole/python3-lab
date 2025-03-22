#
# Title: postgres.py
# Description: postgresql support
# Development Environment: Ubuntu 22.04.5 LTS/python 3.10.12
# Author: G.S. Cole (guycole at gmail dot com)
#
# import sqlalchemy
# from sqlalchemy import and_
# from sqlalchemy import select

import datetime
import time

from typing import List, Dict

import pytz

import sqlalchemy
from sqlalchemy import and_
from sqlalchemy import select

from sql_table import Table1, Table2


class PostGres:
    db_engine = None
    Session = None

    def __init__(self, session: sqlalchemy.orm.session.sessionmaker):
        self.Session = session

    def table1_insert(self, args: dict[str, any]) -> Table1:
        candidate = Table1(args)

        try:
            with self.Session() as session:
                session.add(candidate)
                session.commit()
        except Exception as error:
            print(error)

        return candidate

    def table1_select_by_id(self, id:int) -> list[Table1]:
        with self.Session() as session:
            return session.scalars(select(Table1).filter_by(id=id)).first()

    def table1_update(self, args: dict[str, any]) -> Table1:
        with self.Session() as session:
            candidate = session.scalars(select(Table1).filter_by(id=args['row_id'])).first()
            candidate.random_ivalue = args['random_ivalue']
            candidate.random_string = args['random_string']

            session.add(candidate)
            session.commit()

        return candidate

# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***
