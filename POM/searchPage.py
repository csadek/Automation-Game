from selenium import webdriver
from selenium.webdriver.support.ui import Select

class SearchPageObject(webdriver):
    Searchbutton = webdriver.find_element_by_class_name("header_user_text")
    webdriver.find_element_by_name("email").send_keys("csadek")
    webdriver.find_element_by_name("mot_passe").send_keys("ZAQ!cde3")
    webdriver.find_element_by_class_name("btn-success").click()

    def test_search_products(self ):
        self.Searchbutton.click();
        select_category = Select(self.driver.find_element_by_id("search_category"))
        select_category.select_by_index(1)
        self.driver.find_element_by_class_name("btn-header_search").click()

        self.driver.find_element_by_partial_link_text ("trouser").click()
        self.driver.find_element_by_name("Add to cart").click()