#!/usr/bin/python3
"""
This module starts a simple Flask web application.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Displays a simple message "Hello HBNB!" on the root route.

    Returns:
        str: The message "Hello HBNB!".
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Displays the message "HBNB" on the /hbnb route.

    Returns:
        str: The message "HBNB".
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


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    Displays "Python " followd by the value of the text varible.

    The underscore _ symbols in the text variable are replaced with spaces.
    Default value for text is "is cool"

    Args:
        text (str): The text variable from the URL.

    Returns:
        str: The message "Python " followed by the text variable.
    """
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Displays "<n> is a number" only if n is an integer.

    Args:
        n (int): The number from the URL.

    Returns:
        str: The message "<n> is a number".
    """
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Displays an HTML page with "Number: n" inside the body if n is an integer.

    Args:
        n (int): The number from the URL.

    Returns:
        str: Rendered HTML page.
    """
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
