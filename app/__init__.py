from flask import Flask
from instance.config import app_config
from app.v1.views.parties import api

def create_app(config_name):
    app = Flask(__name__,instance_relative_config=True)
    #register blueprint
    app.register_blueprint(api)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    return app
