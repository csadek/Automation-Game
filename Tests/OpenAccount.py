from ddt import ddt, data, unpack

from POM.NewUser.RegestrationPage import RegistrationPage
from Tests.BaseTestCase import BaseTestCase
from Utilities.ReadExcel import ReadExcel


@ddt
class OpenAccount(BaseTestCase):

    @data(*ReadExcel.get_data('../Utilities/Data.xlsx','Registration'))
    @unpack
    def test_OpenAccount(self,email,nickname,password,firstName,surname,company,capacity,dateofbirth,phone,mobile,address,zipcode,town,country,how_do_you_know_our_website, confirm):
        self.driver.get('http://10.1.22.67/Jamaica/utilisateurs/enregistrement.php')
        self.assertIn(confirm,RegistrationPage.Register_with_valid_input(self,email,nickname,password,firstName,surname,company,capacity,dateofbirth,phone,mobile,address,zipcode,town,country,how_do_you_know_our_website))


