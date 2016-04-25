from POM.BaseTestCase import BaseTestCase
from POM.LoginLogoutPage import LoginLogoutPage
from Utilities.ReadExcel import ReadExcel
from ddt import ddt, data, unpack

@ddt
class LoginLogout(BaseTestCase):

    @unpack
    @data(*ReadExcel.get_data('../Utilities/Data.xlsx','LoginInvalid'))
    def test_login_invalid(self,username,password,error):
        self.assertTrue(error,LoginLogoutPage.login_with_Invalid_credentials(self, username,password))

    @unpack
    @data(*ReadExcel.get_data('../Utilities/Data.xlsx','LoginValid'))
    def test_login_valid(self,username,password):
        self.assertEqual(username,LoginLogoutPage.login_with_valid_credentials(self,username,password))

    def test_logout(self):
        LoginLogoutPage.logout(self)