
from selenium.webdriver.common.by import By
from Utilities.BasePage_Mahran import BasePageObject


class LoginPage(BasePageObject):
    """ this class represent login page elements manipulations and functions"""

    # Locators
    USERNAME = (By.CSS_SELECTOR, 'div:nth-child(1) > div > div > div.middle_column_repeat > div > div:nth-child(2) > form > table > tbody > tr:nth-child(1) > td:nth-child(2) > input')
    PASSWORD = (By.CSS_SELECTOR, 'div:nth-child(2) > form > table > tbody > tr:nth-child(2) > td:nth-child(2) > input')
    LOGIN_BTN = (By.CSS_SELECTOR, 'tr:nth-child(3) > td > p > input.btn.btn-primary')
    Error_LBL = (By.CSS_SELECTOR, 'tr:nth-child(1) > td:nth-child(2) > div.alert.alert-danger.fade.in')
    Error_LBL2 = (By.CSS_SELECTOR, 'tr:nth-child(2) > td:nth-child(2) > div.alert.alert-danger.fade.in')

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)

    def login_with_Invalid_credentials(self, username, password):
        self.driver.find_element(*LoginPage.USERNAME).send_keys(username)
        self.driver.find_element(*LoginPage.PASSWORD).send_keys(password)
        self.driver.find_element(*LoginPage.LOGIN_BTN).click()
        error_LBL = self.driver.find_element(*LoginPage.Error_LBL)
        self.assertTrue(error_LBL.is_displayed())


    def login_with_Invalid_credentials2(self, username, password):
        self.driver.find_element(*LoginPage.USERNAME).send_keys(username)
        self.driver.find_element(*LoginPage.PASSWORD).send_keys(password)
        self.driver.find_element(*LoginPage.LOGIN_BTN).click()
        error_LBL = self.driver.find_element(*LoginPage.Error_LBL2)
        self.assertTrue(error_LBL.is_displayed())

    def login_with_valid_credentials(self, username, password):
        self.driver.find_element(*LoginPage.USERNAME).send_keys(username)
        self.driver.find_element(*LoginPage.PASSWORD).send_keys(password)
        self.driver.find_element(*LoginPage.LOGIN_BTN).click()


