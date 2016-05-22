from POM.searchPage import SearchPage
from ddt import ddt, data, unpack

from POM.BaseTestCase import BaseTestCase
from POM.Customer.PaymentInvalid_1 import PaymentPages
from POM.LoginLogoutPage import LoginLogoutPage
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
        PaymentPages.Pay_Oneproduct_WithoutColorSize(self)

        PaymentPages.get_Error_Msg(self)
        self.assertEqual("You didn't select a color.",PaymentPages.get_Error_Msg(self))