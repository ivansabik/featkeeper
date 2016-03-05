'''
test_functional_new_feature.py
Tests user stories and specs for adding a new feature request
@todo: Should validate wrong input fields
'''

from selenium import webdriver
import unittest
import os

class NewFeatureTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_click_and_display_form(self):
        # User navigates to home page, he can see a button to add a new feature request
        self.browser.get('http://localhost:5000')
        # User can click on the add new feature button and see a form to add feature request info
        self._take_screenshot(self.browser, 'test_can_click_and_display_form.png', '/tmp')
        self.fail('test_can_click_and_display_form Not finished')

    def test_can_create_new_feature_request(self):
        # User can click on the add new feature button and after correclty filling in the required fields see a success message
        self._take_screenshot(self.browser, 'test_create_new_feature_request.png', '/tmp')
        self.fail('test_create_new_feature Not finished')

    def test_can_see_validation_fail(self):
        # User can click on the add new feature button and if any field validation fields, should see an error message
        self._take_screenshot(self.browser, 'test_see_validation_fail.png', '/tmp')
        self.fail('test_see_validation_fail Not finished')

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
