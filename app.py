from flask import Flask, render_template, send_from_directory
from livereload import Server

import os
import pytest
import sys

app = Flask(__name__)


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, "static"),
        "favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )


@app.route("/")
def home():
    myPlatform = sys.platform
    return render_template("home.html", animal="dog")


if __name__ == "__main__":
    server = Server(app.wsgi_app)
    server.serve()
    # app.run(debug=True)
