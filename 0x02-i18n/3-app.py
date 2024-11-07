#!/usr/bin/env python3
"""Parametrize templates part 1"""
from flask import Flask, render_template, request
from flask_babel import Babel, _
from typing import Union


class Config:
    """Config app class with default babel values"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> Union[str, None]:
    """Get locale language from a request"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/', strict_slashes=False)
def index() -> str:
    """Return an html file and parametrize it"""
    return render_template('3-index.html',
                           title=_("home_title"),
                           header=_("home_header"))


if __name__ == '__main__':
    """Main function to run the app"""
    app.run()
