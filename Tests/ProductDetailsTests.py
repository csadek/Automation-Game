from ddt import ddt, data, unpack

from POM.Customer.ProductDetailsPage import ProductDetails
from POM.BaseTestCase import BaseTestCase
from POM.Customer.searchPage import SearchPage
from POM.LoginLogoutPage import LoginLogoutPage
from Utilities.ReadExcel import ReadExcel


@ddt
class Search(BaseTestCase):


    @data(*ReadExcel.get_data('../Utilities/Data.xlsx','LoginValid'))
    @unpack
    def test_add(self,user,password):
        LoginLogoutPage.login_with_valid_credentials(self, user, password)

    @data(*ReadExcel.get_data('../Utilities/Data.xlsx','Products'))
    @unpack
    def test_search_Exist_products(self,productName,Category):
        SearchPage.search_valid_Data(self,productName,Category)
        ProductDetails.getProductDetails(self,productName)
        ProductDetails.zoom_product_image(self)
        ProductDetails.give_your_Opinion_page(self,'Very Good')
        ProductDetails.getProductDetails(self,productName)
        assertNotEquals =( ProductDetails.add_to_notePad_Page(self,productName),True)






