from POM.BaseTestCase import BaseTestCase
from POM.LoginLogoutPage import LoginLogoutPage
from POM.ManageBillingAddressPage import ManageBillingAddressPage

class MangeBilling(BaseTestCase):
    def test_Change(self):
        LoginLogoutPage.login_with_valid_credentials(self, 'csadek@integrant.com', 'ZAQ!cde3')
        ManageBillingAddressPage.manage_billing(self)
        ManageBillingAddressPage.Create_Another_Address(self,'Mmmm5678009','Billing Address','Mohammad','Rihan','mr@gmaddil.com','integrant','566St','11411','Town','Egypt','01223')


