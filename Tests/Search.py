from POM.BaseTestCase import BaseTestCase
from POM.searchPage  import SearchPage
from POM.LoginLogoutPage import LoginLogoutPage
from POM.ProductDetailsPage import ProductDetails
from Utilities.ReadExcel import ReadExcel
from ddt import ddt, data, unpack

@ddt
class Search(BaseTestCase):

    def test_not_exist_Product(self):
        LoginLogoutPage.login_with_valid_credentials(self,"csadek","ZAQ!cde3")
        SearchPage.search_not_exist_Product(self,'DRESS')
        self.assertTrue('No product for this search.',SearchPage.get_not_found_Msg(self))

    @data(*ReadExcel.get_data('../Utilities/Data.xlsx','Products'))
    @unpack
    def test_search_Exist_products(self,productName,Category):
        LoginLogoutPage.login_with_valid_credentials(self,"csadek","ZAQ!cde3")
        SearchPage.search_valid_Data(self,productName,Category)
        self.assertIn(productName,SearchPage.get_Product_Name(self))




