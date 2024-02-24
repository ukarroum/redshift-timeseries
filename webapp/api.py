import random
from functools import lru_cache

import flask
from flask import Flask

from redshift_ts import reporter

app = Flask(__name__, template_folder='.')

vals = [random.random() for i in range(100)]


@app.route("/api/measures")
def measures():
    df = reporter.get_data()

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
