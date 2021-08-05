import os
import yaml
import logging.config
from flask import Flask, request
from api import BroadlinkApi

app = Flask(__name__)

# Logging configuration
logging.config.dictConfig(yaml.load(open('logging.yml', 'r'), Loader=yaml.SafeLoader))

if os.environ.get('FLASK_ENV', 'unknown') == 'production':
    app.config.from_object('config.ProductionConfig')
else:
    app.config.from_object('config.DevelopmentConfig')

# Set up the bot
api = BroadlinkApi(app)

# Init flask routes
from app import routes

@app.before_request
def before_request():
    """Hooks all requests to:
     0. Only accept POST
    """
    # 0. Only accept POST
    if request.method not in ['POST']:
        return 'Bad request [100]', 400
