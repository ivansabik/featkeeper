'''
test_unit_user.py
Tests User behaviour (find, save, validation methods, etc) for both agents and admins
'''

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
import unittest
from featkeeper.models import User
from utils import FeatkeeperTestUtils

class UserUnitTest(unittest.TestCase):
    # Create client, db and collection for tests
    def setUp(self):
        FeatkeeperTestUtils.populate_test_users()

    # Delete test db
    def tearDown(self):
        FeatkeeperTestUtils.destroy_test_db()
    # Test when instanced with default test parameter uses dev db
    def test_use_dev_db(self):
        user = User()
        self.assertEqual('featkeeper', user.collection)

    # Test when instanced with test parameter actually uses test db
    def test_use_test_db(self):
        user = feature_request = User(test=True)
        self.assertEqual('featkeeper-test', user.collection)

    # Test when instanced with test parameter actually uses test db
    def test_use_test_db(self):
        self.fail('test_use_test_db not finished!')

    # Test user authentification for agents (HTTP Digest auth for now) with
    # exiting username and pass
    def test_agent_auth_succesful(self):
        self.fail('test_agent_auth_succesful not finished!')

    # Test user authentification for admins (HTTP Digest auth for now) with
    # exiting username and pass
    def test_admin_auth_succesful(self):
        self.fail('test_admin_auth_succesful not finished!')

    # Test failed user authentification (HTTP Digest auth for now) with wrong
    # username and pass
    def test_auth_failed_wrong_credentials(self):
        self.fail('test_auth_failed_wrong_credentials not finished!')

    # Test failed user authentification (HTTP Digest auth for now) with
    # exiting username and pass that is flagged as access disabled
    def test_auth_failed_user_disabled(self):
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

if __name__ == '__main__':
    unittest.main()
