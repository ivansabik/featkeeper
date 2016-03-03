# test_functional_view_features.py
from selenium import webdriver
import unittest
import os
import sys
sys.path.append('/home/ivansabik/Desktop/featkeeper')
from featkeeper import app
from pymongo import MongoClient
from featkeeper.models import FeatureRequest
from bson import json_util, ObjectId

class ViewFeaturesTest(unittest.TestCase):
    # Create client, db and collection for tests
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.client = MongoClient()
        self.db = self.client.featkeeper
        self.collection = self.db.feature_requests
        self.client.drop_database('featkeeper')
        self._populate_test_feature_requests()

    # Delete test db
    def tearDown(self):
        self.client.drop_database('featkeeper')
        self.browser.quit()

    def test_can_view_feature_requests(self):
        # User navigates to home page, he can see a list of feature requests
        self.browser.get('http://localhost:5000')
        feature_requests_list = self.browser.find_element_by_id('feature-requests')
        self.assertEqual(feature_requests_list.get_attribute('class'), 'table table-striped table-responsive')

        # User can see exactly 2 feature requests
        feature_requests_list = self.browser.find_elements_by_xpath('//*[@id="main"]/table/tbody/tr')
        self.assertEqual(
            len(feature_requests_list),
            3
        )

        # User can see the first feature request's title
        title = self.browser.find_element_by_xpath('//*[@id="main"]/table/tbody/tr[2]/td[2]/p[1]/b')
        self.assertEqual(
            title.text,
            'Support custom themes'
        )

        # User can see the first feature request's description
        description = self.browser.find_element_by_xpath('//*[@id="main"]/table/tbody/tr[2]/td[2]/p[2]')
        self.assertEqual(
            description.text,
            'Client wants to be able to choose different colors, fonts, and layouts for each module'
        )

        # User can see the first feature request's client name
        clientName = self.browser.find_element_by_xpath('//*[@id="feature-requests"]/tbody/tr[2]/td[2]/span[2]')
        self.assertEqual(
            clientName.text,
            'Mandel Jamesdottir'
        )

        # User can see the first feature request's client priority
        clientPriority = self.browser.find_element_by_xpath('//*[@id="main"]/table/tbody/tr[2]/td[2]/span[4]')
        self.assertEqual(
            clientPriority.text,
            '1'
        )

        # User can see the first feature request's target date
        targetDate = self.browser.find_element_by_xpath('//*[@id="main"]/table/tbody/tr[2]/td[2]/span[6]')
        self.assertEqual(
            targetDate.text,
            '2016-08-21'
        )

        # User can see the first feature request's ticket URL
        ticketUrl = self.browser.find_element_by_xpath('//*[@id="main"]/table/tbody/tr[2]/td[2]/a')
        self.assertEqual(
            ticketUrl.text,
            'http://localhost:5000/8VZuWu'
        )

        # User can see the first feature request's product area
        productArea = self.browser.find_element_by_xpath('//*[@id="feature-requests"]/tbody/tr[2]/td[2]/span[9]')
        self.assertEqual(
            productArea.text,
            'Policies'
        )

        # User can see the first feature request's agent name
        agentName = self.browser.find_element_by_xpath('//*[@id="main"]/table/tbody/tr[2]/td[2]/span[11]')
        self.assertEqual(
            agentName.text,
            'Eleuthere'
        )

        # User can see the first feature request's status (open, closed)
        isOpen = self.browser.find_element_by_xpath('//*[@id="main"]/table/tbody/tr[2]/td[1]/span[2]')
        self.assertEqual(
            isOpen.text,
            'In Progress'
        )
        self._take_screenshot(self.browser, 'test_can_view_feature_requests.png', '/tmp')

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
        feature_request = FeatureRequest()
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
