from ddt import ddt, data, unpack
from POM.BaseTestCase import BaseTestCase
from POM.RegestrationPage import RegistrationPage
from Utilities.ReadExcel import ReadExcel


@ddt
class TestExcelDDT(BaseTestCase):
    """ this class represent Registration elements manipulations and functions"""
    @data(ReadExcel.get_data('C:/Users/csadek/Desktop/Automation-Game/Automation-Game/Utilities/Data.xls','Registration'))
    @unpack
    def test_valid_register(self, email, nickname, password, firstname, surname, company, capacity, dateofbirth, phone, mobile,address, zipcode, town, country, how_do_you_know_our_website):

        reg_page = RegistrationPage
        reg_page.Register_with_valid_input(self, email, nickname, password, firstname, surname, company, capacity, dateofbirth, phone, mobile,address, zipcode, town,country, how_do_you_know_our_website)