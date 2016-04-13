from POM.BaseTestCase import BaseTestCase
from POM.LoginPage import LoginPage
from POM.AddProductPage import AddProductPage


class AddProduct(BaseTestCase):

    def Test_Add_Product(self):
        LoginPage.login_with_valid_credentials(self, 'csadek@integrant.com', 'ZAQ!cde3')
        AddProductPage.AddProduct(self)
