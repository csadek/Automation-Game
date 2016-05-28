from ddt import ddt, data, unpack
from POM.Customer.ProductDetailsPage import ProductDetails
from Tests.BaseTestCase import BaseTestCase
from POM.Customer.searchPage import SearchPage
from POM.LoginLogoutPage import LoginLogoutPage
from Utilities.ReadExcel import ReadExcel


@ddt
class Search(BaseTestCase):


    @data(*ReadExcel.get_sheet('../Utilities/Data.xlsx','LoginValid'))
    @unpack
    def test_add(self,user,password):
        LoginLogoutPage.login_with_valid_credentials(self, user, password)

    @data(*ReadExcel.get_sheets('../Utilities/Data.xlsx','Products'))
    @unpack
    def test_search_Exist_products(self,username,password,productName,Category):
        SearchPage.search_valid_Data(self,username,password,productName,Category)
        ProductDetails.getProductDetails(self,productName)





