from selenium.webdriver.common.by import By
from POM.BaseTestCase import BaseTestCase
from POM.CreateBillingAddressPage import CreateBillingAddress


class ManageBillingAddressPage(BaseTestCase):

    PageTitle = (By.CLASS_NAME,'page_title')
    BillingAddressLink = (By.PARTIAL_LINK_TEXT,'Manage my billing and shipping addresses')
    BillingAddressList = (By.ID , 'address_default')
    ShippingAddress = (By.NAME,'personal_address_ship')
    CreatAddressBtn = (By.PARTIAL_LINK_TEXT ,'Create another address')

    def manage_billing(self):
        self.driver.find_element(*ManageBillingAddressPage.BillingAddressLink).click()


    def Create_Another_Address(self,surAddress,surName,firstName,email,company,address,zipCode,town,country,phone):
        self.driver.find_element(*ManageBillingAddressPage.CreatAddressBtn).click()
        CreateBillingAddress.new_address_vaild_input(self,surAddress,surName,firstName,email,company,address,zipCode,town,country,phone)

    def __init__(self, driver):
        super(ManageBillingAddressPage, self).__init__(driver)




