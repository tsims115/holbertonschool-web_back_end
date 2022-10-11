#!/usr/bin/env python3
""" task 0 flask App """
from flask import Flask, render_template, request, g
from flask_babel import Babel, _


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}
app = Flask(__name__)
babel = Babel(app)
_.__doc__ = "setting parmeter values for html"


class Config:
    """Babel configuration"""
    LANGUAGES = ['en', 'fr']


Config.BABEL_DEFAULT_LOCALE = "en"
Config.BABEL_DEFAULT_TIMEZONE = "UTC"
app.config.from_object(Config)
_('home_title')
_('home_header')
_('logged_in_as')
_('not_logged_in')


def get_user():
    """Gets the current user"""
    user = getattr(g, 'user', None)


@babel.localeselector
def get_locale():
    """gets the current locale"""
    loc = request.args.get('locale')
    if loc is not None:
        if loc in Config.LANGUAGES:
            return loc
    return request.accept_languages.best_match(Config.LANGUAGES)

@app.before_request
def before_request():
    """runs before the request"""
    user = get_user()
    if user is not None:
        g.user = user


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """outputs h1 hello world html template"""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
