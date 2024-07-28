#!/usr/bin/python3
"""
Module starts simple Flask web application
"""


from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Displays a simple "hello HBNB!" on root route.

    Returns:
        str: The message "Hello HBNB!"
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
