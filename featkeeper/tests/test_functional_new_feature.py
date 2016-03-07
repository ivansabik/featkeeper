'''
test_functional_new_feature.py
Tests user stories and specs for adding a new feature request
@todo: Should validate wrong input fields
'''

from selenium import webdriver
import time
import unittest
import os
import sys
sys.path.append('/home/ivansabik/Desktop/featkeeper')
from featkeeper import app
from pymongo import MongoClient
from featkeeper.models import FeatureRequest
from bson import json_util, ObjectId

class NewFeatureTest(unittest.TestCase):
    # Create client, db and collection for tests
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.client = MongoClient()
        self.db = self.client.featkeeper_test
        self.collection = self.db.feature_requests
        self.client.drop_database('featkeeper_test')
        self._populate_test_feature_requests()

    # Delete test db
    def tearDown(self):
        self.client.drop_database('featkeeper_test')
        self.browser.quit()

    def test_can_add_new_feature_request(self):
        # User navigates to home page, he can see a button to add a new feature request
        self.browser.get('http://localhost:5000')
        # User can click on the add new feature button and see a form to add feature request info
        self.browser.find_element_by_id('new-feature-request').click()
        self._take_screenshot(self.browser, 'test_can_click_and_display_form_1.png', '/tmp')
        self.assertEqual(
            'block',
            self.browser.find_element_by_id('new').value_of_css_property('display')
        )

        # User can fill in the required fields associated to the new feature request
        self.browser.find_element_by_id('new-title').send_keys('Do stuff')
        self.browser.find_element_by_id('new-description').send_keys('Client wants to be able to do stuff')
        self.browser.find_element_by_id('new-client-name').send_keys('B')
        self.browser.find_element_by_id('new-client-priority').send_keys('2')
        self.browser.find_element_by_id('new-target-date').send_keys('2016-05-13')
        self.browser.find_element_by_id('new-product-area').send_keys('Billing')
        self.browser.find_element_by_id('new-agent-name').send_keys('Jacob')
        self._take_screenshot(self.browser, 'test_can_click_and_display_form_2.png', '/tmp')

        # User can click on the add button and see the newly created feature request
        self.browser.find_element_by_id('save-new-feature-request').click()
        time.sleep(15)
        self._take_screenshot(self.browser, 'test_can_click_and_display_form_3.png', '/tmp')
        # User can see new feature request's title
        newFeatureRequestTitle = self.browser.find_element_by_xpath('//*[@id="feature-requests"]/tbody/tr[2]/td[2]/p[1]/b')
        self.assertEqual('Do stuff', newFeatureRequestTitle.text)

        # User can see new feature request's description
        newFeatureRequestDesc = self.browser.find_element_by_xpath('//*[@id="feature-requests"]/tbody/tr[2]/td[2]/p[2]')
        self.assertEqual('Client wants to be able to do stuff', newFeatureRequestDesc.text)

    # Modified from http://www.calebthorne.com/python/2012/May/taking-screenshot-webdriver-python
    def _take_screenshot(self, driver, name, save_location):
        path = os.path.abspath(save_location)
        if not os.path.exists(path):
            os.makedirs(path)
        full_path = path + '/' + name
        driver.save_screenshot(full_path)
        return full_path

    # Setup test data
    def _populate_test_feature_requests(self):
        feature_request = FeatureRequest(test=True)
        FeatureRequestModel = feature_request.FeatureRequestModel
        feature_request_1 = FeatureRequestModel({
            '_id': ObjectId('56d3d524402e5f1cfc273340'),
            'title': 'Support custom themes',
            'description': 'Client wants to be able to choose different colors, fonts, and layouts for each module',
            'client_name': 'Mandel Jamesdottir',
            'client_priority': 1,
            'target_date': '2016-08-21',
            'ticket_url': 'http://localhost:5000/8VZuWu',
            'product_area': 'Policies',
            'agent_name': 'Eleuthere',
            'created_at': '2016-02-28 23:35:19',
            'is_open': 1
        })
        feature_request_1.save()
        feature_request_2 = FeatureRequestModel({
            '_id': ObjectId('56d3d524402e5f1cfc273342'),
            'title': 'Support Google account auth',
            'description': 'Client wants to be able to login using Google accounts restricted to users in corporate domain',
            'client_name': 'Carlo Fibonacci',
            'client_priority': 2,
            'target_date': '2016-06-15',
            'ticket_url': 'http://localhost:5000/LhPnCk',
            'product_area': 'Billing',
            'agent_name': 'Eleonor',
            'created_at': '2015-12-20 09:15:20',
            'is_open': 1
        })
        feature_request_2.save()

if __name__ == '__main__':
    unittest.main()
