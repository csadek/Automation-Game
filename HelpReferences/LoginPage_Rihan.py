from selenium.webdriver.common.by import By
from HelpReferences.basetestcase import BaseTestCase


class LoginPage(BaseTestCase):
    """ this class represent login page elements manipulations and functions"""

    # Locators
    USERNAME = (By.ID, 'email')
    PASSWORD = (By.ID, 'mot_passe')
    LOGIN_BTN = (By.CLASS_NAME, 'btn btn-primary')
    Error_LBL = (By.CLASS_NAME, 'alert alert-danger fade in')

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)

    def set_email(self, email):
        emailElement = self.driver.find_element(*LoginPage.USERNAME)
        emailElement.send_keys(email)

    def login_error_displayed(self):
        notifcationElement = self.driver.find_element(*LoginPage.Error_LBL)
        return notifcationElement.is_displayed()

    def set_password(self, password):
        pwordElement = self.driver.find_element(*LoginPage.PASSWORD)
        pwordElement.send_keys(password)

    def click_submit(self):
        submitBttn = self.driver.find_element(*LoginPage.LOGIN_BTN)
        submitBttn.click()

    def login(self, email, password):
        self.set_password(password)
        self.set_email(email)
        self.click_submit()