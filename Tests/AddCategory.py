from ddt import ddt, data, unpack
from POM.Administrator.CategoryPage import CategoryPage
from POM.BaseTestCase import BaseTestCase
from POM.LoginLogoutPage import LoginLogoutPage
from Utilities.ReadExcel import ReadExcel


@ddt
class AddCategory(BaseTestCase):

    @data(*ReadExcel.get_data('../Utilities/Data.xlsx','LoginValid'))
    @unpack
    def test_add(self,user,password):
        LoginLogoutPage.login_with_valid_credentials(self, user, password)

    @data(*ReadExcel.get_data('../Utilities/Data.xlsx','Categories'))
    @unpack
    def test_add_category(self,name, parent):
        self.assertTrue(CategoryPage.add_category(self,name,parent))
