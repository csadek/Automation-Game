from selenium.webdriver.common.by import By
from POM.BaseTestCase import BaseTestCase
from selenium.webdriver.support.ui import Select


class SearchPage(BaseTestCase):

    SearchBox = (By.NAME,'search')
    CategoryList = (By.ID,'search_category')
    SearchButton =  (By.CLASS_NAME,'btn-header_search')
    SearchResult= (By.PARTIAL_LINK_TEXT,"trouser")
    AddToCardBtn = (By.NAME,'Add to cart')

    def search_vaild_Data(self,ProductName,CategoryName):

        #Product Name
        self.driver.find_element(*SearchPage.SearchBox).send_keys(ProductName)
        #find Category List On Page
        selected_category=self.driver.find_element(*SearchPage.CategoryList)
        selected_category.select_by_name(CategoryName)

        #click on GO to find results
        self.driver.find_element(*SearchPage.SearchButton).click()


