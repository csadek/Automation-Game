import unittest
from ddt import ddt, data, unpack
from HelpReferences.basetestcase import BaseTestCase
from HelpReferences.ExcelLib import ReadExcel
#from Pages.HomePage import HomePage
from HelpReferences.LoginPage import LoginPage


@ddt
class TestLogin(BaseTestCase):
    @data(*ReadExcel.get_data('../Utilities/Data.xls','LoginCredentials'))
    @unpack
    def test_login(self, username, password):
        # declare page objects will be used by class
        #Home_Obj = HomePage
        Login_Obj = LoginPage
        username = 'username'
        password = 'password'
        Login_Obj.login_with_valid_credentials(self, username, password)
        #EditAccount_obj = AccountEditPage
        #Home_Obj.open_login(self)
        #self.assertIn("Customer Login", Home_Obj.get_page_title(self))

        '''if Username=='csadek@integrant.com':
            Login_Obj.login_with_valid_credentials(self,Username,Password)
            try:
                self.assertIn(LoginName, EditAccount_obj.get_login_Name(self))
                basetestcase.take_screen_shoot(self)
                EditAccount_obj.logout(self)
            except NoSuchElementException:
                basetestcase.take_screen_shoot(self)
                raise
        else:
            Login_Obj.login_with_Invalid_credentials(self, Username, Password)'''

    def tearDown(self):
        # close the browser window
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()