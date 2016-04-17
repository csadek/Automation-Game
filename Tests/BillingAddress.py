from POM.BaseTestCase import BaseTestCase
from POM.LoginPage import LoginPage
from POM.ManageBillingAddressPage import ManageBillingAddressPage

class MangeAddress(BaseTestCase):

    def test_Change(self):
        LoginPage.login_with_valid_credentials(self,"csadek","ZAQ!cde3")
        ManageBillingAddressPage.manage_billing(self)
        ManageBillingAddressPage.Create_Another_Address(self,'Mmmm5678009','Billing Address','Mohammad','Rihan','mr@gmaddil.com','integrant','566St','11411','Town','France','01223')


