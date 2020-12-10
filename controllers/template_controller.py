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
from . import api
from flask import current_app as app
from flask import Flask, jsonify, request, make_response, session,json

# Local Import
from application import app

'''
    /
    http://127.0.0.1:8089/
'''
@api.route('/')
def template_test():
    
    c = 6 + 7

    result_json = {
        'result': c,
        
        'error_code': 0
    }

    return make_response(jsonify(result_json), 200)

'''
    /
    http://127.0.0.1:8089/add
'''
@api.route('/add')
def simple_add():
    
    value_a = int(request.values.get('a'))
    value_b = int(request.values.get('b'))

    value_c = value_a + value_b

    result_json = {
        'value_a' : value_a,
        'value_b' : value_b,
        'result': value_c,
        
        'api_error': 0
    }

    return make_response(jsonify(result_json), 200)