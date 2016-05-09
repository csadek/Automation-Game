from POM.FollowUpOrderPage import FollowUpOrdersPage
from POM.AddFlashSalePage import AddFlashSalePage
from POM.ProductsModule import AddProductPage
from POM.AddPromotionCodePage import AddPromotionCodePage
from POM.CategoryPage import CategoryPage
from POM.LoginLogoutPage import LoginLogoutPage
from POM.searchPage import SearchPage
from POM.RegestrationPage import RegistrationPage
from POM.PaymentPages import PaymentPages
from POM.ProductDetailsPage import ProductDetails
from POM.ManageUserPage import ManageUserPage
from POM.BaseTestCase import BaseTestCase
from Utilities.ReadExcel import ReadExcel
from ddt import ddt, data, unpack


@ddt
class SystemTest(BaseTestCase):

    @unpack
    @data(*ReadExcel.get_data('../Utilities/Data.xlsx','Registration'))
    @data(*ReadExcel.get_data('../Utilities/Data.xlsx','LoginValid'))
    @data(*ReadExcel.get_data('../Utilities/Data.xlsx','Products'))
    @data(*ReadExcel.get_data('../Utilities/Data.xlsx','BillingAddress'))
    def test_system(self,email,nickname,password,firstName,surname,company,capacity,dateofbirth,phone,mobile,address,zipcode,town,country,how,confirmm,username, userpassword,product,category,last,first,mail,number,shipaddress,zipcod,city,pay,comment):
        self.assertIn(confirmm,RegistrationPage.Register_with_valid_input(self,email,nickname,password,firstName,surname,company,capacity,dateofbirth,phone,mobile,address,zipcode,town,country,how))
        LoginLogoutPage.logout(self)
        self.assertEqual(username,LoginLogoutPage.login_with_valid_credentials(self,username,userpassword))
        ManageUserPage.admin_view(self)
        ManageUserPage.edit_user(self)
        LoginLogoutPage.logout(self)
        self.assertEqual(username,LoginLogoutPage.login_with_valid_credentials(self,email,password))
        SearchPage.search_valid_Data(self, product,category)
        '''ProductDetails.getProductDetails(self,'trouser')
        ProductDetails.zoom_product_image(self)
        Send Email From Product Details Page
        ProductDetails.send_email(self)
        conformation_Msg = sendEmailClass.send_Email_successfully(self,'Chris','csadek@integrant.com','Jihad','jMohamed@integrant.com','Hello')
        self.assertTrue('Your message has been sent.',conformation_Msg)
        sendEmailClass.back_to_product_Page(self)'''
        PaymentPages.Pay_Oneproduct(self)
        PaymentPages.Billing_Address(self,last,first,mail,number,shipaddress,zipcod,city,pay,comment)
        #FollowUpOrder.test_FollowOrder_valid(self,email,password)