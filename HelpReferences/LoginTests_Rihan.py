import unittest
from HelpReferences.basetestcase import BaseTestCase
from HelpReferences import LoginPage_Rihan


class LoginTests_Rihan(BaseTestCase):
    def test_login(self, username, password):
        username = 'eng.mohammadrihan@gmail.com'
        password = 'h0tr1ngG'

    def test_login_incorrect_email(self):
       login_page = LoginPage_Rihan.LoginPage(self.driver)
       login_page.login('test123@email.com', 'password')
       assert login_page.login_error_displayed()

    def test_login_blank_password(self):
       login_page = LoginPage_Rihan.LoginPage(self.driver)
       login_page.login('test@email.com', '')
       assert login_page.login_error_displayed()

    def test_login_blank_email(self):
       login_page = LoginPage_Rihan.LoginPage(self.driver)
       login_page.login('', 'password')
       assert login_page.login_error_displayed()



