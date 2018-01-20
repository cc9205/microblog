from flask import Flask
from config import Config
apps = Flask(__name__)
apps.config.from_object(Config)

from app import routes
