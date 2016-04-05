import unittest
from Utilities import BasePage_Mahran
from POM import RegestrationPage_Elements
from HelpReferences.basetestcase import BaseTestCase

class OpenAccount_T(BaseTestCase):
    def test_OpenAccount(self):
        OpenAcc_Obj = RegestrationPage_Elements
        OpenAcc_Obj.RegistrationPageObject.Register_with_valid_input(self, 'mr@gmail.com','R','Mmmm$$5678009','Moh','Ri','Integrant','0122','01223','11411','France','other',OpenAcc_Obj.RegistrationPageObject.select_Howdoyouknowourwebsite,OpenAcc_Obj.RegistrationPageObject.FirstSelection,OpenAcc_Obj.RegistrationPageObject.SecondSelection,OpenAcc_Obj.RegistrationPageObject.OpenAccount)