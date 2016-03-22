from selenium import webdriver
from selenium.webdriver.support.ui import Select


class LoginPageObject(webdriver):
    login = webdriver.find_element_by_class_name("header_user_text")
    Username = webdriver.find_element_by_name("email")
    Password = webdriver.find_element_by_name("mot_passe")
    Submit = webdriver.find_element_by_class_name("btn-success")

    def test_search_products(self, username, password):
        self.login.click()
        self.Username.send_keys(username)
        self.Password.send_keys(password)
        self.Submit.click()