import unittest
from selenium import webdriver
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from DataSourceFiles.readxml import Read_Xml


class basetestcase(unittest.TestCase):


    def setUp(self):

        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        # get app url
        url = Read_Xml.read_tag_attribute_from_xml('../DatasourceFiles/configuration.xml', 'url')
        # navigate to the application home page
        self.driver.get(url)


    def tearDown(self):
        # close the browser window
        self.driver.quit()

    def take_screen_shoot(self):
        st = (datetime.now().strftime('%Y-%m-%d %H.%M.%S'))
        file_name = self.driver.title[:11] + st + ".png"
        self.driver.save_screenshot('../ScreenShoots/' + file_name)

    def explicit_wait(self, locator):
        try:
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
            return True
        except NoSuchElementException:
            raise
        return False




