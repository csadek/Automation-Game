from POM.BaseTestCase import BaseTestCase
from POM.RegestrationPage import RegistrationPage
from Utilities.ReadExcel import ReadExcel
from ddt import ddt, data, unpack

@ddt
class OpenAccount(BaseTestCase):

    @data(*ReadExcel.get_data('../Utilities/Data.xlsx','Registration'))
    @unpack
    def test_OpenAccount(self,one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen):
        self.driver.get('http://10.1.22.67/Jamaica/utilisateurs/enregistrement.php')
        RegistrationPage.Register_with_valid_input(self,one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen)

        RegistrationPage.get_Thanks_Msg(self)
        self.assertIn('Thanks for your confidence.',RegistrationPage.get_Thanks_Msg(self))