from POM.RegestrationPage import RegistrationPageObject
from HelpReferences.basetestcase import BaseTestCase


class OpenAccount(BaseTestCase):

    def test_OpenAccount(self):
        RegistrationPageObject.Register_with_valid_input(self,'mr@gmail.com','R','Mmmm$$5678009','Mohammad','Rihan','Integrant','Employee','04-04-1998','0122','01223','566St','11411','Town','France','other')