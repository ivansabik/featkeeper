from selenium import webdriver
import unittest

class NewFeatureTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_click_and_display_form(self):
        self.fail('test_can_click_and_display_form Not finished')

    def test_create_new_feature(self):
        self.fail('test_create_new_feature Not finished')

    def test_see_validation_fail(self):
        self.fail('test_see_validation_fail Not finished')

    if __name__ == '__main__':
        unittest.main()
