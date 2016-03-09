'''
test_functional_admin_disable_user_access.py
Tests user stories and specs for (user) administrator disabling access for a specific user
'''

from selenium import webdriver
import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
import time
from utils import FeatkeeperTestUtils

class AdminDisableUserTest(unittest.TestCase):
    # Create client, db and collection for tests
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.set_window_size(800, 800)
        FeatkeeperTestUtils.populate_test_users()

    # Delete test db
    def tearDown(self):
        FeatkeeperTestUtils.destroy_test_db()
        self.browser.quit()

    def test_admin_can_flag_agent_user_as_disabled_for_login(self):
        self.fail('test_admin_can_flag_agent_user_as_disabled_for_login not finished!')

if __name__ == '__main__':
    unittest.main()
