"""local.py
View development on local server before deployment
"""

from os.path import abspath, dirname

from jinja2 import FileSystemLoader
from flask import Flask, render_template

app = Flask(__name__)
app.jinja_loader = FileSystemLoader(dirname(abspath(__file__)))


@app.route('/')
def home():
    """Returns home"""
    return render_template("index.html")


@app.route("/thanks.html")
def thanks():
    """Thank you page"""
    return render_template("thanks.html")


@app.errorhandler(404)
def page_not_found(e):
    """Handles 404 error"""
    return render_template("404.html"), 404


@app.errorhandler(500)
def server_error(e):
    """Handles 500 error"""
    return render_template("500.html"), 500


if __name__ == "__main__":

    import argparse

    # manually backspace for formatting help menu
    menu_pad = '\b' * 4

    parser = argparse.ArgumentParser(
        description="Script to run website locally",
        add_help=False
    )

    # arguments for details on program
    parser._positionals.title = 'Parameters'
    parser.add_argument(
        '-h', '--help', action='help',
        default=argparse.SUPPRESS,
        help=menu_pad + '| Show this help message and exit'
    )

    # positional arguments
    parser.add_argument('port', help=menu_pad + '| Port of server')

    # parse arguments to pass into function
    args = parser.parse_args()
    app.run(port=int(args.port))
