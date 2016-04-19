from selenium.webdriver.common.by import By
from POM.BaseTestCase import BaseTestCase


class sendEmailClass(BaseTestCase):
    firstName = (By.NAME,'yname')
    yourEmail = (By.NAME,'yemail')
    recipientNames = (By.NAME,'fname[]')
    recipientEmails = (By.NAME,'femail[]')
    comments = (By.NAME,'comments')
    sendButton= (By.NAME,'action')
    backToProduct = (By.PARTIAL_LINK_TEXT,'Go back to the referer.')
    errorMsg= (By.CSS_SELECTOR,'#main_content > div:nth-child(1) > div > div > div.middle_column_repeat > div')
    confirmationMsg=(By.CSS_SELECTOR,'#main_content > div:nth-child(1) > div > div > div.middle_column_repeat > div')

    def send_Email_successfully(self,name,senderEmail,RecName,RecEmails ,comment):
        self.driver.find_element(*sendEmailClass.firstName).send_keys(name)
        self.driver.find_element(*sendEmailClass.yourEmail).clear()
        self.driver.find_element(*sendEmailClass.yourEmail).send_keys(senderEmail)
        self.driver.find_element(*sendEmailClass.recipientNames).send_keys(RecName)
        self.driver.find_element(*sendEmailClass.recipientEmails).send_keys(RecEmails)
        self.driver.find_element(*sendEmailClass.comments).send_keys(comment)
        self.driver.find_element(*sendEmailClass.sendButton).click()

        return self.driver.find_element(*sendEmailClass.confirmationMsg).text

    def send_Email_empty_data(self):
        self.driver.find_element(*sendEmailClass.sendButton).click()

        return self.driver.find_element(*sendEmailClass.errorMsg).text


    def back_to_product_Page(self):
        self.driver.find_element(*sendEmailClass.backToProduct).click()

