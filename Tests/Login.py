from POM.BaseTestCase import BaseTestCase
from POM.LoginPage import LoginPage


class Login(BaseTestCase):

    def Open(self):
        LoginPage.Open_Login_Page(self)

    def test_login_incorrect(self):
        LoginPage.login_with_Invalid_credentials(self, 'test123@email.com', 'password')

    def test_login_blank_password(self):
        LoginPage.login_with_Invalid_credentials2(self, 'test@email.com', '')

    def test_login_blank_email(self):
        login_obj = LoginPage()
        LoginPage.login_with_Invalid_credentials(self, '', 'password')

    def test_login_valid(self):
        LoginPage.login_with_valid_credentials(self, 'eng.mohammadrihan@gmail.com', 'h0tr1ngG')
