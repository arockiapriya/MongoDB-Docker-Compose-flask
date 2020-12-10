#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on 

Course work: 

@author: raja

Source:
    https://pythonbasics.org/flask-mongodb/
'''

# Import necessary modules
from . import api
from flask import current_app as app
from flask import Flask, jsonify, request, make_response, session,json

# Local Import
from application import app
from db_configuration import *

'''
    /user
    http://127.0.0.1:8089/user
'''
@api.route('/user', methods=['GET'])
def get_user_by_name():
    name = request.args.get('name')
    user = User.objects(name=name).first()
    if not user:
        return jsonify({'error': 'data not found'})
    else:
        return jsonify(user.to_json())

'''
    /user
    http://127.0.0.1:8089/user/all
'''
@api.route('/user/all', methods=['GET'])
def get_all_users():
    users = User.objects().all()

    user_list = []

    for user in users:
        user_list.append(user.to_json())

    result_dict = {
        "users" : user_list
    }
    
    if not user:
        return jsonify({'error': 'data not found'})
    else:
        return jsonify(result_dict)


'''
    /user
    http://127.0.0.1:8089/user/all/vanilla
'''
@api.route('/user/all/vanilla', methods=['GET'])
def get_all_users_vanilla():
    
    users = table_user.find()
    user_list = []

    for user in users:
        # print('user : ', user)
        user_obj = {
            "name"  : user['name'],
            "email" : user['email']
        }
        user_list.append(user_obj)

    result_dict = {
        "users" : user_list
    }
    
    if not user:
        return jsonify({'error': 'data not found'})
    else:
        return jsonify(result_dict)

'''
    /user
    http://127.0.0.1:8089/user
'''
@api.route('/user', methods=['POST'])
def create_record():
    record = json.loads(request.data)
    user = User(name=record['name'],
                email=record['email'])
    user.save()
    return jsonify(user.to_json())
'''
    /user
    http://127.0.0.1:8089/user
'''
@app.route('/user', methods=['DELETE'])
def delete_record():
    record = json.loads(request.data)
    user = User.objects(name=record['name']).first()
    if not user:
        return jsonify({'error': 'data not found'})
    else:
        user.delete()
    return jsonify(user.to_json())
    