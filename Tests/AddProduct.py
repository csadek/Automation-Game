from ddt import ddt, data, unpack

from POM.Administrator.ProductsModule import ProductsModule
from POM.BaseTestCase import BaseTestCase
from POM.LoginLogoutPage import LoginLogoutPage
from Utilities.ReadExcel import ReadExcel


@ddt
class AddProduct(BaseTestCase):

    @data(*ReadExcel.get_data('../Utilities/Data.xlsx','LoginValid'))
    @unpack
    def test_Add(self,user,password):
        LoginLogoutPage.login_with_valid_credentials(self, user, password)


    @data(*ReadExcel.get_data('../Utilities/Data.xlsx','Clothes'))
    @unpack
    def test_Add_Product(self,position,reference,code,price,name,short,description):
        self.assertIn(name,ProductsModule.AddProduct(self,position,reference,code,price,name,short,description))

    @data(*ReadExcel.get_data('../Utilities/Data.xlsx','Clothes'))
    @unpack
    def test_delete(self,position,reference,code,price,name,short,description):
        ProductsModule.delete_product(self,name)

    @data(*ReadExcel.get_data('../Utilities/Data.xlsx','Clothes'))
    @unpack
    def test_edit_product(self,position,reference,code,price,name,short,description):
        ProductsModule.edit_product(self,name)

    def test_end(self):
        LoginLogoutPage.logout(self)
