from POM.LoginPage import LoginPage

from Archive.LogoutPage import LogoutPage
from POM.BaseTestCase import BaseTestCase


class Logout(BaseTestCase):

    def test_logout(self):
        LoginPage.Open_Login_Page(self)
        LoginPage.login_with_valid_credentials(self, 'csadek@integrant.com', 'ZAQ!cde3')
        LogoutPage.logout(self)
