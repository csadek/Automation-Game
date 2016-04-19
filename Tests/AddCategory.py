from POM.BaseTestCase import BaseTestCase
from POM.LoginLogoutPage import LoginLogoutPage
from POM.CategoryPage import AddCategoryPage
from Utilities.ReadExcel import ReadExcel
from ddt import ddt, data, unpack


@ddt
class AddCategory(BaseTestCase):

    @data(*ReadExcel.get_data('../Utilities/Data.xlsx','LoginValid'))
    @unpack
    def test_add(self,user,password):
        LoginLogoutPage.login_with_valid_credentials(self, user, password)
        AddCategoryPage.admin_view(self)

    @data(*ReadExcel.get_data('../Utilities/Data.xlsx','Categories'))
    @unpack
    def test_add_category(self,position,name):
        AddCategoryPage.add_category(self,position,name)

    @data(*ReadExcel.get_data('../Utilities/Data.xlsx','Sub'))
    @unpack
    def test_add_sub_category(self,position,name,no):
        AddCategoryPage.add_sub_category(self,position,name,no)

    def test_end(self):
        LoginLogoutPage.logout(self)