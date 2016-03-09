'''
test_functional_new_feature.py
Tests user stories and specs for agent adding a new feature request
@todo: Should validate wrong input fields
'''

from selenium import webdriver
import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
import time
from utils import FeatkeeperTestUtils

class NewFeatureTest(unittest.TestCase):
    # Create client, db and collection for tests
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.set_window_size(800, 800)
        FeatkeeperTestUtils.populate_test_feature_requests()

    # Delete test db
    def tearDown(self):
        FeatkeeperTestUtils.destroy_test_db()
        self.browser.quit()

    def test_can_add_new_feature_request(self):
        # User navigates to home page, he can see a button to add a new feature request
        self.browser.get('http://localhost:5000')
        # User can click on the add new feature button and see a form to add feature request info
        self.browser.find_element_by_id('new-feature-request').click()
        FeatkeeperTestUtils.take_screenshot(self.browser, 'test_can_add_new_feature_request_1.png', '/tmp')
        time.sleep(5)
        self.assertEqual('block',self.browser.find_element_by_id('new').value_of_css_property('display'))

        # User can fill in the required fields associated to the new feature request
        self.browser.find_element_by_id('new-title').send_keys('Do stuff')
        self.browser.find_element_by_id('new-description').send_keys('Client wants to be able to do stuff')
        self.browser.find_element_by_id('new-client-name').send_keys('B')
        self.browser.find_element_by_id('new-client-priority').send_keys('2')
        self.browser.find_element_by_id('new-target-date').send_keys('2016-05-13')
        self.browser.find_element_by_id('new-product-area').send_keys('Billing')
        self.browser.find_element_by_id('new-agent-name').send_keys('Jacob')
        FeatkeeperTestUtils.take_screenshot(self.browser, 'test_can_click_and_display_form_2.png', '/tmp')

        # User can click on the add button and see the newly created feature request
        self.browser.find_element_by_id('save-new-feature-request').send_keys('\n')
        FeatkeeperTestUtils.take_screenshot(self.browser, 'test_can_click_and_display_form_3.png', '/tmp')

        # User can see new feature request's title
        time.sleep(8)
        newFeatureRequestTitle = self.browser.find_element_by_xpath('//*[@id="feature-requests"]/tbody/tr[2]/td[2]/p[1]/b')
        self.assertEqual('Do stuff', newFeatureRequestTitle.text)

        # User can see new feature request's description
        newFeatureRequestDesc = self.browser.find_element_by_xpath('//*[@id="feature-requests"]/tbody/tr[2]/td[2]/p[2]')
        self.assertEqual('Client wants to be able to do stuff', newFeatureRequestDesc.text)

if __name__ == '__main__':
    unittest.main()
