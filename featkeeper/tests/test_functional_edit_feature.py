from selenium import webdriver
import unittest

class EditFeatureTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_edit_feature(self):
        self.fail('test_edit_feature Not finished')

    def test_see_validation_fail(self):
        self.fail('test_see_validation_fail Not finished')

    def test_close_feature(self):
        self.fail('test_close_feature Not finished')

    if __name__ == '__main__':
        unittest.main()
