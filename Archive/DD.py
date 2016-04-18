import unittest
from ddt import ddt, data, unpack
from POM.BaseTestCase import BaseTestCase
from POM.RegestrationPage import RegistrationPage
from Utilities.ReadExcel import ReadExcel



@ddt
class RegistrationPage(BaseTestCase):
    """ this class represent Registration elements manipulations and functions"""

@data(*ReadExcel.get_data('../Utilities/Data.xls','Registration'))
@unpack
def Valid_Register(self, email, nickname, password, firstname, surname, company, capacity, dateofbirth, phone, mobile,address, zipcode, town
                                  , country, how_do_you_know_our_website):
        Rpage=RegistrationPage
        Rpage.Register_with_valid_input(self, email, nickname, password, firstname, surname, company, capacity, dateofbirth, phone, mobile,address, zipcode, town
                                  , country, how_do_you_know_our_website)



if __name__ == '__main__':
    unittest.main()