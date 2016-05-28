from ddt import ddt, data, unpack

from POM.Customer.FollowUpOrderPage import FollowUpOrdersPage
from POM.LoginLogoutPage import LoginLogoutPage
from Tests.BaseTestCase import BaseTestCase
from Utilities.ReadExcel import ReadExcel


@ddt
class FollowUpOrder(BaseTestCase):

    @data(*ReadExcel.get_sheet('../Utilities/Data.xlsx','LoginValid'))
    @unpack
    def test_FollowOrder_valid(self, username, password):
        LoginLogoutPage.login_with_valid_credentials(self, username, password)
        FollowUpOrdersPage.FollowOrder(self)
        FollowUpOrdersPage.get_Status_Name(self)
        self.assertIn('Payment pending', FollowUpOrdersPage.get_Status_Name(self))
        FollowUpOrdersPage.ClickOnStatus(self)
        self.assertIn('24',FollowUpOrdersPage.get_Order_Number(self))
