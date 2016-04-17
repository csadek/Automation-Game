from POM.BaseTestCase import BaseTestCase
from POM.LoginPage import LoginPage
from POM.LogoutPage import LogoutPage


class Logout(BaseTestCase):

    def test_logout(self):
        LoginPage.Open_Login_Page(self)
        LoginPage.login_with_valid_credentials(self, 'csadek@integrant.com', 'ZAQ!cde3')
        LogoutPage.logout(self)
