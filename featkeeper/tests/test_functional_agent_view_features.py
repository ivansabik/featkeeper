'''
test_functional_view_features.py
Tests user stories and specs for agent viewing existing feature requests
@todo: Should warn when no feature requests exist
@todo: Should fail if user has not authenticated
@todo: Should only display authenticated user's feature requests
'''

from selenium import webdriver
import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
from utils import FeatkeeperTestUtils

class ViewFeaturesTest(unittest.TestCase):
    # Create client, db and collection for tests
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.set_window_size(800, 800)
        FeatkeeperTestUtils.populate_test_feature_requests()

    # Delete test db
    def tearDown(self):
        FeatkeeperTestUtils.destroy_test_db()
        self.browser.quit()

    def test_can_view_feature_requests(self):
        # User navigates to home page, he can see a list of feature requests
        self.browser.get('http://localhost:5000')
        feature_requests_list = self.browser.find_element_by_id('feature-requests')
        self.assertEqual(feature_requests_list.get_attribute('class'), 'table table-striped table-responsive')

        # User can see exactly 2 feature requests
        feature_requests_list = self.browser.find_elements_by_xpath('//*[@id="main"]/table/tbody/tr')
        self.assertEqual(3, len(feature_requests_list))

        # User can see the first feature request's title
        title = self.browser.find_element_by_xpath('//*[@id="main"]/table/tbody/tr[2]/td[2]/p[1]/b')
        self.assertEqual('Support custom themes',title.text)

        # User can see the first feature request's description
        description = self.browser.find_element_by_xpath('//*[@id="main"]/table/tbody/tr[2]/td[2]/p[2]')
        self.assertEqual('Client wants to be able to choose different colors, fonts, and layouts for each module',description.text)

        # User can see the first feature request's client name
        clientName = self.browser.find_element_by_xpath('//*[@id="feature-requests"]/tbody/tr[2]/td[2]/span[2]')
        self.assertEqual('Mandel Jamesdottir', clientName.text)

        # User can see the first feature request's client priority
        clientPriority = self.browser.find_element_by_xpath('//*[@id="main"]/table/tbody/tr[2]/td[2]/span[4]')
        self.assertEqual('1',clientPriority.text)

        # User can see the first feature request's target date
        targetDate = self.browser.find_element_by_xpath('//*[@id="main"]/table/tbody/tr[2]/td[2]/span[6]')
        self.assertEqual('2016-08-21',targetDate.text)

        # User can see the first feature request's ticket URL
        ticketUrl = self.browser.find_element_by_xpath('//*[@id="main"]/table/tbody/tr[2]/td[2]/a')
        self.assertEqual('http://localhost:5000/8VZuWu', ticketUrl.text)

        # User can see the first feature request's product area
        productArea = self.browser.find_element_by_xpath('//*[@id="feature-requests"]/tbody/tr[2]/td[2]/span[9]')
        self.assertEqual('Policies', productArea.text)

        # User can see the first agent name associated with the feature request
        agentName = self.browser.find_element_by_xpath('//*[@id="main"]/table/tbody/tr[2]/td[2]/span[11]')
        self.assertEqual('Eleuthere',agentName.text)

        # User can see the first feature request's status (open, closed)
        isOpen = self.browser.find_element_by_xpath('//*[@id="main"]/table/tbody/tr[2]/td[1]/span[2]')
        self.assertEqual('In Progress',isOpen.text)
        FeatkeeperTestUtils.take_screenshot(self.browser, 'test_can_view_feature_requests.png', '/tmp')

if __name__ == '__main__':
    unittest.main()
