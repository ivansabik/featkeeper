# test_funcional_api.py
import sys
sys.path.append('/home/ivansabik/Desktop/featkeeper')
from featkeeper import api
import unittest
from flask import json
from featkeeper.schemas import *
from pymongo import MongoClient
from bson.objectid import ObjectId

API_ROOT_URL = '/api/v1'

class FeatkeeperApiTest(unittest.TestCase):

    def setUp(self):
        self.app = api.app.test_client()
        self.client = MongoClient()
        self.db = self.client.featkeeper_test
        self.collection = self.db.feature_requests
        self._populate_test_feature_requests()

    def tearDown(self):
        # drop db
        self.client.drop_database('featkeeper_test')

    def test_api_read_feature_requests(self):
        expected = [
            {
                '_id': '56d3d524402e5f1cfc273340',
                'title': 'Support custom themes',
                'description': 'Client wants to be able to choose different colors, fonts, and layouts for each module',
                'client_name': 'Mandel Jamesdottir',
                'client_priority': 1,
                'target_date': '2016-08-21',
                'ticket_url': 'http://localhost:5000/1',
                'product_area': 'Policies',
                'agent_name': 'Eleuthere',
                'created_at': '2016-02-28 23:35:19',
                'is_open': 1
            },
            {
                '_id': '56d3d524402e5f1cfc273344',
                'title': 'Support Google account auth',
                'description': 'Client wants to be able to login using Google accounts restricted to users in corporate domain',
                'client_name': 'Carlo Fibonacci',
                'client_priority': 2,
                'target_date': '2016-06-15',
                'ticket_url': 'http://localhost:5000/2',
                'product_area': 'Billing',
                'agent_name': 'Eleonor',
                'created_at': '2015-12-20 09:15:20',
                'is_open': 1
            }
        ]

        response = self.app.get(API_ROOT_URL + '/feature-request')
        response_test = json.loads(response.data)
        self.assertEqual(expected, response_test)

    def test_api_read_feature_request(self):
        expected = {
            '_id': 1,
            'title': 'Support custom themes',
            'description': 'Client wants to be able to choose different colors, fonts, and layouts for each module',
            'client_name': 'Mandel Jamesdottir',
            'client_priority': 1,
            'target_date': '2016-08-21',
            'ticket_url': 'http://localhost:5000/1',
            'product_area': 'Policies',
            'agent_name': 'Eleuthere',
            'created_at': '2016-02-28 23:35:19',
            'is_open': 1
        }
        response = self.app.get(API_ROOT_URL + '/feature-request/1')
        response_test = json.loads(response.data)
        self.assertEqual(expected, response_test)

    def test_api_create_feature_requests(self):
        expected = {
            'status': 'success',
            'message': 'Feature request added'
        }
        response = self.app.put(API_ROOT_URL + '/feature-request')
        response_test = json.loads(response.data)
        self.assertEqual(expected, response_test)

    def test_api_update_feature_requests(self):
        expected = {
            'status': 'success',
            'message': 'Feature request updated'
        }
        response = self.app.post(API_ROOT_URL + '/feature-request')
        response_test = json.loads(response.data)
        self.assertEqual(expected, response_test)

    def _populate_test_feature_requests(self):
        # setup test data
        FeatureRequest = create_model(
            feature_request_schema(), self.collection)
        feature_request_1 = FeatureRequest({
            '_id': ObjectId('56d3d524402e5f1cfc273340'),
            'title': 'Support custom themes',
            'description': 'Client wants to be able to choose different colors, fonts, and layouts for each module',
            'client_name': 'Mandel Jamesdottir',
            'client_priority': 1,
            'target_date': '2016-08-21',
            'ticket_url': 'http://localhost:5000/1',
            'product_area': 'Policies',
            'agent_name': 'Eleuthere',
            'created_at': '2016-02-28 23:35:19',
            'is_open': 1
        })
        feature_request_1.save()
        feature_request_2 = FeatureRequest({
            '_id': ObjectId('56d3d524402e5f1cfc273342'),
            'title': 'Support Google account auth',
            'description': 'Client wants to be able to login using Google accounts restricted to users in corporate domain',
            'client_name': 'Carlo Fibonacci',
            'client_priority': 2,
            'target_date': '2016-06-15',
            'ticket_url': 'http://localhost:5000/2',
            'product_area': 'Billing',
            'agent_name': 'Eleonor',
            'created_at': '2015-12-20 09:15:20',
            'is_open': 1
        })
        feature_request_2.save()

if __name__ == '__main__':
    unittest.main()
