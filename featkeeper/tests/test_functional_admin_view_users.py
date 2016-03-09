'''
test_functional_admin_view_users.py
Tests user stories and specs for (user) administrator viewing current users
'''

from selenium import webdriver
import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
import time
from utils import FeatkeeperTestUtils

class AdminViewUsersTest(unittest.TestCase):
    # Create client, db and collection for tests
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.set_window_size(800, 800)
        FeatkeeperTestUtils.populate_test_users()

    # Delete test db
    def tearDown(self):
        FeatkeeperTestUtils.destroy_test_db()
        self.browser.quit()

    def test_admin_can_add_user_agent(self):
        self.fail('test_user_admin_can_add_user_agent not finished!')

if __name__ == '__main__':
    unittest.main()
