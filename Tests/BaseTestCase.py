import unittest
from selenium import webdriver


# BaseTestCase class, which will provide us with the setUp() and tearDown() methods
# so that we don't need to write these for each test class we create.
class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        # navigate to the application home page
        self.driver.get('http://10.1.22.67/jamaica/')

    def tearDown(self):
        # close the browser window
        self.driver.quit()
