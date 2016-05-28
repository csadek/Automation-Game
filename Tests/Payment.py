
from ddt import ddt, data, unpack

from POM.Customer.searchPage import SearchPage
from POM.Customer.PaymentPages import PaymentPages
from Tests.BaseTestCase import BaseTestCase
from Utilities.ReadExcel import ReadExcel


@ddt
class Payment(BaseTestCase):

    @data(*ReadExcel.get_sheets('../Utilities/Data.xlsx',['LoginValid','Products']))
    @unpack
    def test_payment2(self,userName,Password,productName,Category):
        SearchPage.search_valid_Data(self,userName,Password,productName,Category)
        PaymentPages.Pay_Oneproduct(self,'grey','Large','2')

    @data(*ReadExcel.get_sheet('../Utilities/Data.xlsx','BillingAddress'))
    @unpack
    def test_payment(self,company,surname,name,email,phone,address,zipcode,town,country):
        PaymentPages.Billing_Address(self,company,surname,name,email,phone,address,zipcode,town,country)
        self.driver.get_screenshot_as_file('screenshot_PayConfirm.jpg')

        PaymentPages.get_Confirm_Msg(self)
        self.assertIn('Confirmation of your order',PaymentPages.get_Confirm_Msg(self))
