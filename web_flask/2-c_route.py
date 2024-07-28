#!/usr/bin/python3
"""
This module starts a simple Flask web application.
"""


from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Displays a simple message "Hello HBNB!" on the root route.

    Returns:
        str: The message "Hello HBNB!"
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Displays the message "HBNB" on the /hbnb route.

    Returns:
        str: The message "HBNB"
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Displays "C " followed by the value of the text variable.

    The underscore _ symbols in the text variable are replaced with spaces.

    Args:
        text (str): The text variable from the URL.

    Returns:
        str: The message "C " followed by the text variable.
    """
    return "C " + text.replace('_', ' ')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
