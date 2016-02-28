# test_funcional_api.py
import sys
sys.path.append('/home/ivansabik/Desktop/featkeeper')
from featkeeper import api
import unittest
from flask import json

API_ROOT_URL = '/api/v1'

class FeatkeeperApiTest(unittest.TestCase):
    def setUp(self):
        self.app = api.app.test_client()
        _populate_test_feature_requests()

    def tearDown(self):
        # drop db
        pass

    def test_api_read_feature_requests(self):
        expected = {}
        response = self.app.get(API_ROOT_URL + '/feature-request')
        response_test = json.loads(response.data)
        self.assertEqual(expected, response_test)

    def test_api_read_feature_request(self):
        expected = {}
        response = self.app.get(API_ROOT_URL + '/feature-request/1')
        response_test = json.loads(response.data)
        self.assertEqual(expected, response_test)

    def test_api_create_feature_requests(self):
        expected = {}
        response = self.app.put(API_ROOT_URL + '/feature-request')
        response_test = json.loads(response.data)
        self.assertEqual(expected, response_test)

    def test_api_update_feature_requests(self):
        expected = {}
        response = self.app.post(API_ROOT_URL + '/feature-request')
        response_test = json.loads(response.data)
        self.assertEqual(expected, response_test)

    def _populate_test_feature_requests(self):
        # setup test data
        pass

if __name__ == '__main__':
    unittest.main()
