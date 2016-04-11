from POM.Payment import Payment1
from HelpReferences.basetestcase import BaseTestCase
from POM.LoginPage import LoginPage
from selenium.webdriver.common.by import By


class TestPayment(BaseTestCase):

    def test_login_valid(self):
        LoginPage.login_with_valid_credentials(self, 'csadek@integrant.com', 'ZAQ!cde3')
        self.driver.find_element(By.CSS_SELECTOR, '#search_category').send_keys('Clothing')
        self.driver.find_element(By.CSS_SELECTOR, 'span.input-group-btn > input').click()
        Payment1.Pay_Oneproduct(self)
        Payment1.Billing_Address(self,'Integrant','Rihan','Mohammad','eng.mohammadriihan@gmail.com','012','566st','11411'
                                ,'FR','France','Thank you')

        Screenshot = self.driver.get_screenshot_as_file('screenshot_PayConfirm.jpg')

    '''def Test_Oneproduct(self):
        Payment1.Pay_Oneproduct(self,'France','Pickup in store','Integrant','Rihan','Mohammad','eng.mohammadriihan@gmail.com','012','566st','11411'
                                ,'FR','France','Thank you')'''
