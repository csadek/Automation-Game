from selenium.webdriver.common.by import By
from POM.BaseTestCase import BaseTestCase


class AddCategoryPage(BaseTestCase):
    """ this class represents add category page elements manipulations and functions"""

    # Navigators
    admin_button = (By.CSS_SELECTOR,'#main_content > div:nth-child(1) > div > div > div.middle_column_repeat > div > a.btn.btn-warning.pull-right')
    main_menu = (By.CSS_SELECTOR, '#menu_label_products')
    sub_menu = (By.CSS_SELECTOR, '#menu_820845ea')
    add_category_link = (By.CSS_SELECTOR,'a[href^=\"http://10.1.22.67/Jamaica/administrer/categories.php?mode=ajout\"]')

    # Locators
    root_category = (By.CSS_SELECTOR,'#total > div.container > div > div > form > table > tbody > tr:nth-child(3) > td:nth-child(2) > select > option:nth-child(1)')
    view_on_home = (By.CSS_SELECTOR,'#total > div.container > div > div > form > table > tbody > tr:nth-child(5) > td:nth-child(2) > input[type="checkbox"]')
    position = (By.NAME,'position')
    state_online = (By.NAME, 'etat')
    name = (By.NAME,'nom_en')
    add_category_button = (By.CSS_SELECTOR,'#total > div.container > div > div > form > table > tbody > tr:nth-child(27) > td > p > input')

    # navigate to admin pages
    def admin_view(self):
        self.driver.find_element(*AddCategoryPage.admin_button).click()

    # Add Product
    def add_category(self,position,name):
        # Open category page
        self.driver.find_element(*AddCategoryPage.main_menu).click()
        self.driver.find_element(*AddCategoryPage.sub_menu).click()
        self.driver.find_element(*AddCategoryPage.add_category_link).click()
        # Add category
        self.driver.find_element(*AddCategoryPage.root_category).click()
        self.driver.find_element(*AddCategoryPage.view_on_home).click()
        self.driver.find_element(*AddCategoryPage.position).send_keys(position)
        self.driver.find_element(*AddCategoryPage.state_online).click()
        self.driver.find_element(*AddCategoryPage.name).send_keys(name)
        # submit
        self.driver.find_element(*AddCategoryPage.add_category_button).click()

    def add_sub_category(self,position,name,no):
        # Open category page
        self.no = no
        self.driver.find_element(*AddCategoryPage.main_menu).click()
        self.driver.find_element(*AddCategoryPage.sub_menu).click()
        self.driver.find_element(*AddCategoryPage.add_category_link).click()
        # Add category
        parent = self.driver.find_elements(By.CSS_SELECTOR,'#total > div.container > div > div > form > table > tbody > tr:nth-child(3) > td:nth-child(2) > select > option[value]').text
        parent(no).click()
        self.driver.find_element(*AddCategoryPage.view_on_home).click()
        self.driver.find_element(*AddCategoryPage.position).send_keys(position)
        self.driver.find_element(*AddCategoryPage.state_online).click()
        self.driver.find_element(*AddCategoryPage.name).send_keys(name)
        # submit
        self.driver.find_element(*AddCategoryPage.add_category_button).click()



