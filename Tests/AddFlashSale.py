from POM.BaseTestCase import BaseTestCase
from POM.LoginLogoutPage import LoginPage
from POM.AddFlashSalePage import AddFlashSalePage


class AddProduct(BaseTestCase):

    def test_Add_Product(self):
        LoginPage.login_with_valid_credentials(self, 'csadek@integrant.com', 'ZAQ!cde3')
        AddFlashSalePage.AddFlashSale(self,50,'04-16-2016 01h50:56','04-17-2016 01h39:56')
        self.assertIn('Products management',AddFlashSalePage.get_Page_Name(self))
