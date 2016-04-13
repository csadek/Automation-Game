from POM.BaseTestCase import BaseTestCase
from POM.LoginPage import LoginPage
from POM.AddProductPage import AddProductPage


class AddProduct(BaseTestCase):

    def test_Add_Product(self):
        LoginPage.login_with_valid_credentials(self, 'csadek@integrant.com', 'ZAQ!cde3')
        AddProductPage.AddProduct(self,50,'04-14-2016 01h50:56','04-15-2016 01h39:56','test1')
        self.assertIn('Products management',AddProductPage.get_Page_Name(self))
