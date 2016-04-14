from selenium.webdriver.common.by import By
from POM.BaseTestCase import BaseTestCase


class AddFlashSalePage(BaseTestCase):
    """ this class represents add product page elements manipulations and functions"""

    # Navigators
    admin_button = (By.CSS_SELECTOR,'#main_content > div:nth-child(1) > div > div > div.middle_column_repeat > div > a.btn.btn-warning.pull-right')
    main_menu = (By.CSS_SELECTOR, '#menu_label_products')
    sub_menu = (By.CSS_SELECTOR, '#menu_1bd8d94f')
    edit_product_link = (By.CSS_SELECTOR,'a[href^=\"http://10.1.22.67/Jamaica/administrer/produits.php\"]')
    edit_product = (By.CSS_SELECTOR,'#total > div.container > div > div > div.table-responsive > table > tbody > tr.classe1 > td:nth-child(1) > a:nth-child(2) > img')

    # Locators
    #Flash Sale locators
    page_title = (By.CSS_SELECTOR,'#page_title > h1')
    flash_sale_price = (By.NAME,'prix_flash')
    start_date = (By.NAME, 'flash_start')
    end_date = (By.NAME, 'flash_end')
    show_in_flash_section =(By.CSS_SELECTOR, '#tab1 > table > tbody > tr:nth-child(51) > td:nth-child(2) > input[type="checkbox"]')
    save_changes_button = (By.CSS_SELECTOR,'#total > div.container > div > div > form > div.center > p > input')

    #Add Product
    def AddFlashSale(self,price,start,end):
        # Open Add product page
        self.driver.find_element(*AddFlashSalePage.admin_button).click()
        self.driver.find_element(*AddFlashSalePage.main_menu).click()
        self.driver.find_element(*AddFlashSalePage.sub_menu).click()
        self.driver.find_element(*AddFlashSalePage.edit_product_link).click()
        self.driver.find_element(*AddFlashSalePage.edit_product).click()

        #add flash sale
        self.driver.find_element(*AddFlashSalePage.flash_sale_price).clear()
        self.driver.find_element(*AddFlashSalePage.flash_sale_price).send_keys(price)
        self.driver.find_element(*AddFlashSalePage.start_date).clear()
        self.driver.find_element(*AddFlashSalePage.start_date).send_keys(start)
        self.driver.find_element(*AddFlashSalePage.end_date).clear()
        self.driver.find_element(*AddFlashSalePage.end_date).send_keys(end)

        #submit
        self.driver.find_element(*AddFlashSalePage.save_changes_button).click()

    def get_Page_Name(self):
        return self.driver.find_element(*AddFlashSalePage.page_title).text



