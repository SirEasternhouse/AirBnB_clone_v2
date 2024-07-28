#!/usr/bin/python3
"""
Module starts a simple Flask web application
"""


from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Displays simple message "Hello HBNB" on the root route.

    Returns:
        str: The message "Hello HBNB!".
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Displays message "HBNB" on the /hbnb route.

    Returns:
        str: The message "HBNB".
    """
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
