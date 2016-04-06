import unittest
from ddt import ddt, data, unpack
from Utilities import Regestration_DataFromExcelsheet
from POM import LoginPage_Mahran
from HelpReferences.basetestcase import BaseTestCase


class Login_T(BaseTestCase):

    def test_login_incorrect_email(self):
       Login_Obj = LoginPage_Mahran
       Login_Obj.LoginPage.login_with_Invalid_credentials(self, '123@gmail.com','invpass')

    def test_login_blank_password(self):
       Login_Obj = LoginPage_Mahran
       Login_Obj.LoginPage.login_with_Invalid_credentials2(self,'test@email.com', '')

    def test_login_blank_email(self):
       Login_Obj = LoginPage_Mahran
       Login_Obj.LoginPage.login_with_Invalid_credentials(self,'', 'password')

    def test_login(self):
        Login_Obj = LoginPage_Mahran
        Login_Obj.LoginPage.login_with_valid_credentials(self,'eng.mohammadrihan@gmail.com','h0tr1ngG')

