from POM.BaseTestCase import BaseTestCase
from POM.LoginLogoutPage import LoginLogoutPage
from POM.ManageBillingAddressPage import ManageBillingAddressPage
from Utilities.ReadExcel import ReadExcel
from ddt import ddt, data, unpack

@ddt
class MangeBilling(BaseTestCase):

    @data(*ReadExcel.get_data('../Utilities/Data.xlsx','BillingAddress'))
    @unpack
    def test_createAnother_Address_Successfully(self,surAddress,surName,firstName,email,company,address,zipCode,town,country,phone):
        LoginLogoutPage.login_with_valid_credentials(self, 'csadek@integrant.com', 'ZAQ!cde3')
        ManageBillingAddressPage.manage_billing(self)
        ManageBillingAddressPage.Create_Another_Address(self,surAddress,surName,firstName,email,company,address,zipCode,town,country,phone)
        self.assertIn('Your new address was created.',ManageBillingAddressPage.get_createAddress_msg(self))

