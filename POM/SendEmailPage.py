from selenium.webdriver.common.by import By
from POM.BaseTestCase import BaseTestCase


class SendEmailClass(BaseTestCase):
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
        self.driver.find_element(*SendEmailClass.firstName).send_keys(name)
        self.driver.find_element(*SendEmailClass.yourEmail).clear()
        self.driver.find_element(*SendEmailClass.yourEmail).send_keys(senderEmail)
        self.driver.find_element(*SendEmailClass.recipientNames).send_keys(RecName)
        self.driver.find_element(*SendEmailClass.recipientEmails).send_keys(RecEmails)
        self.driver.find_element(*SendEmailClass.comments).send_keys(comment)
        self.driver.find_element(*SendEmailClass.sendButton).click()

        return self.driver.find_element(*SendEmailClass.confirmationMsg).text

    def send_Email_empty_data(self):
        self.driver.find_element(*SendEmailClass.sendButton).click()

        return self.driver.find_element(*SendEmailClass.errorMsg).text

    def back_to_product_Page(self):
        self.driver.find_element(*SendEmailClass.backToProduct).click()

