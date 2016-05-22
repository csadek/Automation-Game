from selenium.webdriver.common.by import By
from POM.BaseTestCase import BaseTestCase


class ProductDetails(BaseTestCase):
    """ this class represent login page elements manipulations and functions"""
    '''assert on each function
    complete each process
    integrate with SMTP to check the mail'''

    # Locators
    sendEmailLink = (By.PARTIAL_LINK_TEXT,'Send email to your friend')
    opinionLink= (By.PARTIAL_LINK_TEXT,'Give your opinion')
    peopleFeedBack = (By.PARTIAL_LINK_TEXT,'All opinion on this product')
    addToNotePad = (By.PARTIAL_LINK_TEXT,'Add to notepad')
    printPage = (By.PARTIAL_LINK_TEXT,'Print this page')
    washingTab = (By.PARTIAL_LINK_TEXT,'Washing')
    productInfo = (By.PARTIAL_LINK_TEXT,'Product Info')
    availability= (By.PARTIAL_LINK_TEXT,'Availability')
    zoomTool = (By.CSS_SELECTOR,'#zoom1 > div > div.zoomWindow')

    def getProductDetails(self,ProductName):
        self.driver.find_element_by_partial_link_text(ProductName).click()
        self.driver.find_element(*ProductDetails.availability).click()
        self.driver.find_element(*ProductDetails.washingTab).click()

    def zoom_product_image(self):
         self.driver.find_element(*ProductDetails.zoomTool).click()

    def send_email(self):
        self.driver.find_element(*ProductDetails.sendEmailLink).click()

    def give_your_Opinion_page(self):
         self.driver.find_element(*ProductDetails.opinionLink).click()

    def people_feedback_Page(self):
        self.driver.find_element(*ProductDetails.peopleFeedBack).click()

    def add_to_notePad_Page(self):
        self.driver.find_element(*ProductDetails.addToNotePad).click()

    def print_Page(self):
        self.driver.find_element(*ProductDetails.printPage).click()

    def __init__(self, driver):
        super(ProductDetails, self).__init__(driver)









