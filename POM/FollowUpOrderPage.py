from selenium.webdriver.common.by import By
from POM.BaseTestCase import BaseTestCase
from selenium import webdriver


class FollowUpOrdersPage(BaseTestCase):
    """ this class represent FollowUp_Orders page elements manipulations and functions"""

    # Locators
    FollowUp_Orders_Lnk = (By.CSS_SELECTOR, 'div.middle_column_repeat > div > div:nth-child(7) > div:nth-child(1) > a')
    FollowUp_Orders_Title = (By.CSS_SELECTOR, '#main_content > div:nth-child(1) > div > div > div.middle_column_repeat > h1')
    PaymentStatus_Lnk = (By.CSS_SELECTOR, 'tr:nth-child(1) > td:nth-child(4) > a')
    OrderDetails_Hdr = (By.CSS_SELECTOR, '#main_content > div:nth-child(1) > div > div > div.middle_column_repeat > h2')
    OrderNumber = (By.CSS_SELECTOR, 'div.middle_column_repeat > div > table > tbody > tr:nth-child(1) > td:nth-child(2)')

    def FollowOrder(self):
        self.driver.find_element(*FollowUpOrdersPage.FollowUp_Orders_Lnk).click()
        #text = self.driver.find_element(*FollowUp_Orders.FollowUp_Orders_Lnk).text
        #self.assertEqual(self,text,'Payment pending')
    def get_Status_Name(self):
        self.driver.implicitly_wait(10)
        PaymentStatus_Lnk_LBL = (By.CSS_SELECTOR, 'tr:nth-child(1) > td:nth-child(4) > a')
        return self.driver.find_element(*FollowUpOrdersPage.PaymentStatus_Lnk).text

    def ClickOnStatus(self):
        self.driver.find_element(*FollowUpOrdersPage.PaymentStatus_Lnk).click()

    def get_Order_Number(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*FollowUpOrdersPage.OrderNumber).text







