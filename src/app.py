"""
.. module:: src.app
   :synopsis: Simple flask app that generates a log
"""

from flask import Flask

from src.helper.logging_helper import new_logger as logger

app = Flask(__name__)


@app.route("/")
def hello_world():
    logger.success("Hello, World")
    return "Hello, World!"


@app.route("/error")
def error_world():
    logger.error("Error, World")
    return "Error, World!"


@app.route("/exception")
def exception_world():
    logger.exception("Exception, World")
    return "Exception, World!"


@app.route("/success")
def success_world():
    logger.success("Success, World")
    return "Success, World!"
