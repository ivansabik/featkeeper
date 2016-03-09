'''
utils.py
Implements functionalities required by many tests like populating test db and taking screenshot in selenium
'''

from pymongo import MongoClient
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
from featkeeper.models import FeatureRequest, User
from bson import json_util, ObjectId

class FeatkeeperTestUtils:
    # Setup test data for feature requests, only 2 records with Id manually assigned so as created date
    @classmethod
    def populate_test_feature_requests(cls):
        client = MongoClient()
        db = client.featkeeper_test
        collection = db.feature_requests
        client.drop_database('featkeeper_test')
        feature_request = FeatureRequest(test=True)
        FeatureRequestModel = feature_request.FeatureRequestModel
        feature_request_1 = FeatureRequestModel({
            '_id': ObjectId('56d3d524402e5f1cfc273340'),
            'title': 'Support custom themes',
            'description': 'Client wants to be able to choose different colors, fonts, and layouts for each module',
            'client_name': 'Mandel Jamesdottir',
            'client_priority': 1,
            'target_date': '2016-08-21',
            'ticket_url': 'http://localhost:5000/8VZuWu',
            'product_area': 'Policies',
            'agent_name': 'Eleuthere',
            'created_at': '2016-02-28 23:35:19',
            'is_open': 1
        })
        feature_request_1.save()
        feature_request_2 = FeatureRequestModel({
            '_id': ObjectId('56d3d524402e5f1cfc273342'),
            'title': 'Support Google account auth',
            'description': 'Client wants to be able to login using Google accounts restricted to users in corporate domain',
            'client_name': 'Carlo Fibonacci',
            'client_priority': 2,
            'target_date': '2016-06-15',
            'ticket_url': 'http://localhost:5000/LhPnCk',
            'product_area': 'Billing',
            'agent_name': 'Eleonor',
            'created_at': '2015-12-20 09:15:20',
            'is_open': 1
        })
        feature_request_2.save()

    # Setup test data for users
    @classmethod
    def populate_test_users(cls):
        client = MongoClient()
        db = client.featkeeper_test
        collection = db.users
        client.drop_database('featkeeper_test')
        user = User(test=True)
        UserModel = user.UserModel
        admin_user = UserModel({
            '_id': ObjectId('56d3d524402e5f1cfc123340'),
            'username': '',
            'hashim': '',
            'type': 'admin',
            'created_at': '2016-03-02 23:35:19',
            'access_is_enabled': 1
        })
        admin_user.save()
        agent_user_1 = UserModel({
            '_id': ObjectId('56d3d524402e5f1cfc124340'),
            'username': '',
            'hashim': '',
            'type': 'agent',
            'created_at': '2016-03-02 23:38:15',
            'access_is_enabled': 1
        })
        agent_user_1.save()
        agent_user_2 = UserModel({
            '_id': ObjectId('56d3d524402e5f1cfc125340'),
            'username': '',
            'hashim': '',
            'type': 'agent',
            'created_at': '2016-02-28 23:40:10',
            'access_is_enabled': 0
        })
        agent_user_2.save()

    # Destroy test db
    @classmethod
    def destroy_test_db(cls):
        client = MongoClient()
        client.drop_database('featkeeper_test')

    # Take screenshot for specs/functional testings
    # Modified from http://www.calebthorne.com/python/2012/May/taking-screenshot-webdriver-python
    @classmethod
    def take_screenshot(self, driver, name, save_location):
        path = os.path.abspath(save_location)
        if not os.path.exists(path):
            os.makedirs(path)
        full_path = path + '/' + name
        driver.save_screenshot(full_path)
        return full_path
