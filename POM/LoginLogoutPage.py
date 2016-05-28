from selenium.webdriver.common.by import By
from Tests.BaseTestCase import BaseTestCase


class LoginLogoutPage(BaseTestCase):
    """ this class represent login page elements manipulations and functions"""
    # Navigator
    login_link = (By.CLASS_NAME,'header_user_text')
    # Locators
    username = (By.NAME,'email')
    password =(By.NAME,'mot_passe')
    login_button = (By.CSS_SELECTOR,'input[class="btn btn-success"')
    Error_LBL = (By.CSS_SELECTOR, 'div[class="alert alert-danger fade in"]')
    #logout
    log_out_admin = (By.CSS_SELECTOR, 'span[class ="glyphicon glyphicon-off"')
    logout_link = (By.CSS_SELECTOR,'#header_login > div > a > span.hidden-xs > span.header_user_text')
    logout_user = (By.LINK_TEXT,'Log out')

    def login_with_Invalid_credentials(self, username, password):
        self.driver.find_element(*LoginLogoutPage.login_link).click()
        self.driver.find_element(*LoginLogoutPage.username).clear()
        self.driver.find_element(*LoginLogoutPage.username).send_keys(username)
        self.driver.find_element(*LoginLogoutPage.password).clear()
        self.driver.find_element(*LoginLogoutPage.password).send_keys(password)
        self.driver.find_element(*LoginLogoutPage.login_button).click()
        return self.driver.find_element(*LoginLogoutPage.Error_LBL)

    def login_with_valid_credentials(self, username, password):
        self.driver.find_element(*LoginLogoutPage.login_link).click()
        self.driver.find_element(*LoginLogoutPage.username).clear()
        self.driver.find_element(*LoginLogoutPage.username).send_keys(username)
        self.driver.find_element(*LoginLogoutPage.password).clear()
        self.driver.find_element(*LoginLogoutPage.password).send_keys(password)
        self.driver.find_element(*LoginLogoutPage.login_button).click()
        return self.driver.find_element(*LoginLogoutPage.login_link).text

    def logout(self):
        if 'http://10.1.22.67/Jamaica/administrer' in self.driver.current_url:
            self.driver.find_element(*LoginLogoutPage.log_out_admin).click()
        elif self.driver.find_element(*LoginLogoutPage.logout_link).text != 'Log in':
            self.driver.find_element(*LoginLogoutPage.logout_link).click()
            self.driver.implicitly_wait(5)
            self.driver.find_element(*LoginLogoutPage.logout_user).click()
