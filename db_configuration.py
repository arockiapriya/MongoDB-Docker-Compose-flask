#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on 

Course work: 

@author: raja

Source:
    
'''

# Import necessary modules
from flask_pymongo import PyMongo,pymongo
from flask_mongoengine import MongoEngine

# Local Import
from application import app

mongo  = PyMongo(app)

db = MongoEngine()
db.init_app(app)

# Vaniall Setup
table_user = mongo.db.user

class User(db.Document):

    name = db.StringField()
    email = db.StringField()

    def to_json(self):
        return {"name": self.name,
                "email": self.email}