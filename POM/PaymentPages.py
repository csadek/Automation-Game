from selenium.webdriver.common.by import By
from POM.BaseTestCase import BaseTestCase


class PaymentPages(BaseTestCase):
    """ this class represent payment1 page elements manipulations and functions"""

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
    #Sale Time details message = i think it needs iframe becouse if i take the selector, the message words will be taken not the frame itself

    #Pop up Form
    Pop_Title = (By.CSS_SELECTOR, 'div.popup_cart_title')
    ContinueMyShopping_Btn = (By.CSS_SELECTOR, 'div.modal-footer > button.btn.btn-success')
    YourCart_Btn = (By.CSS_SELECTOR, 'body > div.bootbox.modal.fade.in > div > div > div.modal-footer > button.btn.btn-primary')
    QuantityNo = (By.CSS_SELECTOR, 'tr:nth-child(1) > td.center')
    AmountNo = (By.CSS_SELECTOR, 'tr:nth-child(2) > td.center')

    #Page3 'Your cart'
    PromoCode_Fld = (By.CSS_SELECTOR, '#code_promo')
    UpdateYourCart_Btn = (By.CSS_SELECTOR, 'div.code_promo > div:nth-child(2) > a')
    ShippingZone_Lst = (By.CSS_SELECTOR, '#choix_zone > p:nth-child(1) > select')
    MeansOfShipping_Lst = (By.CSS_SELECTOR, '#choix_zone > p:nth-child(3) > select > option:nth-child(3)')
    CompeleteUrOrder_Btn = (By.CSS_SELECTOR, 'tr:nth-child(1) > td > p > button')
    CompleteYourOrder_Popup_Btn = (By.CSS_SELECTOR, 'div.modal-body > div > div > a')
    ContinueMyShopping_Page3_Btn = (By.CSS_SELECTOR, 'tr:nth-child(2) > td.td_caddie_link_shopping > a')
    EmptyList_Btn = (By.CSS_SELECTOR, 'tr:nth-child(2) > td.td_caddie_link_empty_cart > a')
    Quantity_Page3_Fld = (By.CSS_SELECTOR, 'td.lignecaddie_quantite.center > div > input')
    NetToPay = (By.CSS_SELECTOR, '#step2caddie > p.caddie_net_to_pay > span')

    #Page4 'Payment means' after choose Means of shipping = Pickup in store
    YourPayment_Hdr = (By.CSS_SELECTOR,'div.middle_column_repeat > h1')
    Company_Fld = (By.CSS_SELECTOR,'#societe1')
    Surname_Fld = (By.CSS_SELECTOR,'#nom1')
    FirstName_Fld = (By.CSS_SELECTOR,'#prenom1')
    Email_Fld = (By.CSS_SELECTOR,'#email1')
    Phone_Fld = (By.CSS_SELECTOR,'#contact1')
    Address_Fld = (By.CSS_SELECTOR,'#adresse1')
    ZipCode_Fld = (By.CSS_SELECTOR,'#code_postal1')
    Town_Fld = (By.CSS_SELECTOR,'#ville1')
    Country_Lst = (By.CSS_SELECTOR,'#pays1')
    Payment_RdBtn = (By.CSS_SELECTOR,'table:nth-child(3) > tbody > tr > td > input[type="radio"')
    Comment_Fld = (By.CSS_SELECTOR,'fieldset:nth-child(2) > div > textarea')
    TermsCond = (By.CSS_SELECTOR,'div > p > input[type="checkbox"]')
    NextStep_Btn = (By.CSS_SELECTOR,'div:nth-child(2) > div > div > input')


    #Page5 'Summary' --> Needs more Verifying and assertions
    CompleteYourOrder_Page5_Btn = (By.CSS_SELECTOR,'div.totalcaddie > form > div.center > input')

    #Page6 'Confirmation page'--> Needs more Verifying and assertions
    Confirm_Msg = (By.CSS_SELECTOR,'div.middle_column_repeat > h1')

    def Pay_Oneproduct(self):
        self.driver.find_element(*PaymentPages.Product_1).click()
        self.driver.implicitly_wait(30)
        self.driver.find_element(*PaymentPages.Color_Lst).click()
        self.driver.implicitly_wait(30)
        self.driver.find_element(*PaymentPages.Size_Lst).click()
        self.driver.implicitly_wait(30)
        self.driver.find_element(*PaymentPages.Quantity_Fld).clear()
        self.driver.find_element(*PaymentPages.Quantity_Fld).send_keys('1')
        self.driver.find_element(*PaymentPages.AddToCard_Btn).click()
        self.driver.implicitly_wait(30)
        self.driver.find_element(*PaymentPages.YourCart_Btn).click()
        self.driver.find_element(*PaymentPages.ShippingZone_Lst).click()
        self.driver.implicitly_wait(30)
        self.driver.find_element(*PaymentPages.MeansOfShipping_Lst).click()
        #The next page will be changed according to Means Of Shipping, So in this Method Pickup in store will be chosen
        self.driver.find_element(*PaymentPages.CompeleteUrOrder_Btn).click()
        #self.driver.find_element(*PaymentPages.CompleteYourOrder_Popup_Btn).click()

        #Page4 'Payment means'
    def Billing_Address(self, company, surename, firstname, email, phone, address, zipcode, town, country, comment):
        self.driver.find_element(*PaymentPages.Company_Fld).clear()
        self.driver.find_element(*PaymentPages.Company_Fld).send_keys(company)
        self.driver.find_element(*PaymentPages.Surname_Fld).send_keys(surename)
        self.driver.find_element(*PaymentPages.FirstName_Fld).send_keys(firstname)
        self.driver.find_element(*PaymentPages.Email_Fld).clear()
        self.driver.find_element(*PaymentPages.Email_Fld).send_keys(email)
        self.driver.find_element(*PaymentPages.Phone_Fld).send_keys(phone)
        self.driver.find_element(*PaymentPages.Address_Fld).send_keys(address)
        self.driver.find_element(*PaymentPages.ZipCode_Fld).send_keys(zipcode)
        self.driver.find_element(*PaymentPages.Town_Fld).send_keys(town)
        self.driver.find_element(*PaymentPages.Country_Lst).send_keys(country)
        self.driver.find_element(*PaymentPages.Payment_RdBtn).click()
        self.driver.find_element(*PaymentPages.Comment_Fld).send_keys(comment)
        self.driver.find_element(*PaymentPages.TermsCond).click()
        self.driver.find_element(*PaymentPages.NextStep_Btn).click()
        #Page5
        self.driver.find_element(*PaymentPages.CompleteYourOrder_Page5_Btn).click()
        #Page6 'Confirmation page'--> Needs more Verifying and assertions
    def get_Confirm_Msg(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*PaymentPages.Confirm_Msg).text