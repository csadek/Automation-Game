from POM.BaseTestCase import BaseTestCase
from POM.LoginLogoutPage import LoginLogoutPage
from POM.searchPage import SearchPage
from POM.PaymentPages import PaymentPages
from POM.ProductDetailsPage import ProductDetails
from POM.FollowUpOrderPage import FollowUpOrdersPage
from Utilities.ReadExcel import ReadExcel
from ddt import ddt, data, unpack

@ddt
class SystemTest(BaseTestCase):
    @data(*ReadExcel.get_data('../Utilities/Data.xlsx','BillingAddress'))
    @unpack
    def test_system(self,company,surname,name,email,phone,address,zipcode,town,country,comment):
        LoginLogoutPage.login_with_valid_credentials(self,"csadek","ZAQ!cde3")
        SearchPage.search_valid_Data(self, 'trouser', 'Clothing')
        SearchPage.get_Product_Name(self)
        #ProductDetails.getProductDetails(self,'trouser')
        PaymentPages.Pay_Oneproduct(self)
        PaymentPages.Billing_Address(self,company,surname,name,email,phone,address,zipcode,town,country,comment)
        LoginLogoutPage.logout(self)
        LoginLogoutPage.login_with_valid_credentials(self, 'csadek@integrant.com', 'ZAQ!cde3')
        FollowUpOrdersPage.FollowOrder(self)
        FollowUpOrdersPage.get_Status_Name(self)
        self.assertIn('Payment pending', FollowUpOrdersPage.get_Status_Name(self))
        FollowUpOrdersPage.ClickOnStatus(self)
        FollowUpOrdersPage.get_Order_Number(self)
        self.assertIn('12',FollowUpOrdersPage.get_Order_Number(self))













