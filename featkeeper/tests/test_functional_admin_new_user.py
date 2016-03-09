'''
test_functional_admin_new_user.py
Tests user stories and specs for (user) administrator creating a new user
'''

from selenium import webdriver
import unittest
import os
import sys
sys.path.append('/home/ivansabik/Desktop/featkeeper')
from featkeeper import app
from pymongo import MongoClient
from featkeeper.models import FeatureRequest
from bson import json_util, ObjectId
import time

class AdminNewUserTest(unittest.TestCase):
    # Create client, db and collection for tests
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.set_window_size(800, 800)
        self.client = MongoClient()
        self.db = self.client.featkeeper_test
        self.collection = self.db.users
        self.client.drop_database('featkeeper_test')
        self._populate_test_users()

    # Delete test db
    def tearDown(self):
        self.client.drop_database('featkeeper_test')
        self.browser.quit()

    def test_admin_can_add_agent_user(self):
        self.fail('test_admin_can_add_agent_user not finished!')

    # Setup test data
    def _populate_test_users(self):
        pass

if __name__ == '__main__':
    unittest.main()
