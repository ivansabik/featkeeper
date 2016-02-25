# test_funcional_api.py
import sys
sys.path.append('/home/enivanrodrig/Desktop/featkeeper') # Change
from featkeeper import api
import unittest
from pymongo import MongoClient
from flask import json
from featkeeper.tests.data_setup import *

class CatalogoReadTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = api.app.test_client()
        cls.client = MongoClient()
        populate_test_feature_requests(cls.client)
        populate_test_agents(cls.client)
        populate_test_clients(cls.client)

    @classmethod
    def tearDownClass(cls):
        cls.client.drop_database('featkeeper_tests')

    def test_api_read_feature_requests(self):
        expected = {}
        response = self.app.get('/api/v1/feature-request')
        response_test = json.loads(response.data)
        # self.assertEqual(expected, response_test)
        self.fail('test_api_read_feature_requests Not finished')

    def test_api_create_feature_requests(self):
        expected = {}
        response = self.app.put('/api/v1/feature-request')
        response_test = json.loads(response.data)
        # self.assertEqual(expected, response_test)
        self.fail('test_api_create_feature_requests Not finished')

    def test_api_update_feature_requests(self):
        expected = {}
        response = self.app.post('/api/v1/feature-request')
        response_test = json.loads(response.data)
        # self.assertEqual(expected, response_test)
        self.fail('test_api_update_feature_requests Not finished')

    def test_api_read_agent(self):
        expected = {}
        response = self.app.get('/api/v1/agent')
        response_test = json.loads(response.data)
        # self.assertEqual(expected, response_test)
        self.fail('test_api_read_agent Not finished')

    def test_api_read_client(self):
        expected = {}
        response = self.app.get('/api/v1/client')
        response_test = json.loads(response.data)
        # self.assertEqual(expected, response_test)
        self.fail('test_api_read_client Not finished')

    if __name__ == '__main__':
        unittest.main()
