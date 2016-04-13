from POM.RegestrationPage import RegistrationPage
from POM.BaseTestCase import BaseTestCase


class OpenAccount(BaseTestCase):

    def test_OpenAccount(self):
        self.driver.get('http://10.1.22.67/Jamaica/utilisateurs/enregistrement.php')
        RegistrationPage.Register_with_valid_input(self,'mr@gmaddil.com','Rcc','Mmmm5678009','Mohammad','Rihan','Integrant','Employee','04-04-1998','0122','01223','566St','11411','Town','France','other')

        RegistrationPage.get_Thanks_Msg(self)
        self.assertIn('Thanks for your confidence.',RegistrationPage.get_Thanks_Msg(self))