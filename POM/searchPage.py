from selenium.webdriver.common.by import By
from POM.BaseTestCase import BaseTestCase


class SearchPage(BaseTestCase):

    SearchBox = (By.NAME,'search')
    CategoryList = (By.ID,'search_category')
    SearchButton =  (By.CLASS_NAME,'btn-header_search')
    SearchResult= (By.PARTIAL_LINK_TEXT,"trouser")
    AddToCardBtn = (By.NAME,'Add to cart')
    ProductName = (By.CSS_SELECTOR,'#main_content > div:nth-child(1) > div > div > div.middle_column_repeat > h1')
    emptyResults = (By.CLASS_NAME ,'search_result')

    def search_valid_Data(self,ProductName,CategoryName):
        self.driver.find_element(*SearchPage.SearchBox).send_keys(ProductName)
        self.driver.find_element(*SearchPage.CategoryList).send_keys(CategoryName)
        self.driver.find_element(*SearchPage.SearchButton).click()
        self.driver.implicitly_wait(30)

    def search_not_exist_Product(self,ProductName):
        self.driver.find_element(*SearchPage.SearchBox).send_keys(ProductName)
        self.driver.find_element(*SearchPage.SearchButton).click()


    def get_Product_Name(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*SearchPage.ProductName).text

    def get_not_found_Msg(self):
        return self.driver.find_element(*SearchPage.emptyResults).text
