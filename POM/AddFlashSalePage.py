from selenium.webdriver.common.by import By
from POM.BaseTestCase import BaseTestCase
from dateutil import parser
import datetime
import re


class AddFlashSalePage(BaseTestCase):
    """ this class represents add product page elements manipulations and functions"""
    '''pay with the new price'''

    # Navigators
    admin_button = (By.CSS_SELECTOR,'#main_content > div:nth-child(1) > div > div > div.middle_column_repeat > div > a.btn.btn-warning.pull-right')
    main_menu = (By.CSS_SELECTOR, '#menu_label_products')
    sub_menu = (By.CSS_SELECTOR, '#menu_1bd8d94f')
    edit_product_link = (By.CSS_SELECTOR,'a[href^=\"http://10.1.22.67/Jamaica/administrer/produits.php\"]')

    # Locators
    # Flash Sale locators
    page_title = (By.CSS_SELECTOR,'#page_title > h1')
    flash_sale_price = (By.NAME,'prix_flash')
    start_date = (By.NAME, 'flash_start')
    end_date = (By.NAME, 'flash_end')
    show_in_flash_section =(By.CSS_SELECTOR, '#tab1 > table > tbody > tr:nth-child(51) > td:nth-child(2) > input[type="checkbox"]')
    save_changes_button = (By.CSS_SELECTOR,'#total > div.container > div > div > form > div.center > p > input')
    alert = (By.CSS_SELECTOR,'div[class=\'alert alert-success fade in\']')

    view_online = (By.CSS_SELECTOR,'#page_title > h1 > a')
    price = (By.ID,'prix_28')
    old_price = (By.CSS_SELECTOR,'#detailsajout28 > div > div > table > tbody > tr:nth-child(2) > td > del')
    remaining_time = (By.CSS_SELECTOR,'div.alert.alert-warning')

    # Add flash sale
    def AddFlashSale(self,price,start,end,name):
        # Open edit page
        self.driver.find_element(*AddFlashSalePage.admin_button).click()
        self.driver.find_element(*AddFlashSalePage.main_menu).click()
        self.driver.find_element(*AddFlashSalePage.sub_menu).click()
        self.driver.find_element(*AddFlashSalePage.edit_product_link).click()
        self.driver.find_element_by_css_selector('a[title=\'Delete {}\']+a[title=\'Modify\']'.format(name)).click()

        # add flash sale
        self.driver.find_element(*AddFlashSalePage.flash_sale_price).clear()
        self.driver.find_element(*AddFlashSalePage.flash_sale_price).send_keys(int(price))
        self.driver.find_element(*AddFlashSalePage.start_date).click()
        self.driver.find_element(*AddFlashSalePage.start_date).clear()
        self.driver.find_element(*AddFlashSalePage.start_date).send_keys(start)
        self.driver.find_element(*AddFlashSalePage.end_date).click()
        self.driver.find_element(*AddFlashSalePage.end_date).clear()
        self.driver.find_element(*AddFlashSalePage.end_date).send_keys(end)

        # submit
        self.driver.find_element(*AddFlashSalePage.save_changes_button).click()
        return self.driver.find_element(*AddFlashSalePage.alert).text

    def verify_flash_sale(self,name):
        # Open Add product page
        self.driver.find_element(*AddFlashSalePage.main_menu).click()
        self.driver.find_element(*AddFlashSalePage.sub_menu).click()
        self.driver.find_element(*AddFlashSalePage.edit_product_link).click()
        self.driver.find_element_by_css_selector('a[title=\'Delete {}\']+a[title=\'Modify\']'.format(name)).click()
        window_before = self.driver.window_handles[0]
        print(window_before)

        # view online
        self.driver.find_element(*AddFlashSalePage.view_online).click()
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        print(window_after)
        new = self.driver.find_element(*AddFlashSalePage.price).text
        whole_text = new.split(',')
        no = whole_text[0]
        return int(no)

    def verify_remaining_time(self,end_time):
        alert1 = self.driver.find_element(*AddFlashSalePage.remaining_time).text
        time_list = re.findall(r'(?:\d)?\d+', alert1)
        now = datetime.datetime.now()
        remaining_time = parser.parse(end_time) - now
        if remaining_time.days == time_list[0]:
            return True
        else:
            return False

        




