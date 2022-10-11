#!/usr/bin/env python3
""" task 0 flask App """
from flask import Flask, render_template, request
from flask_babel import Babel, _


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


@babel.localeselector
def get_locale():
    """gets the current locale"""
    loc = request.args.get('locale')
    if loc is not None:
        if loc in Config.LANGUAGES:
            return loc
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """outputs h1 hello world html template"""
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
