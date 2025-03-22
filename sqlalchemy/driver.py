#
# Title: driver.py
# Description:
# Development Environment: Ubuntu 22.04.5 LTS/python 3.10.12
# Author: G.S. Cole (guycole at gmail dot com)
#
import datetime
import os
import pytz
import random
import sys

import yaml
from yaml.loader import SafeLoader

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sql_table import Table1, Table2
import postgres


class DemoDriver:

    mock_rows = {}

    def __init__(self, configuration: dict[str, str]):
        self.db_conn = configuration["dbConn"]
        self.sql_echo = configuration["sqlEchoEnable"]

        connect_dict = {"options": "-csearch_path={}".format("public")}
        db_engine = create_engine(
            self.db_conn, echo=self.sql_echo, connect_args=connect_dict
        )

        self.postgres = postgres.PostGres(
            sessionmaker(bind=db_engine, expire_on_commit=False)
        )

    def mock_row(self) -> dict[str, any]:
        return {
            'row_id': 0,
            'date_stamp': datetime.datetime.now().date(),
            'random_ivalue': random.randint(1, 999),
            'random_string': 'rs' + str(random.randint(1, 999)),
            'time_stamp1': datetime.datetime.now(),
            'time_stamp2': datetime.datetime.now(pytz.utc)
        }

    def mock_row_compare(self, ndx: int, selected: Table1) -> bool:
        candidate = self.mock_rows[ndx]
#        print(candidate)

        if candidate['row_id'] != selected.id:
            print("bad row id")
            return False

        if candidate['date_stamp'] != selected.date_stamp:
            print("bad date stamp")
            return False

        if candidate['random_ivalue'] != selected.random_ivalue:
            print(type(candidate['random_ivalue']))
            print(type(selected.random_ivalue))
            print(f"bad ivalue expected {candidate['random_ivalue']} got {selected.random_ivalue}")
            return False

        if candidate['random_string'] != selected.random_string:
            print("bad random string")
            return False

        if candidate['time_stamp1'] != selected.time_stamp1:
            print("bad time stamp1")
            print(selected.time_stamp1)
            return False

        if candidate['time_stamp2'] != selected.time_stamp2:
            print("bad time stamp2")
            return False

    def generate_mock_rows(self, limit: int):
        for ndx in range(limit):
            self.mock_rows[ndx] = self.mock_row()

    def update_mock_rows(self):
        for key, value in self.mock_rows.items():
            value['random_ivalue'] = random.randint(1, 999)
            value['random_string'] = 'rs' + str(random.randint(1, 999))

    def execute(self) -> None:
        limit = 5

        # create test datum
        self.generate_mock_rows(limit)

        # postgres insert
        for key, value in self.mock_rows.items():
            temp = self.postgres.table1_insert(value)
            value['row_id'] = temp.id

        # postgres select and compare
        for key, value in self.mock_rows.items():
            candidate = self.postgres.table1_select_by_id(value['row_id'])
            self.mock_row_compare(key, candidate)

        # test datum update
        self.update_mock_rows()

        # postgres update
        for key, value in self.mock_rows.items():
            temp = self.postgres.table1_update(value)
        
        # postgres select and compare
        for key, value in self.mock_rows.items():
            candidate = self.postgres.table1_select_by_id(value['row_id'])
            self.mock_row_compare(key, candidate)


print("start driver")

#
# argv[1] = configuration filename
#
if __name__ == "__main__":
    if len(sys.argv) > 1:
        config_name = sys.argv[1]
    else:
        config_name = "config.yaml"

    with open(config_name, "r", encoding="utf-8") as in_file:
        try:
            configuration = yaml.load(in_file, Loader=SafeLoader)
        except yaml.YAMLError as error:
            print(error)

    driver = DemoDriver(configuration)
    driver.execute()

print("stop driver")

# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***
