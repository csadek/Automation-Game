from selenium.webdriver.common.by import By
from POM.BaseTestCase import BaseTestCase

class SearchPage(BaseTestCase):

    CategoryList = (By.ID,'search_category')
    SearchButton =  (By.CLASS_NAME,'btn-header_search')
    SearchResult= (By.PARTIAL_LINK_TEXT,"trouser")
    AddToCardBtn = (By.NAME,'Add to cart')

    def search_vaild_Data(self):

        select_category=self.driver.find_element(*SearchPage.CategoryList)
        select_category.select_by_index(1)
        self.driver.find_element_by_class_name("btn-header_search").click()
        self.driver.find_element_by_partial_link_text ("trouser").click()
        self.driver.find_element_by_name("Add to cart").click()