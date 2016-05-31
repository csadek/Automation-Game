import os
import sys
sys.path.append(os.path.abspath(os.path.join(sys.path[0], os.pardir)))
from Tests.BaseTestCase import BaseTestCase
from POM.LoginLogoutPage import LoginLogoutPage
from POM.NewUser.RegestrationPage import RegistrationPage
from POM.Administrator.ManageUserPage import ManageUserPage
from POM.Customer.ManageBillingAddressPage import ManageBillingAddressPage
from POM.Customer.searchPage import SearchPage
from POM.Customer.PaymentPages import PaymentPages
from POM.Customer.FollowUpOrderPage import FollowUpOrdersPage
from Utilities.ReadExcel import ReadExcel
from ddt import ddt, data, unpack


@ddt
class Smoke(BaseTestCase):

    @unpack
    @data(*ReadExcel.get_sheets('../Utilities/Data.xlsx',['LoginValid','Registration']))
    def test_smoke_testcase1(self,admin,adminpass,email,nickname,password,firstName,surname,company,capacity,dateofbirth,phone,mobile,address,zipcode,town,country,how_do_you_know_our_website, confirm):
        self.assertIn(confirm,RegistrationPage.Register_with_valid_input(self,email,nickname,password,firstName,surname,company,capacity,dateofbirth,phone,mobile,address,zipcode,town,country,how_do_you_know_our_website))
        self.assertTrue(email,RegistrationPage.verify_user_at_DB(self,nickname))
        self.assertIn(email,ManageUserPage.edit_user(self,admin,adminpass,email))
        LoginLogoutPage.logout(self)
        self.assertEqual(email,LoginLogoutPage.login_with_valid_credentials(self,nickname,password))

    @unpack
    @data(*ReadExcel.get_sheets('../Utilities/Data.xlsx',['Products','ShppingAddress']))
    def test_smoke_testcase2(self,productName,Category,surAddress, surName, firstName, email, company, address, zipCode,
                                                town, country, phone):
        ManageBillingAddressPage.navigate_to_manage_billing(self)
        old_billing_no = len(ManageBillingAddressPage.get_billingAddress_list(self).options)
        ManageBillingAddressPage.Create_Another_Address(self, surAddress, surName, firstName, email, company, address,
                                                        zipCode, town, country, phone)

        # assert that the new address is created and added to drop down list
        self.assertIn('Your new address was created.', ManageBillingAddressPage.get_createAddress_msg(self))
        self.assertEqual(old_billing_no+1, len(ManageBillingAddressPage.get_billingAddress_list(self).options))
        self.assertEqual(old_billing_no+1 , len(ManageBillingAddressPage.get_shippingAddress_list(self).options))

        # Make the added address is default billing and shipping address
        ManageBillingAddressPage.get_billingAddress_list(self).select_by_visible_text(surAddress)
        ManageBillingAddressPage.get_shippingAddress_list(self).select_by_visible_text(surAddress)
        SearchPage.search_data(self,productName,Category)
        self.assertIn('Confirmation of your order',PaymentPages.pay_product(self,'grey','Large','2'))
        self.driver.get_screenshot_as_file('screenshot_PayConfirm.jpg')
        self.assertEqual('Payment pending',FollowUpOrdersPage.FollowOrder(self))