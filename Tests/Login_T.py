import unittest
from Utilities import BasePage_Mahran
from POM import LoginPage_Mahran
from HelpReferences.basetestcase import BaseTestCase

class Login_T(BaseTestCase):
    def test_login(self):
        Login_Obj = LoginPage_Mahran
        Login_Obj.LoginPage.login_with_valid_credentials(self,'eng.mohammadrihan@gmail.com','h0tr1ngG')

        if __name__ == '__main__':
            unittest.main()
