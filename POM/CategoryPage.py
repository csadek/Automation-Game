from selenium.webdriver.common.by import By
from POM.BaseTestCase import BaseTestCase


class CategoryPage(BaseTestCase):
    """ this class represents add and delete both category and subcategory elements manipulations and functions"""

    # Navigators
    admin_button = (By.CSS_SELECTOR,'#main_content > div:nth-child(1) > div > div > div.middle_column_repeat > div > a.btn.btn-warning.pull-right')
    main_menu = (By.CSS_SELECTOR, '#menu_label_products')
    sub_menu = (By.CSS_SELECTOR, '#menu_820845ea')
    add_category_link = (By.CSS_SELECTOR,'a[href^=\"http://10.1.22.67/Jamaica/administrer/categories.php?mode=ajout\"]')
    category_list_link = (By.CSS_SELECTOR,'a[href^=\"http://10.1.22.67/Jamaica/administrer/categories.php\"]')

    # Locators
    root_category = (By.CSS_SELECTOR,'#total > div.container > div > div > form > table > tbody > tr:nth-child(3) > td:nth-child(2) > select > option:nth-child(1)')
    view_on_home = (By.CSS_SELECTOR,'#total > div.container > div > div > form > table > tbody > tr:nth-child(5) > td:nth-child(2) > input[type="checkbox"]')
    position = (By.NAME,'position')
    state_online = (By.NAME, 'etat')
    name = (By.NAME,'nom_en')
    parent = (By.CSS_SELECTOR,'#total > div.container > div > div > form > table > tbody > tr:nth-child(3) > td:nth-child(2) > select > option[value]')
    add_category_button = (By.CSS_SELECTOR,'#total > div.container > div > div > form > table > tbody > tr:nth-child(27) > td > p > input')
    # alert
    alert = (By.XPATH,'//*[@id="total"]/div[3]/div/div/div[2]/text()')

    # navigate to admin pages
    def admin_view(self):
        self.driver.find_element(*CategoryPage.admin_button).click()

    # Add category
    def add_category(self,position,name):
        # Open category page
        self.driver.find_element(*CategoryPage.main_menu).click()
        self.driver.find_element(*CategoryPage.sub_menu).click()
        self.driver.find_element(*CategoryPage.add_category_link).click()
        # Add category
        self.driver.find_element(*CategoryPage.root_category).click()
        self.driver.find_element(*CategoryPage.view_on_home).click()
        self.driver.find_element(*CategoryPage.position).send_keys(position)
        self.driver.find_element(*CategoryPage.state_online).click()
        self.driver.find_element(*CategoryPage.name).send_keys(name)
        # submit
        self.driver.find_element(*CategoryPage.add_category_button).click()
        #return self.driver.find_element(*CategoryPage.alert).text

    # Add sub category
    def add_sub_category(self,position,name,parent):
        # Open category page
        self.driver.find_element(*CategoryPage.main_menu).click()
        self.driver.find_element(*CategoryPage.sub_menu).click()
        self.driver.find_element(*CategoryPage.add_category_link).click()
        # Add sub category
        for i in self.driver.find_elements(*CategoryPage.parent):
            if i.text == parent:
                i.click()
        self.driver.find_element(*CategoryPage.view_on_home).click()
        self.driver.find_element(*CategoryPage.position).send_keys(position)
        self.driver.find_element(*CategoryPage.state_online).click()
        self.driver.find_element(*CategoryPage.name).send_keys(name)
        # submit
        self.driver.find_element(*CategoryPage.add_category_button).click()
        #return self.driver.find_element(*CategoryPage.alert).text

    # delete category
    def delete_category(self,idd):
        # Open category page
        self.driver.find_element(*CategoryPage.main_menu).click()
        self.driver.find_element(*CategoryPage.sub_menu).click()
        self.driver.find_element(*CategoryPage.category_list_link).click()
        # delete category
        delete_row = (By.CSS_SELECTOR,'#total > div.container > div > div > div.table-responsive > table > tbody > tr')
        self.driver.find_element(By.CSS_SELECTOR,'a[href="http://10.1.22.67/Jamaica/administrer/categories.php?mode=suppr&id={}"]'.format(idd))






