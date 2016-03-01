from selenium import webdriver
import unittest
import os

class EditFeatureTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_edit_feature_request(self):
        take_screenshot(self.browser, 'test_edit_feature.png', '/tmp')
        self.fail('test_edit_feature Not finished')

    def test_can_see_validation_fail(self):
        self._take_screenshot(self.browser, 'test_see_validation_fail.png', '/tmp')
        self.fail('test_see_validation_fail Not finished')

    def test_can_close_feature_request(self):
        self._take_screenshot(self.browser, 'test_close_feature.png', '/tmp')
        self.fail('test_close_feature Not finished')

    def _take_screenshot(self, driver, name, save_location):
        path = os.path.abspath(save_location)
        if not os.path.exists(path):
            os.makedirs(path)
        full_path = path + '/' + name
        driver.save_screenshot(full_path)
        return full_path

    if __name__ == '__main__':
        unittest.main()
