from selenium.webdriver.common.by import By
from POM.BaseTestCase import BaseTestCase


class ProductDetails(BaseTestCase):
    """ this class represent login page elements manipulations and functions"""

    # Locators
    sendEmailLink = (By.PARTIAL_LINK_TEXT,'Send email to your friend')
    opinionLink= (By.PARTIAL_LINK_TEXT,'Give your opinion')
    peopleFeedBack = (By.PARTIAL_LINK_TEXT,'All opinion on this product')
    addToNotePad = (By.PARTIAL_LINK_TEXT,'Add to notepad')
    printPage = (By.PARTIAL_LINK_TEXT,'Print this page')
    washingTab = (By.PARTIAL_LINK_TEXT,'Washing')
    productInfo = (By.PARTIAL_LINK_TEXT,'Product Info')
    careTab= (By.PARTIAL_LINK_TEXT,'Care')


    def getProductDetails(self,ProductName):
        self.driver.find_element_by_partial_link_text(ProductName).click()
        #self.driver.find_element(*ProductDetails.productInfo).click()
        #self.driver.find_element(*ProductDetails.careTab).click()
        #self.driver.find_element(*ProductDetails.washingTab).click()

    def __init__(self, driver):
        super(ProductDetails, self).__init__(driver)









