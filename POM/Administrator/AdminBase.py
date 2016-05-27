import ConfigReader as Conf
from selenium.webdriver.common.by import By
from Tests.BaseTestCase import BaseTestCase
from POM.LoginLogoutPage import LoginLogoutPage


class AdminBase(BaseTestCase):
    # Navigators
    admin_button = (By.CSS_SELECTOR,'a[class="btn btn-warning pull-right"]')
    products_main =(By.CSS_SELECTOR, '#menu_label_products')
    products_sub =(By.CSS_SELECTOR, '#menu_1bd8d94f')
    product_list_link=(By.CSS_SELECTOR,'a[title="Products list"]')
    add_product_link = (By.CSS_SELECTOR,'a[title="Add a product"]')
    category_sub = (By.CSS_SELECTOR, '#menu_820845ea')
    add_category_link = (By.CSS_SELECTOR,'a[title="Add category"]')
    category_list_link = (By.CSS_SELECTOR,'a[title="Categories list"]')
    users_main =(By.CSS_SELECTOR, '#menu_label_users')
    users_sub = (By.CSS_SELECTOR, '#menu_3233bb4a')
    users_list_link = (By.CSS_SELECTOR,'a[title="Users list"]')
    customer_loyalty_link = (By.CSS_SELECTOR, '#menu_bc24ec8e')
    coupon_codes_link = (By.CSS_SELECTOR,'a[title="Coupon codes"]')

    # constructor
    def __init__(self, driver):
        super(AdminBase, self.__init__(driver))

    # navigate to admin pages
    def navigate_to_admin(self,username, password):
        if Conf.read_ini_config('Paths','LoginURL') in self.driver.current_url:
            loginlogout_obj = LoginLogoutPage()
            if self.driver.find_element(loginlogout_obj.logout_link).text == 'Log in':
                loginlogout_obj.login_with_valid_credentials(username,password)
                self.driver.get(Conf.read_ini_config('Paths','HomeURL'))
                self.driver.find_element(*AdminBase.admin_button).click()
            else:
                self.driver.get(Conf.read_ini_config('Paths','HomeURL'))
                self.driver.find_element(*AdminBase.admin_button).click()

    def view_users(self):
        self.driver.find_element(*AdminBase.users_main).click()
        self.driver.find_element(*AdminBase.users_sub).click()
        self.driver.find_element(*AdminBase.users_list_link).click()

    def add_coupon_navigator(self):
        self.driver.find_element(*AdminBase.users_main).click()
        self.driver.find_element(*AdminBase.customer_loyalty_link).click()
        self.driver.find_element(*AdminBase.coupon_codes_link).click()

    def edit_product_navigator(self):
        self.driver.find_element(*AdminBase.products_main).click()
        self.driver.find_element(*AdminBase.products_sub).click()
        self.driver.find_element(*AdminBase.product_list_link).click()

    def add_product_navigator(self):
        self.driver.find_element(*AdminBase.products_main).click()
        self.driver.find_element(*AdminBase.products_sub).click()
        self.driver.find_element(*AdminBase.add_product_link).click()

    def edit_category_navigator(self):
        self.driver.find_element(*AdminBase.products_main).click()
        self.driver.find_element(*AdminBase.category_sub).click()
        self.driver.find_element(*AdminBase.category_list_link).click()

    def add_category_navigator(self):
        self.driver.find_element(*AdminBase.products_main).click()
        self.driver.find_element(*AdminBase.category_sub).click()
        self.driver.find_element(*AdminBase.add_category_link).click()

