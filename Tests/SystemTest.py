from POM.BaseTestCase import BaseTestCase
from POM.LoginPage import LoginPage
from POM.searchPage import SearchPage
from POM.Payment import Payment1


class Test_SystemTest1(BaseTestCase):

    def test_search_Exist_products(self):
        LoginPage.Open_Login_Page(self)
        LoginPage.login_with_valid_credentials(self,"csadek","ZAQ!cde3")
        SearchPage.search_vaild_Data(self,'trouser','Clothing')
        SearchPage.get_Product_Name(self)
        Payment1.Pay_Oneproduct(self)
        Payment1.Billing_Address(self,'Integrant','Rihan','Mohammad','eng.mohammadriihan@gmail.com','012','566st','11411'
                                ,'FR','France','Thank you')






