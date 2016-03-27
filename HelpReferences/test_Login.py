import unittest

from ddt import ddt, data, unpack
from selenium.common.exceptions import NoSuchElementException
from baseclasses.basetestcase import basetestcase
from DataSourceFiles.ExcelLib import ReadExcel
from Pages.AccountEditPage import AccountEditPage
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage


@ddt
class test_login(basetestcase):
    @data(*ReadExcel.get_data( '../TestData/Data.xls','LoginCredentials'))
    @unpack
    def test_login(self,Username,Password,LoginName):
        # declare page objects will be used by class
        Home_Obj = HomePage
        Login_Obj = LoginPage
        EditAccount_obj = AccountEditPage
        Home_Obj.open_login(self)
        self.assertIn("Customer Login", Home_Obj.get_page_title(self))

        if Username=='aabdelfattah@integrant.com':
            Login_Obj.login_with_valid_credentials(self,Username,Password)
            try:
                self.assertIn(LoginName, EditAccount_obj.get_login_Name(self))
                basetestcase.take_screen_shoot(self)
                EditAccount_obj.logout(self)
            except NoSuchElementException:
                basetestcase.take_screen_shoot(self)
                raise
        else:
            Login_Obj.login_with_Invalid_credentials(self, Username, Password)
    def tearDown(self):
        # close the browser window
        self.driver.quit()
if __name__=='__main__':
    unittest.main()
