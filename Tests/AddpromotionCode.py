from ddt import ddt, data, unpack

from POM.Administrator.AddPromotionCodePage import AddPromotionCodePage
from POM.BaseTestCase import BaseTestCase
from POM.LoginLogoutPage import LoginLogoutPage
from Utilities.ReadExcel import ReadExcel


@ddt
class AddPromotionCode(BaseTestCase):

    @data(*ReadExcel.get_data('../Utilities/Data.xlsx','LoginValid'))
    @unpack
    def test_Add(self,user,password):
        LoginLogoutPage.login_with_valid_credentials(self,user, password)

    @data(*ReadExcel.get_data('../Utilities/Data.xlsx','Coupon'))
    @unpack
    def test_Add_Promotion(self,name,start,amount):
        AddPromotionCodePage.AddCoupon(self,name,start,amount)
        self.assertIn('PROMOTIONAL CODE LIST',AddPromotionCodePage.get_page_name(self))
