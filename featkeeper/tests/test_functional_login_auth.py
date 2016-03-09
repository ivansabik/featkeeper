'''
test_login_auth.py
Tests user stories and specs for login and authentication
'''

from selenium import webdriver
import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
import time
from utils import FeatkeeperTestUtils

class LoginAuthTest(unittest.TestCase):
    # Create client, db and collection for tests
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.set_window_size(800, 800)
        FeatkeeperTestUtils.populate_test_feature_requests()
        FeatkeeperTestUtils.populate_test_users()

    # Delete test db
    def tearDown(self):
        FeatkeeperTestUtils.destroy_test_db()
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

if __name__ == '__main__':
    unittest.main()
