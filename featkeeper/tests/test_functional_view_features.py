from selenium import webdriver
import unittest

class ViewFeaturesTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_view_features(self):
        self.fail('test_view_features Not finished')

    if __name__ == '__main__':
        unittest.main()
