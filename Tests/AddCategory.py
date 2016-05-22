from POM.BaseTestCase import BaseTestCase
from POM.LoginLogoutPage import LoginLogoutPage
from POM.CategoryPage import CategoryPage
from Utilities.ReadExcel import ReadExcel
from ddt import ddt, data, unpack


@ddt
class AddCategory(BaseTestCase):

    @data(*ReadExcel.get_data('../Utilities/Data.xlsx','LoginValid'))
    @unpack
    def test_add(self,user,password):
        LoginLogoutPage.login_with_valid_credentials(self, user, password)
        CategoryPage.admin_view(self)

    @data(*ReadExcel.get_data('../Utilities/Data.xlsx','Categories'))
    @unpack
    def test_add_category(self,name, parent):
        self.assertIn(name,CategoryPage.add_category(self,name,parent))

    def test_end(self):
        LoginLogoutPage.logout(self)