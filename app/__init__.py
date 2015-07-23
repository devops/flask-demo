#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

from flask import Flask
from flask.ext.login import LoginManager

from config import config

login_manager = LoginManager()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    from  app.core.views import mod as core_blueprint
    app.register_blueprint(core_blueprint, url_prefix='/')
    
    login_manager.init_app(app)


    return app


