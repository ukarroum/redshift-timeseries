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


def insert_measure(measure: float, ts: dt.datetime):
    conn = get_con()

    cursor = conn.cursor()

    print(f"insert into ts_data values('{ts}', {measure})")
    cursor.execute(f"insert into ts_data values('{ts}', {measure})")
    conn.commit()


def loop():
    while True:
        insert_measure(get_measure(), dt.datetime.now())


if __name__ == "__main__":
    loop()
