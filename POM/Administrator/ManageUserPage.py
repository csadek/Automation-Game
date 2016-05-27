from selenium.webdriver.common.by import By
from POM.Administrator.AdminBase import AdminBase


class ManageUserPage(AdminBase):
    """ this class represents manage users page elements manipulations and functions"""
    '''give user admin permission'''

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

        self.driver.find_element(*ManageUserPage.edit).click()
        #change permission
        for i in self.driver.find_elements(*ManageUserPage.user_permission):
            if i.text != '[Jamaica] Client':
                i.click()