from POM.BaseTestCase import BaseTestCase
from POM.LoginLogoutPage import LoginLogoutPage
from Utilities.ReadExcel import ReadExcel
from ddt import ddt, data, unpack

@ddt
class LoginLogout(BaseTestCase):

    @data(*ReadExcel.get_data('../Utilities/Data.xlsx','LoginInvalid'))
    @unpack
    def test_login_incorrect(self,one,two):
        self.assertTrue('Bad email or password.',LoginLogoutPage.login_with_Invalid_credentials(self, one,two))

    @data(*ReadExcel.get_data('../Utilities/Data.xlsx','LoginBlankPW'))
    @unpack
    def test_login_blank_password(self,one,two):
        self.assertTrue('Please type in your password.',LoginLogoutPage.login_with_Invalid_credentials2(self,one,two))

    @data(*ReadExcel.get_data('../Utilities/Data.xlsx','LoginBlankUN'))
    @unpack
    def test_login_blank_email(self,one,two):
        self.assertTrue('Bad email or password.',LoginLogoutPage.login_with_Invalid_credentials(self,one,two))

    @data(*ReadExcel.get_data('../Utilities/Data.xlsx','LoginValid'))
    @unpack
    def test_login_valid(self,one,two):
        self.driver.get('http://10.1.22.67/Jamaica/utilisateurs/enregistrement.php')
        LoginLogoutPage.login_with_valid_credentials(self,one,two)

    def test_logout(self):
        LoginLogoutPage.logout(self)
