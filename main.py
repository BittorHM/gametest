#!/usr/bin/env python

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello Team"

@app.route("/hello")
def index2():
    return "Hello Cloud"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
