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
        self.assertEqual(
            feature_requests_list.get_attribute('class'),
            'table'
        )
        # User can see the first feature request on the list
        feature_request_1 = self.browser.find_element_by_id('56d3d524402e5f1cfc273340')
        self.assertEqual(
            feature_requests_list.get_tag_name('tr'),
            'table'
        )
        # User can see the second feature request on the list
        feature_request_2 = self.browser.find_element_by_id('56d3d524402e5f1cfc273340')
        self.assertEqual(
            feature_requests_list.get_tag_name('tr'),
            'table'
        )

        self._take_screenshot(
            self.browser,
            'test_can_view_feature_requests.png',
            '/tmp'
        )
        self.fail('test_view_features Not finished')

    def test_view_specific_feature_request(self):
        # User navigates to home page, he can see a info related to the first request on the list
        self.browser.get('http://localhost:5000')
        # User can see the fist feature request's title
        # User can see the fist feature request's description
        # User can see the fist feature request's client name
        # User can see the fist feature request's client priority
        # User can see the fist feature request's target date
        # User can see the fist feature request's ticket URL
        # User can see the fist feature request's product area
        # User can see the fist feature request's agent name
        # User can see the fist feature request's created at
        # User can see the fist feature request's status (open, closed)
        self._take_screenshot(
            self.browser,
            'test_can_click_and_view_specific_feature_request.png',
            '/tmp'
        )
        self.fail('test_view_features Not finished')

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
