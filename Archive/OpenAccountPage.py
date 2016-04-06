from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest

driver = webdriver.Firefox()

driver.get('http://10.1.22.67/Jamaica/')
driver.implicitly_wait(30)

class OpenAccountPage(webdriver):
        login = webdriver.find_elements_by_xpath("/html/body/div[1]/header/div[1]/div/div[1]/div/div[1]/div/a/span[2]/span[2]")[0]
        OpenAccount_B = webdriver.find_element_by_class_name("btn btn-primary")

def test_OpenAccountPage(self):
        self.login.click()
        self.OpenAccount_B.click()