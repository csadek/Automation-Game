from POM.searchPage import SearchPage
from ddt import ddt, data, unpack

from POM.Customer.PaymentPages import PaymentPages
from POM.LoginLogoutPage import LoginLogoutPage
from Tests.BaseTestCase import BaseTestCase
from Utilities.ReadExcel import ReadExcel


@ddt
class Payment(BaseTestCase):
    @data(*ReadExcel.get_data('../Utilities/Data.xlsx','LoginValid'))
    @unpack
    def test_payment1(self,username,password):
        LoginLogoutPage.login_with_valid_credentials(self, username,password)

    @data(*ReadExcel.get_data('../Utilities/Data.xlsx','Products'))
    @unpack
    def test_payment2(self,item,category):
        SearchPage.search_valid_Data(self,item,category)
        PaymentPages.Pay_Oneproduct(self)

    @data(*ReadExcel.get_data('../Utilities/Data.xlsx','BillingAddress'))
    @unpack
    def test_payment(self,company,surname,name,email,phone,address,zipcode,town,country,comment):
        PaymentPages.Billing_Address(self,company,surname,name,email,phone,address,zipcode,town,country,comment)
        self.driver.get_screenshot_as_file('screenshot_PayConfirm.jpg')

        PaymentPages.get_Confirm_Msg(self)
        self.assertIn('Confirmation of your order',PaymentPages.get_Confirm_Msg(self))
