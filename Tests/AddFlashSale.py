from POM.BaseTestCase import BaseTestCase
from POM.LoginLogoutPage import LoginLogoutPage
from POM.AddFlashSalePage import AddFlashSalePage
from Utilities.ReadExcel import ReadExcel
from ddt import ddt, data, unpack


@ddt
class AddFlashSale(BaseTestCase):

    @data(*ReadExcel.get_data('../Utilities/Data.xlsx','LoginValid'))
    @unpack
    def test_Add(self,user,password):
        LoginLogoutPage.login_with_valid_credentials(self, user, password)

    @data(*ReadExcel.get_data('../Utilities/Data.xlsx','flash'))
    @unpack
    def test_Add_flash_sale(self,amount,start,end):
        AddFlashSalePage.AddFlashSale(self,amount,start,end)
        self.assertIn('Products management',AddFlashSalePage.get_Page_Name(self))
