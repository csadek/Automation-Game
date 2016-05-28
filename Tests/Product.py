from ddt import ddt, data, unpack
from POM.Administrator.ProductsModule import ProductsModule
from Tests.BaseTestCase import BaseTestCase
from Utilities.ReadExcel import ReadExcel


@ddt
class AddProduct(BaseTestCase):

    @data(*ReadExcel.get_sheets('../Utilities/Data.xlsx',['LoginValid','Clothes']))
    @unpack
    def test_Add_Product(self,username,password,position,reference,code,price,name,short,description):
        self.assertIn(name,ProductsModule.AddProduct(self,username,password,int(position),reference,code,int(price),name,short,description))

    @data(*ReadExcel.get_sheets('../Utilities/Data.xlsx',['LoginValid','Clothes']))
    @unpack
    def test_delete(self,username,password,position,reference,code,price,name,short,description):
        ProductsModule.delete_product(self,username,password,name)

    @data(*ReadExcel.get_sheets('../Utilities/Data.xlsx',['LoginValid','Product instructions']))
    @unpack
    def test_edit_product(self,username,password,name,tab1,desc1,tab2,desc2):
        ProductsModule.edit_product(self,username,password,name,tab1,desc1,tab2,desc2)

