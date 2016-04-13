from POM.BaseTestCase import BaseTestCase
from POM.SearchPage import SearchPage
from POM.LoginPage import LoginPage


class SearchTests(BaseTestCase):

    def test_search_Exist_products(self):
        LoginPage.login_with_valid_credentials(self,"csadek","ZAQ!cde3")
        SearchPage.search_valid_Data(self,'trouser','Clothing')
        SearchPage.get_Product_Name(self)
        self.assertIn('TROUSER',SearchPage.get_Product_Name(self))

