from flask import Flask
from config import Config
import os, re

if Config.RUN_MODE == "dev":
    print(">>>", os.path.basename(__file__))

application = Flask(__name__)
application.config.from_object(Config)

from portfolio import routes

if __name__ == "__main__":
    application.run()
