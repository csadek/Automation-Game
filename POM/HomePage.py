from selenium.webdriver.common.by import By
from HelpReferences import basetestcase

class HomePageObject(basetestcase):
    logoutbutton = By.CLASS_NAME("btn btn-primary pull-right")


    def test_search_products(self, username, password):
        self.logoutbutton
        self.Username.send_keys(username)
        self.Password.send_keys(password)
        self.Submit.click()


