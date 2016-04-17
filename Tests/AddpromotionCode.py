from POM.BaseTestCase import BaseTestCase
from POM.LoginLogoutPage import LoginPage
from POM.AddPromotionCodePage import AddPromotionCodePage


class AddPromotionCode(BaseTestCase):

    def test_Add_Promotion(self):
        LoginPage.login_with_valid_credentials(self, 'csadek@integrant.com', 'ZAQ!cde3')
        AddPromotionCodePage.AddCoupon(self,'code1','04-15-2016',200)
        self.assertIn('PROMOTIONAL CODE LIST',AddPromotionCodePage.get_page_name(self))
