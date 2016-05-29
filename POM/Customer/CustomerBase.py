import ConfigReader as Conf
from selenium.webdriver.common.by import By
from Tests.BaseTestCase import BaseTestCase
from POM.LoginLogoutPage import LoginLogoutPage


class CustomerBase(BaseTestCase):
    # Navigators


    # navigate to admin pages
    def navigate_to_page(self,username, password):
        if Conf.read_ini_config('Paths','AdminURL') in self.driver.current_url:
            self.driver.get(Conf.read_ini_config('Paths','HomeURL'))
            if self.driver.find_element(*LoginLogoutPage.login_link).text == 'Log in':
                LoginLogoutPage.login_with_valid_credentials(self,username,password)

    def view_users(self):
        self.driver.find_element(*AdminBase.users_main).click()
        self.driver.find_element(*AdminBase.users_sub).click()
        self.driver.find_element(*AdminBase.users_list_link).click()



