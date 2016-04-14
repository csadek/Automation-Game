from POM.BaseTestCase import BaseTestCase
from POM.LoginPage import LoginPage
from POM.AddProductPage import AddProductPage


class AddProduct(BaseTestCase):

    def test_Add_Product(self):
        LoginPage.login_with_valid_credentials(self, 'csadek@integrant.com', 'ZAQ!cde3')
        AddProductPage.AddProduct(self,'test2')
        self.assertIn('Products management',AddProductPage.get_Page_Name(self))
