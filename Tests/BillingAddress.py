from ddt import ddt, data, unpack

from POM.BaseTestCase import BaseTestCase
from POM.Customer.ManageBillingAddressPage import ManageBillingAddressPage
from POM.LoginLogoutPage import LoginLogoutPage
from Utilities.ReadExcel import ReadExcel


@ddt
class MangeBilling(BaseTestCase):
    @data(*ReadExcel.get_data('../Utilities/Data.xlsx', 'BillingAddress'))
    @unpack
    def test_createAnother_Address_Successfully(self, surAddress, surName, firstName, email, company, address, zipCode,
                                                town, country, phone):
        LoginLogoutPage.login_with_valid_credentials(self, 'csadek@integrant.com', 'ZAQ!cde3')
        ManageBillingAddressPage.manage_billing(self)
        ManageBillingAddressPage.Create_Another_Address(self, surAddress, surName, firstName, email, company, address,
                                                        zipCode, town, country, phone)

        # assert that the new address is created and added to drop down list
        self.assertIn('Your new address was created.', ManageBillingAddressPage.get_createAddress_msg(self))
        self.assertEqual(4, len(ManageBillingAddressPage.get_billingAddress_list.options))
        self.assertEqual(4, len(ManageBillingAddressPage.get_shippingAddress_list(self).options))

        # Make the added address is default billing and shipping address
        ManageBillingAddressPage.get_billingAddress_list.select_by_visible_text(surAddress)
        ManageBillingAddressPage.get_shippingAddress_list.select_by_visible_text(surAddress)


