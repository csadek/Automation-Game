from selenium.webdriver.common.by import By
from POM.BaseTestCase import BaseTestCase


class LoginLogoutPage(BaseTestCase):
    """ this class represent login page elements manipulations and functions"""
    # Navigator
    login_link = (By.CSS_SELECTOR,'#header_login > div > a > span.hidden-xs > span.header_user_text')
    # Locators
    username = (By.CSS_SELECTOR,'#compte_login_mini > form > table > tbody > tr:nth-child(1) > td.module_login_email > input')
    password =(By.CSS_SELECTOR,'#compte_login_mini > form > table > tbody > tr:nth-child(2) > td.module_login_password > input')
    login_button = (By.CSS_SELECTOR,'#compte_login_mini > form > table > tbody > tr:nth-child(3) > td > input.btn.btn-success')
    Error_LBL = (By.CSS_SELECTOR, 'div[class=\'alert alert-danger fade in\']')
    #logout
    log_out_admin = (By.CSS_SELECTOR, '#total > div.navbar.navbar-inverse.navbar-static-top > div > div > div.navbar-collapse.collapse > nav > ul.nav.nav-pills.pull-right > li:nth-child(2) > a')
    logout_link = (By.CSS_SELECTOR,'#header_login > div > a > span.hidden-xs > span.header_user_text')
    logout_user = (By.CSS_SELECTOR,'#header_login > div > div > div > div > a:nth-child(8)')

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
        elif self.driver.current_url == 'http://10.1.22.67/Jamaica/':
            pass
        else:
            self.driver.find_element(*LoginLogoutPage.logout_link).click()
            self.driver.find_element(*LoginLogoutPage.logout_user).click()