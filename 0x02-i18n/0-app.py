#!/usr/bin/env python3
""" Basic Flask app"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index() -> str:
    """Index page"""
    return render_template('0-index.html')


if __name__ == "__main__":
    """Main function"""
    app.run()
