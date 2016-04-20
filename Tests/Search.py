from POM.BaseTestCase import BaseTestCase
from POM.searchPage  import SearchPage
from POM.LoginLogoutPage import LoginLogoutPage
from Utilities.ReadExcel import ReadExcel
from ddt import ddt, data, unpack

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
        self.assertTrue(productName,str.capitalize(SearchPage.get_Product_Name(self)) )

    def test_not_exist_Product(self):
        SearchPage.search_not_exist_Product(self,'DRESS')
        self.assertTrue('No product for this search.',SearchPage.get_not_found_Msg(self))



