from POM.BaseTestCase import BaseTestCase
from POM.LoginLogoutPage import LoginPage
from POM import SearchPage
from POM.PaymentPages import PaymentPages


class SystemTest(BaseTestCase):

    def test_search_Exist_products(self):
        LoginPage.Open_Login_Page(self)
        LoginPage.login_with_valid_credentials(self,"csadek","ZAQ!cde3")
        SearchPage.SearchPage.search_valid_Data(self, 'trouser', 'Clothing')
        #SearchPage.get_Product_Name(self)
        PaymentPages.Pay_Oneproduct(self)
        PaymentPages.Billing_Address(self,'Integrant','Rihan','Mohammad','eng.mohammadriihan@gmail.com','012','566st','11411'
                                ,'FR','France','Thank you')
        #Follow
        #Logout






