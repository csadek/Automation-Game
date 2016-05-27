from selenium.webdriver.common.by import By
from POM.BaseTestCase import BaseTestCase
import sys, string, os

class ProductsModule(BaseTestCase):
    """ this class represents product page elements manipulations and functions. Administrator should be able to:
     - Add new products for specific categories
     - Edit existing product
     - Delete product at specific category or subcategory"""

    # Navigators
    admin_button = (By.CSS_SELECTOR,'a[class="btn btn-warning pull-right"]')
    product_menu = (By.CSS_SELECTOR, '#menu_label_products')
    product_sub_menu = (By.CSS_SELECTOR, '#menu_1bd8d94f')
    add_product_link = (By.CSS_SELECTOR,'a[href^=\"http://10.1.22.67/Jamaica/administrer/produits.php?mode=ajout\"]')

    # Locators
    # first tab
    category = (By.CSS_SELECTOR,'#categories > option')
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
    product_instructions = (By.CSS_SELECTOR,'a[href="http://10.1.22.67/Jamaica/administrer/produits.php?mode=modif_tab&id=1&tab_lang=en"]')
    content_tab1 = (By.NAME,'tab1_title_en')
    content_desc1 = (By.CSS_SELECTOR,'#xEditingArea > iframe')
    content_tab2 = (By.NAME,'tab2_title_en')
    content_desc2= (By.CSS_SELECTOR,'#tab2_html_en___Frame')
    save_content = (By.CSS_SELECTOR,'#total > div.container > div > div > form > table > tbody > tr:nth-child(21) > td > input')
    confirm_tab2 =(By.CLASS_NAME,'alert alert-success fade in')

    # Third tab
    file_associated_tab = (By.CSS_SELECTOR,'a[href="#tab2"]')
    image_upload_button = (By.CSS_SELECTOR,'#image1 > div > div.qq-upload-button > input[type="file"]')


    # Save & notify
    save_button = (By.CSS_SELECTOR,'#total > div.container > div > div > form > div.center > p > input')
    confirm_delete = (By.CSS_SELECTOR,'body > div.bootbox.modal.fade.in > div > div > div.modal-footer > button.btn.btn-primary')
    confirm_msg =(By.CSS_SELECTOR,'#total > div.container > div > div > div.alert.alert-success.fade.in > b')
    page_title = (By.CSS_SELECTOR,'#page_title > h1')

    # Add Product
    def AddProduct(self,position,reference,code,price,name,short,description):
        # Open Add product page
        if 'http://10.1.22.67/Jamaica/achat' in self.driver.current_url:
            self.driver.get('http://10.1.22.67/Jamaica/compte.php')
            self.driver.find_element(*ProductsModule.admin_button).click()
        elif 'http://10.1.22.67/Jamaica/compte.php' in self.driver.current_url:
            self.driver.find_element(*ProductsModule.admin_button).click()
        else:
            pass
        self.driver.find_element(*ProductsModule.product_menu).click()
        self.driver.find_element(*ProductsModule.product_sub_menu).click()
        self.driver.find_element(*ProductsModule.add_product_link).click()

        # Add first
        self.driver.find_element(*ProductsModule.category).click()
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

        #add Third tab - Jihad
        self.driver.find_element(*ProductsModule.file_associated_tab).click()
        self.driver.find_element(*ProductsModule.image_upload_button).submit()
        self.driver.implicitly_wait(10)
        os.system("C:\\Users\\jmohamed\\Desktop\\AutoIDscript.exe")
        self.driver.implicitly_wait(30)

        # submit
        self.driver.find_element(*ProductsModule.save_button).click()
        return self.driver.find_element(*ProductsModule.confirm_msg).text

    # edit product details
    def edit_product(self,name,tab1,desc1,tab2,desc2):
        # Add product details
        self.driver.find_element_by_css_selector('a[title=\'Delete {}\']+a[title=\'Modify\']'.format(name)).click()
        self.driver.find_element(*ProductsModule.english_tab).click()
        self.driver.find_element(*ProductsModule.product_instructions).click()
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        self.driver.find_element(*ProductsModule.content_tab1).clear()
        self.driver.find_element(*ProductsModule.content_tab1).send_keys(tab1)
        self.driver.find_element(*ProductsModule.content_desc1).clear()
        self.driver.find_element(*ProductsModule.content_desc1).send_keys(desc1)
        self.driver.find_element(*ProductsModule.content_tab2).clear()
        self.driver.find_element(*ProductsModule.content_tab2).send_keys(tab2)
        self.driver.find_element(*ProductsModule.content_desc2).clear()
        self.driver.find_element(*ProductsModule.content_desc2).send_keys(desc2)
        self.driver.find_element(*ProductsModule.save_content).click()
        return self.driver.find_element(*ProductsModule.confirm_tab2).text

    # delete product
    def delete_product(self,name):
        self.driver.find_element_by_css_selector('a[title=\'Delete {}\']'.format(name)).click()
        self.driver.find_element(*ProductsModule.confirm_delete).click()



