from POM.BaseTestCase import BaseTestCase
from POM.LoginLogoutPage import LoginLogoutPage
from POM.FollowUpOrderPage import FollowUpOrdersPage
from Utilities.ReadExcel import ReadExcel
from ddt import ddt, data, unpack

@ddt
class FollowUpOrder(BaseTestCase):

    @data(*ReadExcel.get_data('../Utilities/Data.xlsx','LoginValid'))
    @unpack
    def test_FollowOrder_valid(self, username, password):
        LoginLogoutPage.login_with_valid_credentials(self, username, password)
        FollowUpOrdersPage.FollowOrder(self)
        FollowUpOrdersPage.get_Status_Name(self)
        self.assertIn('Payment pending', FollowUpOrdersPage.get_Status_Name(self))
        FollowUpOrdersPage.ClickOnStatus(self)
        self.assertIn('12',FollowUpOrdersPage.get_Order_Number(self))
