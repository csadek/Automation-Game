from POM.BaseTestCase import BaseTestCase
from POM.LoginLogoutPage import LoginLogoutPage
from POM.ProductDetailsPage import ProductDetails
from POM.SendEmailPage import sendEmailClass
from Utilities.ReadExcel import ReadExcel
from ddt import ddt, data, unpack

@ddt
class sendEmailTestCases(BaseTestCase):

    @data(*ReadExcel.get_data('../Automation-Game/Automation-Game/Utilities/Data.xlsx','SendEmail'))
    @unpack
    def test_send_mail_successfully(self,SenderName,SenderEmail,RecName,RecEmails,comment):
        LoginLogoutPage.login_with_valid_credentials(self, 'csadek@integrant.com', 'ZAQ!cde3')
        ProductDetails.getProductDetails(self,'trouser')
        ProductDetails.send_email(self)

        conformation_Msg = sendEmailClass.send_Email_successfully(self,SenderName,SenderEmail,RecName,RecEmails,comment)
        self.assertTrue('Your message has been sent.',conformation_Msg)

    def test_mail_empty_data(self):
         LoginLogoutPage.login_with_valid_credentials(self, 'csadek@integrant.com', 'ZAQ!cde3')
         ProductDetails.getProductDetails(self,'trouser')
         ProductDetails.send_email(self)

         errorMessage = 'The form content is invalid (unvalid email ou missing data). Please click "back" and fill the forms with correct answers.'
         self.assertTrue(errorMessage ,sendEmailClass.send_Email_empty_data(self))







