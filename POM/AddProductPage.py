from selenium.webdriver.common.by import By
from POM.BaseTestCase import BaseTestCase


class AddProductPage(BaseTestCase):
    """ this class represents add product page elements manipulations and functions"""

    # Navigators
    admin_button = (By.CSS_SELECTOR,'#main_content > div:nth-child(1) > div > div > div.middle_column_repeat > div > a.btn.btn-warning.pull-right')
    main_menu = (By.CSS_SELECTOR, '#menu_label_products')
    sub_menu = (By.CSS_SELECTOR, '#menu_1bd8d94f')
    add_product_link = (By.CSS_SELECTOR,'a[href^=\"http://10.1.22.67/Jamaica/administrer/produits.php?mode=ajout\"]')

    # Locators
    # first tab
    page_title = (By.CSS_SELECTOR,'#page_title > h1')
    select_category = (By.CSS_SELECTOR,'#categories > option:nth-child(1)')
    position = (By.NAME,'position')
    our_selection = (By.NAME, 'on_special')
    state_online = (By.NAME, 'etat')

     # Second tab
    english_tab = (By.CSS_SELECTOR,'a[href="#tab_EN"]')
    product_name = (By.CSS_SELECTOR,'#tab_EN > input:nth-child(3)')
    add_product_button = (By.CSS_SELECTOR,'#total > div.container > div > div > form > div.center > p > input')

    #Add Product
    def AddProduct(self,name):
        # Open Add product page
        self.driver.find_element(*AddProductPage.admin_button).click()
        self.driver.find_element(*AddProductPage.main_menu).click()
        self.driver.find_element(*AddProductPage.sub_menu).click()
        self.driver.find_element(*AddProductPage.add_product_link).click()

        #Add first
        self.driver.find_element(*AddProductPage.select_category).click()
        self.driver.find_element(*AddProductPage.our_selection).click()
        self.driver.find_element(*AddProductPage.state_online).click()

        # add second tab
        self.driver.find_element(*AddProductPage.english_tab).click()
        self.driver.find_element(*AddProductPage.product_name).send_keys(name)

        #submit
        self.driver.find_element(*AddProductPage.add_product_button).click()

    def get_Page_Name(self):
        return self.driver.find_element(*AddProductPage.page_title).text



