#!/usr/bin/env python3
"""Create a single / route and an index.html"""


from flask import Flask, render_template
from flask_babel import Babel
app = Flask(__name__)
babel = Babel(app)
class Config():
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"
app.config.from_object(Config)

@app.route("/")
def begin():
    """Create a single / route and an index.html"""
    return render_template("0-index.html")
