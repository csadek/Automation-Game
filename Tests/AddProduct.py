from POM.BaseTestCase import BaseTestCase
from POM.LoginLogoutPage import LoginLogoutPage
from POM.AddProductPage import AddProductPage
from Utilities.ReadExcel import ReadExcel
from ddt import ddt, data, unpack


@ddt
class AddProduct(BaseTestCase):

    @data(*ReadExcel.get_data('../Utilities/Data.xlsx','Clothes'))
    @unpack
    def test_Add_Product(self,position,reference,code,price,name,short,description):
        LoginLogoutPage.login_with_valid_credentials(self, 'csadek@integrant.com', 'ZAQ!cde3')
        AddProductPage.admin_view(self)
        AddProductPage.AddProduct(self,position,reference,code,price,name,short,description)
        self.assertIn(name,AddProductPage.get_Page_Name(self))