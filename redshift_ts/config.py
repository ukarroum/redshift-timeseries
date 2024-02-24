"""
    Config.py
    =========

    A wrapper around redshift_ts config file

    IMPORTANT: file is expected to be in ~/redshift_ts.toml
"""

from functools import lru_cache
import tomllib
import os


@lru_cache
def get_config() -> dict:
    with open(os.path.expanduser("~/.redshift_ts.toml"), "rb") as f:
        return tomllib.load(f)


@lru_cache
def get_db_credentials() -> dict:
    return get_config()['database']
