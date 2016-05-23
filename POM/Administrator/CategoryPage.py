from selenium.webdriver.common.by import By
from POM.BaseTestCase import BaseTestCase
from selenium.webdriver.common.keys import Keys


class CategoryPage(BaseTestCase):
    """ this class represents add and delete both category and subcategory elements manipulations and functions"""
    """ Admin user should add categories and subcategories to add products to those categories"""
    # Navigators
    admin_button = (By.CSS_SELECTOR,'a[class="btn btn-warning pull-right"]')
    main_menu = (By.CSS_SELECTOR, '#menu_label_products')
    sub_menu = (By.CSS_SELECTOR, '#menu_820845ea')
    add_category_link = (By.CSS_SELECTOR,'a[href^=\"http://10.1.22.67/Jamaica/administrer/categories.php?mode=ajout\"]')
    category_list_link = (By.CSS_SELECTOR,'a[href^=\"http://10.1.22.67/Jamaica/administrer/categories.php\"]')

    # Locators
    root_category = (By.CSS_SELECTOR,'#total > div.container > div > div > form > table > tbody > tr:nth-child(3) > td:nth-child(2) > select > option:nth-child(1)')
    view_on_home = (By.CSS_SELECTOR,'#total > div.container > div > div > form > table > tbody > tr:nth-child(5) > td:nth-child(2) > input[type="checkbox"]')
    state_online = (By.NAME, 'etat')
    name = (By.NAME,'nom_en')
    parent = (By.CSS_SELECTOR,'#total > div.container > div > div > form > table > tbody > tr:nth-child(3) > td:nth-child(2) > select > option[value]')
    add_category_button = (By.CSS_SELECTOR,'#total > div.container > div > div > form > table > tbody > tr:nth-child(27) > td > p > input')
    # alert
    alert = (By.CSS_SELECTOR,'div[class=\'alert alert-success fade in\']')
    # category online
    view_online = (By.CSS_SELECTOR, '#total > div.container > div > div > form > table > tbody > tr:nth-child(1) > td > a')
    title = (By.CSS_SELECTOR,'#main_content > div > div > div > div.middle_column_repeat > div:nth-child(2) > h1')

    # Add category or sub category
    def add_category(self,name,parent):
        # Open category page
        if 'http://10.1.22.67/Jamaica/achat' in self.driver.current_url:
            self.driver.get('http://10.1.22.67/Jamaica/compte.php')
            self.driver.find_element(*CategoryPage.admin_button).click()
        elif 'http://10.1.22.67/Jamaica/compte.php' in self.driver.current_url:
            self.driver.find_element(*CategoryPage.admin_button).click()
        else:
            pass
        self.driver.find_element(*CategoryPage.main_menu).click()
        self.driver.find_element(*CategoryPage.sub_menu).click()
        self.driver.find_element(*CategoryPage.add_category_link).click()
        # Add sub category
        if parent == "":
            self.driver.find_element(*CategoryPage.root_category).click()
        else:
            for i in self.driver.find_elements(*CategoryPage.parent):
                if i.text == parent:
                    i.click()
        self.driver.find_element(*CategoryPage.view_on_home).click()
        self.driver.find_element(*CategoryPage.state_online).click()
        self.driver.find_element(*CategoryPage.name).send_keys(name)
        # submit
        self.driver.find_element(*CategoryPage.add_category_button).click()

        # Open edit product page
        self.driver.find_element(*CategoryPage.main_menu).click()
        self.driver.find_element(*CategoryPage.sub_menu).click()
        self.driver.find_element(*CategoryPage.category_list_link).click()
        self.driver.find_element_by_link_text(name).click()

        # view online
        self.driver.find_element(*CategoryPage.view_online).click()
        window_after = self.driver.window_handles[1]
        self.driver.find_element(self.driver.current_window_handle[0]).send_keys(Keys.ALT + Keys.F4)
        self.driver.switch_to.window(window_after)

        # Check category name
        if self.driver.find_element(*CategoryPage.title).text == name:
            return True
        else:
            return False

    # delete category
    def delete_category(self,idd):
        # Open category page
        self.driver.find_element(*CategoryPage.main_menu).click()
        self.driver.find_element(*CategoryPage.sub_menu).click()
        self.driver.find_element(*CategoryPage.category_list_link).click()
        # delete category
        delete_row = (By.CSS_SELECTOR,'#total > div.container > div > div > div.table-responsive > table > tbody > tr')
        self.driver.find_element(By.CSS_SELECTOR,'a[href="http://10.1.22.67/Jamaica/administrer/categories.php?mode=suppr&id={}"]'.format(idd))






