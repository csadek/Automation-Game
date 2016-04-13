from POM.FollowUp import FollowUp_Orders
from POM.BaseTestCase import BaseTestCase
from POM.LoginPage import LoginPage


class TestOrder(BaseTestCase):
    def test_FollowOrder_valid(self):
        LoginPage.login_with_valid_credentials(self, 'csadek@integrant.com', 'ZAQ!cde3')
        FollowUp_Orders.FollowOrder(self)
        FollowUp_Orders.get_Status_Name(self)
        self.assertIn('Payment pending', FollowUp_Orders.get_Status_Name(self))
        FollowUp_Orders.ClickOnStatus(self)
        FollowUp_Orders.get_Order_Number(self)
        self.assertIn('12',FollowUp_Orders.get_Order_Number(self))
