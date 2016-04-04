from selenium.webdriver.common.by import By
from HelpReferences import basetestcase

class LoginPageObject(basetestcase):
    login = By.CLASS_NAME("header_user_text")
    Username = By.NAME("email")
    Password = By.NAME("mot_passe")
    Submit = By.CLASS_NAME("btn-success")

    def test_search_products(self, username, password):
        self.login.click()
        self.Username.send_keys(username)
        self.Password.send_keys(password)
        self.Submit.click()

  '''  def test_search_products(self, username, password):
        self.login.click()
        self.Username.send_keys(username)
        self.Password.send_keys(password)
        self.Submit.click()
'''
