from POM.PaymentPages import PaymentPages
from POM.BaseTestCase import BaseTestCase
from POM.LoginLogoutPage import LoginLogoutPage
from POM.searchPage import SearchPage
from Utilities.ReadExcel import ReadExcel
from ddt import ddt, data, unpack

@ddt
class Payment(BaseTestCase):
    @data(*ReadExcel.get_data('../Utilities/Data.xlsx','BillingAddress'))
    @unpack
    def test_payment(self,company,surname,name,email,phone,address,zipcode,town,country,comment):
        LoginLogoutPage.login_with_valid_credentials(self, 'csadek@integrant.com', 'ZAQ!cde3')
        SearchPage.search_valid_Data(self,'trouser','Clothing')
        PaymentPages.Pay_Oneproduct(self)
        PaymentPages.Billing_Address(self,company,surname,name,email,phone,address,zipcode,town,country,comment)
        self.driver.get_screenshot_as_file('screenshot_PayConfirm.jpg')
        PaymentPages.get_Confirm_Msg(self)
        self.assertIn('Confirmation of your order',PaymentPages.get_Confirm_Msg(self))
