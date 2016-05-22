from ddt import ddt, data, unpack

from POM.BaseTestCase import BaseTestCase
from POM.Customer.ManageUserPage import ManageUserPage
from POM.LoginLogoutPage import LoginLogoutPage
from Utilities.ReadExcel import ReadExcel


@ddt
class ManageUser(BaseTestCase):

    @unpack
    @data(*ReadExcel.get_data('../Utilities/Data.xlsx','LoginValid'))
    def test_Add(self,user,password):
        LoginLogoutPage.login_with_valid_credentials(self, user, password)
        ManageUserPage.admin_view(self)

    def test_edit(self):
        ManageUserPage.edit_user(self)