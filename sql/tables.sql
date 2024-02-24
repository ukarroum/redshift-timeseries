CREATE DATABASE rs_data_test;

CREATE TABLE ts_data (
    ts timestamp,
    val float
) SORTKEY(ts);