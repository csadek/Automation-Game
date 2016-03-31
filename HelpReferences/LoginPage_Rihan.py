from selenium.webdriver.common.by import By
from HelpReferences.basetestcase import BaseTestCase


class LoginPage(BaseTestCase):
    """ this class represent login page elements manipulations and functions"""

    # Locators
    USERNAME = (By.CSS_SELECTOR, 'div:nth-child(1) > div > div > div.middle_column_repeat > div > div:nth-child(2) > form > table > tbody > tr:nth-child(1) > td:nth-child(2) > input')
    PASSWORD = (By.CSS_SELECTOR, 'div:nth-child(2) > form > table > tbody > tr:nth-child(2) > td:nth-child(2) > input')
    LOGIN_BTN = (By.CSS_SELECTOR, 'tr:nth-child(3) > td > p > input.btn.btn-primary')
    Error_LBL = (By.CSS_SELECTOR, 'tr:nth-child(1) > td:nth-child(2) > div.alert.alert-danger.fade.in')

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)

    def login_error_displayed(self):
        notifcationElement = self.driver.find_element(*LoginPage.Error_LBL)
        return notifcationElement.is_displayed()

    def click_submit(self):
        submitBttn = self.driver.find_element(*LoginPage.LOGIN_BTN)
        submitBttn.click()

    def login(self, email, password):
        self.driver.find_element(*LoginPage.USERNAME).send_keys(email)
        self.driver.find_element(*LoginPage.PASSWORD).send_keys(password)
        self.click_submit()