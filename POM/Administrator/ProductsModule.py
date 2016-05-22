from selenium.webdriver.common.by import By
from POM.BaseTestCase import BaseTestCase


class ProductsModule(BaseTestCase):
    """ this class represents add product page elements manipulations and functions"""
    '''1- check product details(view online)-
    2-calculate promotion
     3- edit product to add tabs & check them online
     4- delete product
     5- windows forms'''
    # Navigators
    admin_button = (By.CSS_SELECTOR,'#main_content > div:nth-child(1) > div > div > div.middle_column_repeat > div > a.btn.btn-warning.pull-right')
    main_menu = (By.CSS_SELECTOR, '#menu_label_products')
    sub_menu = (By.CSS_SELECTOR, '#menu_1bd8d94f')
    add_product_link = (By.CSS_SELECTOR,'a[href^=\"http://10.1.22.67/Jamaica/administrer/produits.php?mode=ajout\"]')

    # Locators
    # first tab
    page_title = (By.CSS_SELECTOR,'#page_title > h1')
    select_category = (By.CSS_SELECTOR,'#categories > option')
    position = (By.NAME,'position')
    our_selection = (By.NAME, 'on_special')
    new = (By.NAME,'on_new' )
    special = (By.NAME,'on_promo')
    reseller = (By.NAME,'on_reseller')
    best_seller = (By.NAME,'on_top')
    recommended = (By.NAME,'recommanded_product_on_cart_page')
    best= (By.NAME,'on_rollover')
    state_online = (By.NAME, 'etat')
    reference = (By.NAME,'reference')
    code = (By.NAME,'technical_code')
    price = (By.NAME,'prix')
    promotion = (By.NAME,'promotion')

    # Second tab
    english_tab = (By.CSS_SELECTOR,'a[href="#tab_EN"]')
    product_name = (By.CSS_SELECTOR,'#tab_EN > input:nth-child(3)')
    short_description = (By.NAME,'descriptif_en')
    description = (By.CSS_SELECTOR,'body')
    add_product_button = (By.CSS_SELECTOR,'#total > div.container > div > div > form > div.center > p > input')
    confirm_delete = (By.CSS_SELECTOR,'body > div.bootbox.modal.fade.in > div > div > div.modal-footer > button.btn.btn-primary')

    # Notification
    alert =(By.CSS_SELECTOR,'#total > div.container > div > div > div.alert.alert-success.fade.in > b')

    # navigate to admin pages
    def admin_view(self):
        self.driver.find_element(*ProductsModule.admin_button).click()

    # Add Product
    def AddProduct(self,position,reference,code,price,name,short,description):
        # Open Add product page
        self.driver.find_element(*ProductsModule.main_menu).click()
        self.driver.find_element(*ProductsModule.sub_menu).click()
        self.driver.find_element(*ProductsModule.add_product_link).click()
        # Add first
        self.driver.find_element(*ProductsModule.select_category).click()
        self.driver.find_element(*ProductsModule.position).clear()
        self.driver.find_element(*ProductsModule.position).send_keys(position)
        self.driver.find_element(*ProductsModule.our_selection).click()
        self.driver.find_element(*ProductsModule.new).click()
        self.driver.find_element(*ProductsModule.special).click()
        self.driver.find_element(*ProductsModule.reseller).click()
        self.driver.find_element(*ProductsModule.recommended).click()
        self.driver.find_element(*ProductsModule.best).click()
        self.driver.find_element(*ProductsModule.state_online).click()
        self.driver.find_element(*ProductsModule.reference).send_keys(reference)
        self.driver.find_element(*ProductsModule.code).send_keys(code)
        self.driver.find_element(*ProductsModule.price).send_keys(price)
        # add second tab
        self.driver.find_element(*ProductsModule.english_tab).click()
        self.driver.find_element(*ProductsModule.product_name).send_keys(name)
        self.driver.find_element(*ProductsModule.short_description).send_keys(short)
        self.driver.find_element(*ProductsModule.description).send_keys(description)
        # submit
        self.driver.find_element(*ProductsModule.add_product_button).click()
        return self.driver.find_element(*ProductsModule.alert).text

    def delete_product(self,name):
        self.driver.find_element_by_css_selector('a[title=\'Delete {}\']'.format(name)).click()
        self.driver.find_element(*ProductsModule.confirm_delete).click()

    def edit_product(self,name):
        self.driver.find_element_by_css_selector('a[title=\'Delete {}\']+a[title=\'Modify\']'.format(name)).click()





