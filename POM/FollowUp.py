from selenium.webdriver.common.by import By
from POM.BaseTestCase import BaseTestCase


class FollowUp_Orders(BaseTestCase):
    """ this class represent FollowUp_Orders page elements manipulations and functions"""

    # Locators
    FollowUp_Orders_Lnk = (By.CSS_SELECTOR, 'div.middle_column_repeat > div > div:nth-child(7) > div:nth-child(1) > a')
    FollowUp_Orders_Title = (By.CSS_SELECTOR, '#main_content > div:nth-child(1) > div > div > div.middle_column_repeat > h1')
    PaymentStatus_Lnk = (By.CSS_SELECTOR, 'tr:nth-child(1) > td:nth-child(4) > a')
    OrderDetails_Hdr = (By.CSS_SELECTOR, '#main_content > div:nth-child(1) > div > div > div.middle_column_repeat > h2')

    def FollowOrder(self):
        self.driver.find_element(*FollowUp_Orders.FollowUp_Orders_Lnk).click()
        #text = self.driver.find_element(*FollowUp_Orders.FollowUp_Orders_Lnk).text
        #self.assertEqual(self,text,'Payment pending')

        self.driver.find_element(*FollowUp_Orders.PaymentStatus_Lnk).click()








