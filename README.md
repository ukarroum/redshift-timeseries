# Redshift Timeseries
---------------------

A small poc to study timeseries usage with redshift.

## Usage
--------

### Installation

pipenv sync

### Running flask webserver

PYTHONPATH=<path to repo>:$PYTHONPATH pipenv run gunicorn api:app -b "0.0.0.0:80"