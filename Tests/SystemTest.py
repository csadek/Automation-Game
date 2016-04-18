from POM.BaseTestCase import BaseTestCase
from POM.LoginLogoutPage import LoginLogoutPage
from POM.searchPage import SearchPage
from POM.PaymentPages import PaymentPages
from POM.ProductDetailsPage import ProductDetails
from POM.FollowUpOrderPage import FollowUpOrdersPage


class SystemTest(BaseTestCase):

    def test_search_Exist_products(self):
        LoginLogoutPage.login_with_valid_credentials(self,"csadek","ZAQ!cde3")
        SearchPage.search_valid_Data(self, 'trouser', 'Clothing')
        SearchPage.get_Product_Name(self)
        ProductDetails.getProductDetails(self,'trouser')
        PaymentPages.Pay_Oneproduct(self)
        PaymentPages.Billing_Address(self,'Integrant','Rihan','Mohammad','eng.mohammadriihan@gmail.com','012','566st','11411'
                                ,'FR','France','Thank you')
        LoginLogoutPage.logout(self)
        LoginLogoutPage.login_with_valid_credentials(self, 'csadek@integrant.com', 'ZAQ!cde3')
        FollowUpOrdersPage.FollowOrder(self)
        FollowUpOrdersPage.get_Status_Name(self)
        self.assertIn('Payment pending', FollowUpOrdersPage.get_Status_Name(self))
        FollowUpOrdersPage.ClickOnStatus(self)
        FollowUpOrdersPage.get_Order_Number(self)
        self.assertIn('12',FollowUpOrdersPage.get_Order_Number(self))

        #Follow
        #Logout













