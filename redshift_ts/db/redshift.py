from functools import lru_cache

import redshift_connector

from redshift_ts import config


def get_con():
    cfg = config.get_config()
    return redshift_connector.connect(
        host=cfg['database']['host'],
        database=cfg['database']['database'],
        port=cfg['database']['port'],
        user=cfg['database']['user'],
        password=cfg['database']['password']
    )
