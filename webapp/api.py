import random
from functools import lru_cache
import datetime as dt

import flask
from flask import Flask

from redshift_ts import reporter

app = Flask(__name__, template_folder='.')


@app.route("/api/measures", methods=["POST"])
def measures():
    start_time = flask.request.form.get("starttime")
    if not start_time:
        start_time = None
    else:
        start_time = dt.datetime.fromisoformat(start_time)

    df = reporter.get_data_rs(start_time=start_time, window=int(flask.request.form.get("window")))

    return {"labels": df.ts.to_list(), "data": df.val.to_list()}


@app.route("/")
def index():
    return flask.render_template("index.html")


@app.route('/js/<path:path>')
def js(path):
    return flask.send_from_directory('js', path)


@app.route('/css/<path:path>')
def css(path):
    return flask.send_from_directory('css', path)
