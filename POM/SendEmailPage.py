from selenium.webdriver.common.by import By
from POM.BaseTestCase import BaseTestCase


class sendEmail(BaseTestCase):
    firstName = (By.NAME,'yname')
    yourEmail = (By.NAME,'yemail')
    recipientNames = (By.NAME,'fname[]')
    recipientEmails = (By.NAME,'femail[]')
    comments = (By.NAME,'comments')
    sendButton= (By.NAME,'action')
    confirmationMsg= (By.CLASS_NAME,'alert alert-success')

    def send_Email(self,name,email,RecName,RecEmails ,comment):
        self.driver.find_element(*sendEmail.firstName).send_keys(name)
        self.driver.find_element(*sendEmail.yourEmail).send_keys(email)
        self.driver.find_element(*sendEmail.recipientNames).send_keys(RecName)
        self.driver.find_element(*sendEmail.recipientEmails).send_keys(RecEmails)
        self.driver.find_element(*sendEmail.comments).send_keys(comment)

        self.driver.find_element(*sendEmail.sendButton).click()

    def get_conformation_Message(self):
        return self.driver.find_element_by(*sendEmail.confirmationMsg).text


