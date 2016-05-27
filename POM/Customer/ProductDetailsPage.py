from selenium.webdriver.common.by import By
from POM.BaseTestCase import BaseTestCase
from selenium.webdriver.common.action_chains import ActionChains


class ProductDetails(BaseTestCase):
    """ this class represent login page elements manipulations and functions"""
    '''assert on each function
    complete each process
    integrate with SMTP to check the mail'''

    # Locators
    sendEmailLink = (By.PARTIAL_LINK_TEXT,'Send email to your friend')
    addToNotePad = (By.PARTIAL_LINK_TEXT,'Add to notepad')
    printPage = (By.PARTIAL_LINK_TEXT,'Print this page')
    washingTab = (By.PARTIAL_LINK_TEXT,'Washing')
    productInfo = (By.PARTIAL_LINK_TEXT,'Product Info')
    availability= (By.PARTIAL_LINK_TEXT,'Availability')
    zoomTool = (By.CLASS_NAME,'zoomPup')

    #Add to notepad
    MyAccountLink=(By.PARTIAL_LINK_TEXT,'My Account')
    myReminder= (By.PARTIAL_LINK_TEXT,'Check my reminder')

    #Give your opinion Link
    opinionLink= (By.PARTIAL_LINK_TEXT,'Give your opinion')
    yourOpinionText=(By.NAME,'avis')
    sendOpinionBtn=(By.CSS_SELECTOR,'#main_content > div:nth-child(1) > div > div > div.middle_column_repeat > form > table > tbody > tr:nth-child(7) > td > input')
    rate= (By.NAME,'note')
    confirmMsg=(By.CSS_SELECTOR,'#main_content > div:nth-child(1) > div > div > div.middle_column_repeat > div.alert.alert-success.fade.in')

    def getProductDetails(self,ProductName):
        self.driver.find_element_by_partial_link_text(ProductName).click()

    def getDetailsTab(self):
        self.driver.find_element(*ProductDetails.availability).click()
        self.driver.find_element(*ProductDetails.washingTab).click()

    def zoom_product_image(self):
         element=self.driver.find_element(*ProductDetails.zoomTool)
         self.driver.implicitly_wait(30)

    def send_email(self):
        self.driver.find_element(*ProductDetails.sendEmailLink).click()


    def give_your_Opinion_page(self,Opinion):
         self.driver.find_element(*ProductDetails.opinionLink).click()
         self.driver.find_element(*ProductDetails.yourOpinionText).send_keys(Opinion)
         self.driver.find_element(*ProductDetails.rate).click()
         self.driver.find_element(*ProductDetails.sendOpinionBtn).click()

        # return self.driver.find_element(*ProductDetails.confirmMsg).text


    def add_to_notePad_Page(self):
        self.driver.find_element(*ProductDetails.addToNotePad).click()
        self.driver.find_element(*ProductDetails.MyAccountLink).click()
        self.driver.find_element(*ProductDetails.myReminder).click()



    def __init__(self, driver):
        super(ProductDetails, self).__init__(driver)









