'''
test_unit_user.py
Tests User behaviour (find, save, validation methods, etc) for both agents and admins
'''

import sys
sys.path.append('/home/ivansabik/Desktop/featkeeper')
import unittest
from pymongo import MongoClient
from featkeeper.models import User
from bson import ObjectId

class FeatureRequestUnitTest(unittest.TestCase):
    # Create client, db and collection for tests
    def setUp(self):
        self.client = MongoClient()
        self.db = self.client.featkeeper_test
        self.collection = self.db.feature_requests
        self.client.drop_database('featkeeper_test')
        self._populate_test_feature_requests()

    # Delete test db
    def tearDown(self):
        self.client.drop_database('featkeeper_test')

    # Test when instanced with default test parameter uses dev db
    def test_use_dev_db(self):
        self.fail('test_use_dev_db not finished!')

    # Test when instanced with test parameter actually uses test db
    def test_use_test_db(self):
        self.fail('test_use_test_db not finished!')

    # Test user authentification (HTTP Digest auth for now) with exiting username and pass
    def test_auth_succesful(cls):
        self.fail('test_auth_succesful not finished!')

    # Test failed user authentification (HTTP Digest auth for now) with wrong username and pass
    def test_auth_failed_wrong_credentials(cls):
        self.fail('test_auth_failed_wrong_credentials not finished!')

    # Test failed user authentification (HTTP Digest auth for now) with exiting username and pass that is flagged as access disabled
    def test_auth_failed_wrong_credentials(cls):
        self.fail('test_auth_failed_wrong_credentials not finished!')

    # Test find all agents
    def test_find_all_agents(self):
        self.fail('test_find_all_agents not finished!')

    # Test find user by username
    def test_find_user_by_username(self):
        self.fail('test_find_user_by_username not finished!')

    # Test create agent
    def test_create_user_agent_type(self):
        self.fail('test_create_user_agent_type not finished!')

    # Test update existing agent
    def test_create_user_agent_type(self):
        self.fail('test_create_user_agent_type not finished!')
