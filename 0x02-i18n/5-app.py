#!/usr/bin/env python3
"""Mock logging in."""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _
from typing import Union, Dict, Optional


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


@babel.localeselector
def get_locale() -> Union[str, None]:
    """
    Determine the best match language for the current request.

    First checks if a 'locale' parameter is provided in the URL and matches
    a supported language. If so, uses it
    otherwise, defaults to the client's
    preferred language based on 'Accept-Language' headers.
    """
    locale = request.args.get('locale')
    if locale in app.config["LANGUAGES"]:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


def get_user() -> Optional[Dict]:
    """
    User login function
    params: ID
    returns: a dictionary of users or None
    """
    try:
        user_id = int(request.args.get('login_as'))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None


@app.before_request
def before_request():
    """Before request function to handle user login."""
    g.user = get_user()


@app.route("/", methods=["GET"], strict_slashes=False)
def index() -> str:
    """
    Render the main index page with a message depending on the login state.

    Returns:
        str: Rendered HTML template.
    """
    if g.user:
        welcome_msg = _("logged_in_as", username=g.user.get("name"))
    else:
        welcome_msg = _("not_logged_in")
    return render_template("5-index.html", welcome_msg=welcome_msg,
                           title=_("home_title"),
                           header=_("home_header"))


if __name__ == '__main__':
    """Main function to run the app"""
    app.run()
