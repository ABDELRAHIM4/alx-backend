#!/usr/bin/env python3
"""Create a single / route and an index.html"""


from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def begin():
    """Create a single / route and an index.html"""
    return render_template("0-index.html")
