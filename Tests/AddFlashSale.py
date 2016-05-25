from ddt import ddt, data, unpack
from POM.Administrator.FlashSalePage import AddFlashSalePage
from POM.BaseTestCase import BaseTestCase
from POM.LoginLogoutPage import LoginLogoutPage
from Utilities.ReadExcel import ReadExcel


@ddt
class AddFlashSale(BaseTestCase):

    @data(*ReadExcel.get_data('../Utilities/Data.xlsx','LoginValid'))
    @unpack
    def test_Add(self,user,password):
        LoginLogoutPage.login_with_valid_credentials(self, user, password)

    @data(*ReadExcel.get_data('../Utilities/Data.xlsx','flash'))
    @unpack
    def test_Add_flash_sale(self,amount,start,end,product_name):
        self.assertIn('×\nChanges to product {} have been taken into account.'.format(product_name),AddFlashSalePage.add_flash_sale_to_product(self,amount,start,end,product_name))
        self.assertEqual(amount,AddFlashSalePage.verify_flash_sale_price(self, product_name))
        self.assertTrue(True, AddFlashSalePage.verify_remaining_time_to_end_sale(self, end))
