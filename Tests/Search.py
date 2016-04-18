from POM.BaseTestCase import BaseTestCase
from POM.searchPage  import SearchPage
from POM.LoginLogoutPage import LoginLogoutPage


class Search(BaseTestCase):

    def test_search_Exist_products(self):
        LoginLogoutPage.login_with_valid_credentials(self,"csadek","ZAQ!cde3")
        SearchPage.search_valid_Data(self,'TROUSER ','Clothing')
        SearchPage.get_Product_Name(self)

        self.assertIn('TROUSER',SearchPage.get_Product_Name(self))

    def test_not_exist_Product(self):
         LoginLogoutPage.login_with_valid_credentials(self,"csadek","ZAQ!cde3")
         SearchPage.search_not_exist_Product(self,'DRESS')
         self.assertTrue('No product for this search.',SearchPage.get_not_found_Msg(self))


