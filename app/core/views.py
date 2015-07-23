#!/usr/bin/env python2
# -*- coding: UTF-8 -*- 

from flask import Blueprint, render_template

mod = Blueprint('core', __name__)


@mod.app_errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@mod.route('/')
def index():
    return render_template('index.html')
