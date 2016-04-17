from POM.BaseTestCase import BaseTestCase
from POM.LoginLogoutPage import LoginPage
from POM.FollowUpOrderPage import FollowUpOrdersPage


class FollowUpOrder(BaseTestCase):
    def test_FollowOrder_valid(self):
        LoginPage.login_with_valid_credentials(self, 'csadek@integrant.com', 'ZAQ!cde3')
        FollowUpOrdersPage.FollowOrder(self)
        FollowUpOrdersPage.get_Status_Name(self)
        self.assertIn('Payment pending', FollowUpOrdersPage.get_Status_Name(self))
        FollowUpOrdersPage.ClickOnStatus(self)
        FollowUpOrdersPage.get_Order_Number(self)
        self.assertIn('12',FollowUpOrdersPage.get_Order_Number(self))
