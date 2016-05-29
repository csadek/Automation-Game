from ddt import ddt, data, unpack
from POM.Administrator.ManageUserPage import ManageUserPage
from Tests.BaseTestCase import BaseTestCase
from Utilities.ReadExcel import ReadExcel


@ddt
class ManageUser(BaseTestCase):

    @unpack
    @data(*ReadExcel.get_sheets('../Utilities/Data.xlsx',['LoginValid','Registration']))
    def test_edit(self,username,passw,email,nickname,password,firstName,surname,company,capacity,dateofbirth,phone,mobile,address,zipcode,town,country,how_do_you_know_our_website,Message,):
        self.assertIn(email,ManageUserPage.edit_user(self,username,passw,email))