from selenium.webdriver.common.by import By
from POM.BaseTestCase import BaseTestCase


class ManageUserPage(BaseTestCase):
    """ this class represents manage users page elements manipulations and functions"""

    # Navigators
    admin_button = (By.CSS_SELECTOR,'#main_content > div:nth-child(1) > div > div > div.middle_column_repeat > div > a.btn.btn-warning.pull-right')
    main_menu = (By.CSS_SELECTOR, '#menu_label_users')
    sub_menu = (By.CSS_SELECTOR, '#menu_3233bb4a')
    user_list_link = (By.CSS_SELECTOR,'a[href^=\"http://10.1.22.67/Jamaica/administrer/utilisateurs.php\"]')

    # Locators
    edit = (By.CSS_SELECTOR,'#tablesForm > tbody > tr:nth-child(2) > td:nth-child(1) > table > tbody > tr:nth-child(1) > td:nth-child(3) > a > img')
    user_permission = (By.CSS_SELECTOR,'select[name="priv[]"] option')
    save_button = (By.CSS_SELECTOR,'#total > div.container > div > div > form:nth-child(1) > table > tbody > tr:nth-child(53) > td > p > input')

    # naviagate to admin pages
    def admin_view(self):
        self.driver.find_element(*ManageUserPage.admin_button).click()
    #Add Product
    def edit_user(self):
        #Open edit user page
        self.driver.find_element(*ManageUserPage.main_menu).click()
        self.driver.find_element(*ManageUserPage.sub_menu).click()
        self.driver.find_element(*ManageUserPage.user_list_link).click()
        self.driver.find_element(*ManageUserPage.edit).click()
        #change permission
        for i in self.driver.find_elements(*ManageUserPage.user_permission):
            if i.text != '[Jamaica] Client':
                i.click()