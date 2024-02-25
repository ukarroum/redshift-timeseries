import datetime as dt
import random

import pandas as pd

from redshift_ts.db.redshift import get_con


def get_data_rs(
        window: int = 60*2,  # nb of seconds
        start_time: dt.datetime = None,
        mock=False
):
    if mock:
        if start_time:
            end_time = start_time + dt.timedelta(seconds=window)
        else:
            end_time = dt.datetime.now()

        return pd.DataFrame(data={'ts': [end_time - dt.timedelta(seconds=i) for i in range(window)], 'val': [random.random() for _ in range(window)]})

    conn = get_con()

    cursor = conn.cursor()

    if start_time:
        print(f"select * from ts_data where ts < '{start_time + dt.timedelta(seconds=window)}' and ts > '{start_time}'")
        cursor.execute(f"select * from ts_data where ts < '{start_time + dt.timedelta(seconds=window)}' and ts > '{start_time}'")
    else:
        print(f"select * from ts_data where ts > '{dt.datetime.now() - dt.timedelta(seconds=window)}'")
        cursor.execute(f"select * from ts_data where ts > '{dt.datetime.now() - dt.timedelta(seconds=window)}'")

    return cursor.fetch_dataframe()


def get_data_ts(
    window: int = 60*2  # nb of seconds
):
    conn = get_con()

    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM \"rs_data_test\".\"ts_data\" WHERE time between ago(15m) and now() ORDER BY time DESC LIMIT 10 ")

    # not sure if it's faster to limit in sql or in pandas
    return cursor.fetch_dataframe()
