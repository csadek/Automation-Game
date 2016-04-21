from POM.BaseTestCase import BaseTestCase
from POM.LoginLogoutPage import LoginLogoutPage
from POM.AddProductPage import AddProductPage
from Utilities.ReadExcel import ReadExcel
from ddt import ddt, data, unpack


@ddt
class AddProduct(BaseTestCase):

    @data(*ReadExcel.get_data('../Utilities/Data.xlsx','LoginValid'))
    @unpack
    def test_Add(self,user,password):
        LoginLogoutPage.login_with_valid_credentials(self, user, password)
        AddProductPage.admin_view(self)

    @data(*ReadExcel.get_data('../Utilities/Data.xlsx','Clothes'))
    @unpack
    def test_Add_Product(self,position,reference,code,price,name,short,description):
        self.assertIn(name,AddProductPage.AddProduct(self,position,reference,code,price,name,short,description))

    @data(*ReadExcel.get_data('../Utilities/Data.xlsx','Clothes'))
    @unpack
    def test_delete(self,position,reference,code,price,name,short,description):
        AddProductPage.delete_product(self,name)

    @data(*ReadExcel.get_data('../Utilities/Data.xlsx','Clothes'))
    @unpack
    def test_edit_product(self,position,reference,code,price,name,short,description):
        AddProductPage.edit_product(self,name)

    def test_end(self):
        LoginLogoutPage.logout(self)
