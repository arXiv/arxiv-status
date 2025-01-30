"""Application for status.arxiv.org page"""

import logging
from flask.logging import default_handler
from flask import Flask, render_template
from arxiv.base import Base

APP_VERSION="0.1.0"

def create_web_app(**kwargs) -> Flask:
    """Initialize an instance of the status web application."""
    root = logging.getLogger()
    root.addHandler(default_handler)
    app = Flask('status', static_url_path=f'/static/status/{APP_VERSION}')
    Base(app)

    @app.route("/")
    def status():
        return render_template("status.html")

    if not app.jinja_env.globals:
        app.jinja_env.globals = {}

    return app
