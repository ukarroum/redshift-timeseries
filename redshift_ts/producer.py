"""
    Producer.py
    -----------

    A simple python script to mock and store the timeseries data
"""

import random
import datetime as dt

from redshift_ts.db.redshift import get_con


def get_measure():
    return random.random()


def insert_measures(measures: list[float]|float, ts: list[dt.datetime]|dt.datetime):
    if isinstance(measures, float):
        measures = [measures]
    if isinstance(ts, dt.datetime):
        ts = [ts]

    conn = get_con()
    conn.autocommit = True

    cursor = conn.cursor()

    query = "insert into ts_data values " + ", ".join([f"('{t}', {m})" for t, m in zip(ts, measures)])
    print(query)
    cursor.execute(query)


def loop():
    while True:
        insert_measures(get_measure(), dt.datetime.now())


if __name__ == "__main__":
    loop()
