import os
import time
from selenium.webdriver.common.by import By
from Tests.BaseTestCase import BaseTestCase



class ProductDetails(BaseTestCase):
    """ this class represent login page elements manipulations and functions"""
    '''assert on each function
    complete each process
    integrate with SMTP to check the mail'''

    # Locators
    sendEmailLink = (By.PARTIAL_LINK_TEXT,'Send email to your friend')
    addToNotePad = (By.PARTIAL_LINK_TEXT,'Add to notepad')
    productInfo = (By.PARTIAL_LINK_TEXT,'Product Info')
    zoomTool = (By.CLASS_NAME,'zoomPup')

    # Details tabs
    availability= (By.PARTIAL_LINK_TEXT,'Availability')
    washingTab = (By.PARTIAL_LINK_TEXT,'Washing')

    #Add to notepad
    MyAccountLink=(By.PARTIAL_LINK_TEXT,'My Account')
    myReminder= (By.PARTIAL_LINK_TEXT,'Check my reminder')
    table=(By.CLASS_NAME,'table-responsive')
    reminder_name = (By.CSS_SELECTOR,'#main_content > div > div > div > div.middle_column_repeat > div > table > tbody > tr > td.lignecaddie_produit_details > a')

    #Give your opinion Link
    opinionLink= (By.PARTIAL_LINK_TEXT,'Give your opinion')
    yourOpinionText=(By.NAME,'avis')
    sendOpinionBtn=(By.CSS_SELECTOR,'#main_content > div:nth-child(1) > div > div > div.middle_column_repeat > form > table > tbody > tr:nth-child(7) > td > input')
    rate= (By.NAME,'note')
    confirmMsg=(By.CSS_SELECTOR,'#main_content > div:nth-child(1) > div > div > div.middle_column_repeat > div.alert.alert-success.fade.in')

    #Print Page
    printPage = (By.PARTIAL_LINK_TEXT,'Print this page')




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


    def add_to_notePad_Page(self,product_name):
        self.driver.find_element(*ProductDetails.addToNotePad).click()
        self.driver.find_element(*ProductDetails.MyAccountLink).click()
        self.driver.find_element(*ProductDetails.myReminder).click()
        for i in self.driver.find_elements(*ProductDetails.reminder_name):
            if i.text == product_name:
                return True
            else:
                return False

    def print_Product_Details(self):
        self.driver.find_element(*ProductDetails.printPage).click()
        self.driver.get("http://10.1.22.67/Jamaica/achat/produit_details.php?id=1")
        time.sleep(5)
        os.startfile(r"C:\Users\csadek\Desktop\Automation-Game\Automation-Game\Utilities\PrintScript.exe")
        print ("")




    def __init__(self, driver):
        super(ProductDetails, self).__init__(driver)









