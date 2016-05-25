from ddt import ddt, data, unpack

from POM.BaseTestCase import BaseTestCase
from POM.Customer.ProductDetailsPage import ProductDetails
from POM.Customer.SendEmailPage import SendEmailClass
from POM.LoginLogoutPage import LoginLogoutPage
from Utilities.ReadExcel import ReadExcel


@ddt
class sendEmailTestCases(BaseTestCase):

    @data(*ReadExcel.get_data('../Utilities/Data.xlsx','LoginValid'))
    @unpack
    def test_add(self,user,password):
        LoginLogoutPage.login_with_valid_credentials(self, user, password)

    @data(*ReadExcel.get_data('../Utilities/Data.xlsx','SendEmail'))
    @unpack
    def test_send_email_successfully(self,SenderName,SenderEmail,RecName,RecEmails,comment):
        ProductDetails.getProductDetails(self,'trouser')
        ProductDetails.send_email(self)

        conformation_Msg = SendEmailClass.send_Email_successfully(self,SenderName,SenderEmail,RecName,RecEmails,comment)
        self.assertTrue('Your message has been sent.',conformation_Msg)
        SendEmailClass.back_to_product_Page(self)

    def test_send_empty_data(self):
     ProductDetails.send_email(self)
     errorMessage = 'The form content is invalid (unvalid email ou missing data). Please click "back" and fill the forms with correct answers.'
     self.assertTrue(errorMessage ,SendEmailClass.send_Email_empty_data(self))


    def test_Open_Outlook(self):
        SendEmailClass.open_outlook(self,'jmohamed@integrant.com','Gaso3113')










