#!/usr/bin/env python3
""" task 0 flask App """
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """Babel configuration"""
    LANGUAGES = ['en', 'fr']


Config.BABEL_DEFAULT_LOCALE = "en"
Config.BABEL_DEFAULT_TIMEZONE = "UTC"
app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """gets the current locale"""
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """outputs h1 hello world html template"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
