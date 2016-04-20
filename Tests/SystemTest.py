from Tests.LoginLogout import LoginLogout
from Utilities.ReadExcel import ReadExcel
from ddt import ddt, data, unpack

@ddt
class SystemTest(BaseTestCase):

    @unpack
    @data(*ReadExcel.get_data('../Utilities/Data.xlsx','BillingAddress'))
    def test_system(self,username,password,company,surname,name,email,phone,address,zipcode,town,country,comment):
        LoginLogout.test_login_valid(self,username, password)
        SearchPage.search_valid_Data(self, 'trouser', 'Clothing')
        SearchPage.get_Product_Name(self)
        ProductDetails.getProductDetails(self,'trouser')
       # ProductDetails.zoom_product_image(self)
        #Send Email From Product Details Page
        ProductDetails.send_email(self)
        conformation_Msg = sendEmailClass.send_Email_successfully(self,'Chris','csadek@integrant.com','Jihad','jMohamed@integrant.com','Hello')
        self.assertTrue('Your message has been sent.',conformation_Msg)
        sendEmailClass.back_to_product_Page(self)

        PaymentPages.Pay_Oneproduct(self)
        PaymentPages.Billing_Address(self,company,surname,name,email,phone,address,zipcode,town,country,comment)
        LoginLogoutPage.logout(self)
        LoginLogoutPage.login_with_valid_credentials(self, 'csadek@integrant.com', 'ZAQ!cde3')
        FollowUpOrdersPage.FollowOrder(self)
        FollowUpOrdersPage.get_Status_Name(self)
        self.assertIn('Payment pending', FollowUpOrdersPage.get_Status_Name(self))
        FollowUpOrdersPage.ClickOnStatus(self)
        FollowUpOrdersPage.get_Order_Number(self)
        self.assertIn('12',FollowUpOrdersPage.get_Order_Number(self))