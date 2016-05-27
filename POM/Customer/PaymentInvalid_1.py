from selenium.webdriver.common.by import By

from Tests.BaseTestCase import BaseTestCase


class PaymentPages(BaseTestCase):
    '''1- pay with no products selected
    2- pay with missing values.
    3- pay multiple products and calculate
    4- pay multiple products not exists at the store
    '''
    # Locators
    #Page1
    Product_1 = (By.CSS_SELECTOR, 'tr:nth-child(1) > td > a > span')
    SearchField = (By.CSS_SELECTOR, '#search_advanced_input')
    Dropdwn_Words = (By.CSS_SELECTOR, 'ul.attribute_select_search.attribute_select_search_part1 > li > select')
    Dropdwn_Cat = (By.CSS_SELECTOR, 'ul.attribute_select_search.attribute_select_search_part2 > li > select')
    Search_Btn = (By.CSS_SELECTOR, 'div.middle_column_repeat > form > div > input')
    Prdct_Type = (By.CSS_SELECTOR, 'tr:nth-child(1) > td > a > span')
    Prdct_Name = (By.CSS_SELECTOR, 'tr:nth-child(3) > td > div.description_text > a')
    #Sale Time details message = i think it needs iframe becouse if i take the selector, the message words will be taken not the frame itself

    #page2
    Color_Lst = (By.CSS_SELECTOR, '#couleur > option:nth-child(2)')
    Size_Lst = (By.CSS_SELECTOR, '#taille > option:nth-child(5)')
    Quantity_Fld = (By.CSS_SELECTOR, 'div.product_quantity.pull-left > input')
    Warning_Msg_Popup = (By.CSS_SELECTOR, 'div.modal-body > div')
    OK_Popup_Btn = (By.CSS_SELECTOR,'div.modal-footer > button')
    AddToCard_Btn = (By.CSS_SELECTOR, 'tr > td > div.product_order.pull-right > input')
    EditPrdct_AdminLnk = (By.CSS_SELECTOR, 'div.middle_column_repeat > div > p > a')
    PrdctTitle = (By.CSS_SELECTOR, 'div.fp_produit > h1')
    SendEmail_Lnk = (By.CSS_SELECTOR, 'tr.picto-tell_friends > td.txt-tell_friends > a')
    GiveOpenion_Lnk = (By.CSS_SELECTOR, 'tr.picto-avis > td.txt-avis > a')
    AllOpenion_Lnk = (By.CSS_SELECTOR, 'tr.picto-tous_avis > td.txt-tous_avis > a')
    AddToNotePad_Lnk = (By.CSS_SELECTOR, 'tr.picto-pensebete > td.txt-pensebete > a')
    PrintPage_Lnk = (By.CSS_SELECTOR, 'tr.picto-print > td.txt-print > a')

    def Pay_Oneproduct_WithoutColorSize(self):
        self.driver.find_element(*PaymentPages.Product_1).click()
        #self.driver.implicitly_wait(30)
        #self.driver.find_element(*PaymentPages.Color_Lst).click()
        #self.driver.implicitly_wait(30)
        #self.driver.find_element(*PaymentPages.Size_Lst).click()
        self.driver.implicitly_wait(30)
        self.driver.find_element(*PaymentPages.Quantity_Fld).clear()
        self.driver.find_element(*PaymentPages.Quantity_Fld).send_keys('1')
        self.driver.find_element(*PaymentPages.AddToCard_Btn).click()
        self.driver.implicitly_wait(30)

    def get_Error_Msg(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*PaymentPages.Warning_Msg_Popup).text
    def OK(self):
        self.driver.find_element(*PaymentPages.OK_Popup_Btn).click()




