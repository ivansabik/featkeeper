# test_functional_view_features.py
from selenium import webdriver
import unittest
import os

class ViewFeaturesTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_view_feature_requests(self):
        # User navigates to home page, he can see a list of feature requests
        self.browser.get('http://localhost:5000')
        feature_requests_list = self.browser.find_element_by_id('feature-requests')
        self.assertEqual(feature_requests_list.get_attribute('class'), 'table table-striped table-responsive')

        # User can see exactly 2 feature requests
        feature_requests_list = self.browser.find_element_by_xpath('//*[@id="main"]/table/tbody/tr')
        self.assertEqual(
            len(feature_requests_list),
            3
        )

        # User can see the fist feature request's title
        title = self.browser.find_element_by_xpath('//*[@id="main"]/table/tbody/tr[2]/td[2]/p[1]/b')
        self.assertEqual(
            title.text,
            'Support custom themes'
        )
        # User can see the fist feature request's description
        description = self.browser.find_element_by_xpath('//*[@id="main"]/table/tbody/tr[2]/td[2]/p[2]')
        self.assertEqual(
            description.text,
            'Client wants to be able to choose different colors, fonts, and layouts for each module'
        )
        # User can see the fist feature request's client name
        clientName = self.browser.find_element_by_xpath('//*[@id="main"]/table/tbody/tr[2]/td[2]/span[1]')
        self.assertEqual(
            clientName.text,
            'Mandel Jamesdottir'
        )
        # User can see the fist feature request's client priority
        clientPriority = self.browser.find_element_by_xpath('//*[@id="main"]/table/tbody/tr[2]/td[2]/span[4]')
        self.assertEqual(
            clientPriority.text,
            '1'
        )
        # User can see the fist feature request's target date
        targetDate = self.browser.find_element_by_xpath('//*[@id="main"]/table/tbody/tr[2]/td[2]/span[6]')
        self.assertEqual(
            targetDate.text,
            '2016-08-21'
        )
        # User can see the fist feature request's ticket URL
        ticketUrl = self.browser.find_element_by_xpath('//*[@id="main"]/table/tbody/tr[2]/td[2]/a')
        self.assertEqual(
            ticketUrl.text,
            'http://localhost:5000/8VZuWu'
        )
        # User can see the fist feature request's product area
        productArea = self.browser.find_element_by_xpath('//*[@id="main"]/table/tbody/tr[2]/td[2]/p[1]/b')
        self.assertEqual(
            productArea.text,
            'Policies'
        )
        # User can see the fist feature request's agent name
        agentName = self.browser.find_element_by_xpath('//*[@id="main"]/table/tbody/tr[2]/td[2]/span[11]')
        self.assertEqual(
            agentName.text,
            'Eleuthere'
        )
        # User can see the fist feature request's created at
        createdAt = self.browser.find_element_by_xpath('')
        self.assertEqual(
            createdAt.text,
            ''
        )
        # User can see the fist feature request's status (open, closed)
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

if __name__ == '__main__':
    unittest.main()
