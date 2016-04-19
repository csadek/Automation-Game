from POM.BaseTestCase import BaseTestCase
from POM.SendEmailPage import sendEmail



class sendEmailTestCases(BaseTestCase):

    def test_mail_incorrect(self):
        self.assertTrue('The form content is invalid (unvalid email ou missing data). Please click "back" and fill the forms with correct answers.'
                        ,sendEmail.send_Email_missing_data(self,'csadek@integrant.com','ali','jmohamed@integrant.com'))


    def test_send_mail(self):
        conformation_Msg = sendEmail.send_Email_successfully(self,'Chris','Jihad','jMohamed@integrant.com','Hello')
        self.assertTrue('Your message has been sent.',conformation_Msg)


