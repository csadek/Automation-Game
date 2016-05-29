from ddt import ddt, data, unpack
from Tests.BaseTestCase import BaseTestCase
from POM.Customer.searchPage import SearchPage
from POM.LoginLogoutPage import LoginLogoutPage
from Utilities.ReadExcel import ReadExcel


@ddt
class Search(BaseTestCase):

    @data(*ReadExcel.get_sheets('../Utilities/Data.xlsx',['LoginValid','Search']))
    @unpack
    def test_search(self,username,password,scen,productName,Category,result):
        LoginLogoutPage.login_with_valid_credentials(self, username, password)
        self.assertIn(result,SearchPage.search_data(self,productName,Category))





