from ddt import ddt, data, unpack
from POM.NewUser.RegestrationPage import RegistrationPage
from Tests.BaseTestCase import BaseTestCase
from Utilities.ReadExcel import ReadExcel
from POM.Administrator.ManageUserPage import ManageUserPage


@ddt
class OpenAccount(BaseTestCase):

    @data(*ReadExcel.get_sheets('../Utilities/Data.xlsx',['LoginValid','Registration']))
    @unpack
    def test_OpenAccount(self,admin,adminpass,email,nickname,password,firstName,surname,company,capacity,dateofbirth,phone,mobile,address,zipcode,town,country,how_do_you_know_our_website, confirm):
        self.assertIn(confirm,RegistrationPage.Register_with_valid_input(self,email,nickname,password,firstName,surname,company,capacity,dateofbirth,phone,mobile,address,zipcode,town,country,how_do_you_know_our_website))
        self.assertTrue(email,RegistrationPage.verify_user_at_DB(self,nickname))
        self.assertIn('has been updated',ManageUserPage.edit_user(self,admin,adminpass,email))


