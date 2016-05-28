import pymysql
from selenium.webdriver.common.by import By
from Tests.BaseTestCase import BaseTestCase
from POM.LoginLogoutPage import LoginLogoutPage


class SearchPage(BaseTestCase):
    '''search product with no category
    search all products at specific category
    assert on each function'''
    SearchBox = (By.NAME,'search')
    CategoryList = (By.ID,'search_category')
    SearchButton =  (By.CLASS_NAME,'btn-header_search')
    SearchResult= (By.PARTIAL_LINK_TEXT,"trouser")
    AddToCardBtn = (By.NAME,'Add to cart')
    ProductName = (By.CSS_SELECTOR,'#main_content > div:nth-child(1) > div > div > div.middle_column_repeat > h1')
    emptyResults = (By.CLASS_NAME ,'search_result')
    list_of_products = (By.CSS_SELECTOR, 'div[class="produits row allow_order"] > div')


    def search_valid_Data(self,userName,Password,ProductName,CategoryName):
        LoginLogoutPage.login_with_valid_credentials(self,userName,Password)
        self.driver.find_element(*SearchPage.SearchBox).send_keys(ProductName)
        self.driver.find_element(*SearchPage.CategoryList).send_keys(CategoryName)
        self.driver.find_element(*SearchPage.SearchButton).click()

        if CategoryName == "":
            self.driver.find_element(*SearchPage.SearchBox).send_keys(ProductName)
        elif ProductName == "":
            self.driver.find_element(*SearchPage.CategoryList).send_keys(CategoryName)
            self.driver.find_element(*SearchPage.SearchButton).click()
            self.driver.implicitly_wait(30)
            no_of_products = len(self.driver.find_elements(*SearchPage.list_of_products))
            conn = pymysql.connect(host='10.1.22.67', port=3306, user='Selenium', passwd='python', db='peel')
            cur = conn.cursor()
            cur.execute("count FROM `peel_codes_promos` WHERE `date_fin`> {} && `etat` = 1".format(end_date))
            coupon_data = cur.fetchone()[0]
            return coupon_data


    def search_not_exist_Product(self,ProductName):
        self.driver.find_element(*SearchPage.SearchBox).send_keys(ProductName)
        self.driver.find_element(*SearchPage.SearchButton).click()


    def get_Product_Name(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*SearchPage.ProductName).text

    def get_not_found_Msg(self):
        return self.driver.find_element(*SearchPage.emptyResults).text
