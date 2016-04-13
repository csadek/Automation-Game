from selenium.webdriver.common.by import By
from POM.BaseTestCase import BaseTestCase


class AddProductPage(BaseTestCase):

    """ this class represents add product page elements manipulations and functions"""

    # Navigators
    admin_button = (By.CSS_SELECTOR,'#main_content > div:nth-child(1) > div > div > div.middle_column_repeat > div > a.btn.btn-warning.pull-right')
    add_product_link = (By.CSS_SELECTOR,'a[href^=\"http://10.1.22.67/Jamaica/administrer/produits.php?mode=ajout\"]')

    # Locators
    page_title = (By.CSS_SELECTOR,'#page_title > h1')
    SelectCategory = (By.NAME,'categories[]')
    Position = (By.NAME,'position')

    #Add Product
    def AddProduct(self):
        self.driver.find_element(*AddProductPage.admin_button).click()
        self.driver.find_element(*AddProductPage.add_product_link).click()
        self.assertEqual("Add product", self.driver.find_element(*AddProductPage.page_title).text)



