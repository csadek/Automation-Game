from POM.BaseTestCase import BaseTestCase
from POM.LoginLogoutPage import LoginLogoutPage


class Login(BaseTestCase):

    def test_login_incorrect(self):
        self.assertTrue('Bad email or password.',LoginLogoutPage.login_with_Invalid_credentials(self, 'test123@email.com','password'))

    def test_login_blank_password(self):
        self.assertTrue('Please type in your password.',LoginLogoutPage.login_with_Invalid_credentials2(self, 'test@email.com', ''))

    def test_login_blank_email(self):
        self.assertTrue('Bad email or password.',LoginLogoutPage.login_with_Invalid_credentials(self, 'test123@email.com','password'))

    def test_login_valid(self):
        LoginLogoutPage.login_with_valid_credentials(self, 'eng.mohammadrihan@gmail.com', 'h0tr1ngG')

    def test_logout(self):
        LoginLogoutPage.logout(self)
