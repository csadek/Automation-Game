from selenium.webdriver.common.by import By
from POM.BaseTestCase import BaseTestCase


class LogoutPage(BaseTestCase):
    Logout_Btn = (By.CSS_SELECTOR,'a.btn.btn-primary.pull-right')

    def logout(self):
        self.driver.find_element(*LogoutPage.Logout_Btn).click()