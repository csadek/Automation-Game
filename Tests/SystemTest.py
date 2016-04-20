from Tests.LoginLogout import LoginLogout
from Tests.OpenAccount import OpenAccount
from Tests.ManageUser import ManageUser
from Tests.Search import Search
from Tests.Payment import Payment
from Tests.FollowUpOrder import FollowUpOrder
from POM.BaseTestCase import BaseTestCase
from Utilities.ReadExcel import ReadExcel
from ddt import ddt, data, unpack

@ddt
class SystemTest(BaseTestCase):

    @unpack
    @data(*ReadExcel.get_data('../Utilities/Data.xlsx','Registration'))
    @data(*ReadExcel.get_data('../Utilities/Data.xlsx','LoginValid'))
    @data(*ReadExcel.get_data('../Utilities/Data.xlsx','Products'))
    def test_system(self,email,nickname,password,firstName,surname,company,capacity,dateofbirth,phone,mobile,address,zipcode,town,country,how,confirm,username, userpassword,product,category):
        OpenAccount.test_OpenAccount(self,email,nickname,password,firstName,surname,company,capacity,dateofbirth,phone,mobile,address,zipcode,town,country,how,confirm)
        LoginLogout.test_logout(self)
        ManageUser.test_Add(self,username, userpassword)
        ManageUser.test_edit(self)
        LoginLogout.test_logout(self)
        LoginLogout.test_login_valid(email,password)
        Search.test_search_Exist_products(self, product,category)
        '''ProductDetails.getProductDetails(self,'trouser')
        ProductDetails.zoom_product_image(self)
        Send Email From Product Details Page
        ProductDetails.send_email(self)
        conformation_Msg = sendEmailClass.send_Email_successfully(self,'Chris','csadek@integrant.com','Jihad','jMohamed@integrant.com','Hello')
        self.assertTrue('Your message has been sent.',conformation_Msg)
        sendEmailClass.back_to_product_Page(self)'''
        Payment.Pay_Oneproduct(self)
        Payment.test_payment(self)
        FollowUpOrder.test_FollowOrder_valid(self,email,password)