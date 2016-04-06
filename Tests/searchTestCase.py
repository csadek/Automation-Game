from POM.BaseTestCase import BaseTestCase
from POM.searchPage import SearchPage

class searchTests(BaseTestCase):

    def test_search_products(self):
        SearchPage.search_vaild_Data(self,'trouser','Clothing')

