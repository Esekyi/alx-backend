#!/usr/bin/env python3
"""Mock logging in."""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _
from typing import Union, Dict


_.__doc__ = "Alias for `gettext`, used to mark strings for translation."


class Config:
    """Config app class with default babel values."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_user(user: int) -> Union[Dict, None]:
    """
    User login function
    params: ID
    returns: a dictionary of users or None
    """
    if user in users:
        return users[user]
    return None


@app.before_request
def before_request(userP=None):
    """Before request function to handle user login."""
    user = get_user(userP)
    if user:
        g.user = user
    else:
        g.user = None


@app.route("/", methods=["GET"], strict_slashes=False)
def index():
    """Index page."""
    if g.user:
        user = g.user.get("name")
    else:
        user = None
    return render_template("5-index.html", user=user,
                           title=_("home_title"),
                           header=_("home_header"),
                           logged_in_as=_("logged_in_as"),
                           not_logged_in=_("not_logged_in"))

if __name__ == '__main__':
    """Main function to run the app"""
    app.run()
