from functools import lru_cache

import psycopg

from redshift_ts import config


@lru_cache
def get_con():
    cfg = config.get_config()
    return psycopg.connect(
        host=cfg['database']['host'],
        database=cfg['database']['database'],
        port=cfg['database']['port'],
        user=cfg['database']['user'],
        password=cfg['database']['password']
    )