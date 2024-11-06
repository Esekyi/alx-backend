#!/usr/bin/env python3
"""Basic Babel setup"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Config app class"""

    LANGUAGES = ["en", "fr"]


# def get_locales():
#     """Get languages from Config class"""
#     return request.accept_languages.best_match(app.config['LANGUAGES'])


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app, default_locale='en', default_timezone='UTC',)


@app.route('/', strict_slashes=False)
def index() -> str:
    """Return an html file"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
