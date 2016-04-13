from POM.RegestrationPage import RegistrationPageObject
from POM.BaseTestCase import BaseTestCase


class OpenAccount(BaseTestCase):

    def test_OpenAccount(self):
        self.driver.get('http://10.1.22.67/Jamaica/utilisateurs/enregistrement.php')
        RegistrationPageObject.Register_with_valid_input(self,'mr@gmail.com','R','Mmmm$$5678009','Mohammad','Rihan','Integrant','Employee','04-04-1998','0122','01223','566St','11411','Town','France','other')

        RegistrationPageObject.get_Thanks_Msg(self)
        self.assertIn('Thanks for your confidence.',RegistrationPageObject.get_Thanks_Msg(self))