#!/usr/bin/python3
""" script that starts a Flask web application"""

from flask import Flask

appl = Flask(__name__)

#route for URL
@appl.route('/', strict_slashes=False)
def hello_hbnb():
    """ print hello hbnb!"""
    return "Hello HBNB!"


if __name__ == "__main__":
    #listen to all available network
    appl.run(host='0.0.0.0', port=5000)

