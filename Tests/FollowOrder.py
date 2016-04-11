from POM.FollowUp import FollowUp_Orders
from HelpReferences.basetestcase import BaseTestCase
from POM.LoginPage import LoginPage
from selenium.webdriver.common.by import By


class TestPayment(BaseTestCase):

    def test_login_valid(self):
        LoginPage.login_with_valid_credentials(self, 'csadek@integrant.com', 'ZAQ!cde3')

        FollowUp_Orders.FollowOrder(self)