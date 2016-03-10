import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class searchTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

      # navigate to the application home page
        self.driver.get("http://10.1.22.67/Jamaica/")
        self.driver.find_element_by_class_name("header_user_text").click()
        self.driver.find_element_by_name("email").send_keys("csadek")
        self.driver.find_element_by_name("mot_passe").send_keys("ZAQ!cde3")
        self.driver.find_element_by_class_name("btn-success").click()

    def test_search_products(self):

        select_category = Select(self.driver.find_element_by_id("search_category"))
        select_category.select_by_index(1)
        self.driver.find_element_by_class_name("btn-header_search").click()

        self.driver.find_element_by_partial_link_text ("trouser").click()
        self.driver.find_element_by_name("Add to cart").click()


