import unittest
from selenium import webdriver


# BaseTestCase class, which will provide us with the setUp() and tearDown() methods
# so that we don't need to write these for each test class we create.
class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        # navigate to the application home page
        cls.driver.get('http://10.1.22.67/Jamaica/search.php?match=1&search=&categorie=1')

    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)