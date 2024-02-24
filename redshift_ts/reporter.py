import datetime as dt

from redshift_ts.db.redshift import get_con


def get_data(
        window: int = 60*2  # nb of seconds
    ):
    conn = get_con()

    cursor = conn.cursor()

    print(f"select * from ts_data where ts > '{dt.datetime.now() - dt.timedelta(seconds=window)}'")
    cursor.execute(f"select * from ts_data where ts > '{dt.datetime.now() - dt.timedelta(seconds=window)}'")

    # not sure if it's faster to limit in sql or in pandas
    return cursor.fetch_dataframe()
