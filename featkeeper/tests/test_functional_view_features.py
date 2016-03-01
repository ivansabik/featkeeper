from selenium import webdriver
import unittest
import os

class ViewFeaturesTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_view_features(self):
        self._take_screenshot(self.browser, 'test_view_features.png', '/tmp')
        self.fail('test_view_features Not finished')

    def _take_screenshot(self, driver, name, save_location):
        path = os.path.abspath(save_location)
        if not os.path.exists(path):
            os.makedirs(path)
        full_path = path + '/' + name
        driver.save_screenshot(full_path)
        return full_path

    if __name__ == '__main__':
        unittest.main()
