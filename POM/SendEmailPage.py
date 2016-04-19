from selenium.webdriver.common.by import By
from POM.BaseTestCase import BaseTestCase


class sendEmail(BaseTestCase):
    firstName = (By.NAME,'yname')
    yourEmail = (By.NAME,'yemail')
    recipientNames = (By.NAME,'fname[]')
    recipientEmails = (By.NAME,'femail[]')
    comments = (By.NAME,'comments')
    sendButton= (By.NAME,'action')
    errorMsg= (By.CSS_SELECTOR,'#main_content > div:nth-child(1) > div > div > div.middle_column_repeat > div')
    confirmationMsg=(By.CSS_SELECTOR,'#main_content > div:nth-child(1) > div > div > div.middle_column_repeat > div')

    def send_Email_successfully(self,name,RecName,RecEmails ,comment):
        self.driver.find_element(*sendEmail.firstName).send_keys(name)
        self.driver.find_element(*sendEmail.recipientNames).send_keys(RecName)
        self.driver.find_element(*sendEmail.recipientEmails).send_keys(RecEmails)
        self.driver.find_element(*sendEmail.comments).send_keys(comment)
        self.driver.find_element(*sendEmail.sendButton).click()

        return self.driver.find_element(*sendEmail.confirmationMsg).text

    def send_Email_missing_data(self,RecName,RecEmails):
        self.driver.find_element(*sendEmail.recipientNames).send_keys(RecName)
        self.driver.find_element(*sendEmail.recipientEmails).send_keys(RecEmails)
        self.driver.find_element(*sendEmail.sendButton).click()

    def get_Error_mesage(self):
        return self.driver.find_element(*sendEmail.errorMsg).text

