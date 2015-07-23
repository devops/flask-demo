#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

from flask import Flask
from flask.ext.pymongo import PyMongo
from flask.ext.login import LoginManager

from config import config


mongo = PyMongo()
login_manager = LoginManager()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    from  app.core.views import mod as core_blueprint
    app.register_blueprint(core_blueprint, url_prefix='/')
    from app.users.views import mod as users_blueprint
    app.register_blueprint(users_blueprint, url_prefix='/users')
    from  app.deploy.views import mod as deploy_blueprint
    app.register_blueprint(deploy_blueprint, url_prefix='/deploy')
    from app.assets.views import mod as assets_blueprint
    app.register_blueprint(assets_blueprint, url_prefix='/assets')

    mongo.init_app(app)
    login_manager.init_app(app)


    return app


