from selenium.webdriver.common.by import By
from POM.BaseTestCase import BaseTestCase
from selenium.webdriver.support.ui import Select


class SearchPage(BaseTestCase):

    SearchBox = (By.NAME,'search')
    CategoryList = (By.ID,'search_category')
    SearchButton =  (By.CLASS_NAME,'btn-header_search')
    SearchResult= (By.PARTIAL_LINK_TEXT,"trouser")
    AddToCardBtn = (By.NAME,'Add to cart')
    ProductName = (By.CSS_SELECTOR,'#main_content > div:nth-child(1) > div > div > div.middle_column_repeat > h1')

    def search_vaild_Data(self,ProductName,CategoryName):

        #Product Name
        self.driver.find_element(*SearchPage.SearchBox).send_keys(ProductName)
        #find Category List On Page
        self.driver.find_element(*SearchPage.CategoryList).send_keys(CategoryName)

        #click on GO to find results
        self.driver.find_element(*SearchPage.SearchButton).click()


    def get_Product_Name(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*SearchPage.ProductName).text