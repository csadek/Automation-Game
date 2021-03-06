from ddt import ddt, data, unpack
from POM.Customer.ProductDetailsPage import ProductDetailsPage
from Tests.BaseTestCase import BaseTestCase
from POM.Customer.searchPage import SearchPage
from POM.LoginLogoutPage import LoginLogoutPage
from Utilities.ReadExcel import ReadExcel


@ddt
class ProductDetails(BaseTestCase):

    @data(*ReadExcel.get_sheets('../Utilities/Data.xlsx',['LoginValid','Products']))
    @unpack
    def test_product_details(self,username,password,productName,Category):
        LoginLogoutPage.login_with_valid_credentials(self,username,password)
        SearchPage.search_data(self,productName,Category)
        ProductDetailsPage.get_product_details(self,productName)
        ProductDetailsPage.give_your_Opinion_page(self,'Very Good')
        ProductDetailsPage.get_product_details(self,productName)
        self.assertTrue(ProductDetailsPage.add_to_notePad_Page(self,productName))
        ProductDetailsPage.get_product_details(self,productName)
        ProductDetailsPage.ge_details_tab(self)






