#!/usr/bin/env python3
"""Parametrize templates"""
from flask import Flask, render_template, request
from flask_babel import Babel, _
from typing import Union


class Config:
    """Config app class"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "fr"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> Union[str, None]:
    """Get locale from a request"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/', strict_slashes=False)
def index() -> str:
    """Return an html file"""
    return render_template('3-index.html',
                           title=_("home_title"),
                           header=_("home_header"))


if __name__ == '__main__':
    """Main function"""
    app.run()
