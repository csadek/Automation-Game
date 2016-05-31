from ddt import ddt, data, unpack

from POM.Administrator.PromotionCodePage import AddPromotionCodePage
from Tests.BaseTestCase import BaseTestCase
from Utilities.ReadExcel import ReadExcel


@ddt
class AddPromotionCode(BaseTestCase):

    @data(*ReadExcel.get_sheets('../Utilities/Data.xlsx',['LoginValid','Coupon']))
    @unpack
    def test_Add_Promotion(self,username,password,name,start,end,amount):
        self.assertIn('×\nThe coupon code {} has been created.'.format(name.upper()), AddPromotionCodePage.AddCoupon(self, username,password,name, start, end,amount))