#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on 

Course work: 

@author: raja

Source:
    https://stackoverflow.com/questions/3659142/bulk-insert-with-sqlalchemy-orm

    http://docs.mongoengine.org/projects/flask-mongoengine/en/latest/

    https://pythonbasics.org/flask-mongodb/
'''

# Import necessary modules

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_cors import CORS
import os

# DB import
from flask_pymongo import PyMongo,pymongo
from flask_mongoengine import MongoEngine

# Local Import
from controllers import *

app = Flask(__name__)

# logging setup

app.register_blueprint(api)

# app configs
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
# app.config["API_KEY"] = os.environ.get('API_KEY')

mongo = PyMongo(app)
bcrypt = Bcrypt()
CORS(app)

app.secret_key = 'dummytesat' 

app.config['MONGODB_SETTINGS'] = {
    'db': 'tact_test',
    'host': app.config["MONGO_URI"]
}

if __name__ == "__main__":
    
    app.config['city'] = 'Toronto'
    
    host = '0.0.0.0'
    port = 8089
    
    app.run(host = host, port = port, use_reloader = True)