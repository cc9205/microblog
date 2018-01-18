from flask import Flask

apps = Flask(__name__)

from app import routes
