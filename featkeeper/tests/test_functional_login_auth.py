'''
test_login_auth.py
Tests user stories and specs for login and authentication
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

class LoginAuthTest(unittest.TestCase):
    # Create client, db and collection for tests
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.set_window_size(800, 800)
        self.client = MongoClient()
        self.db = self.client.featkeeper_test
        self.collection = self.db.feature_requests
        self.client.drop_database('featkeeper_test')
        self._populate_test_feature_requests()

    # Delete test db
    def tearDown(self):
        self.client.drop_database('featkeeper_test')
        self.browser.quit()

    def test_agent_can_login(self):
        self.fail('test_agent_can_login not finished!')

    def test_agent_cannot_login_with_wrong_credentials(self):
        self.fail('test_agent_cannot_login_with_wrong_credentials not finished!')

    def test_admin_can_login(self):
        self.fail('test_admin_can_login not finished!')

    def test_admin_cannot_login_with_wrong_credentials(self):
        self.fail('test_admin_cannot_login_with_wrong_credentials not finished!')

    def test_anonymous_user_cannot_access_admin_view(self):
        self.fail('test_anonymous_user_cannot_access_admin_view not finished!')

    def test_anonymous_user_cannot_access_agent_view(self):
        self.fail('test_anonymous_user_cannot_access_agent_view not finished!')

    def test_agent_cannot_access_admin_view(self):
        self.fail('test_agent_cannot_access_admin_view not finished!')

    # Setup test data
    def _populate_test_feature_requests(self):
        pass
