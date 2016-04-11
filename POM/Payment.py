from selenium.webdriver.common.by import By
from POM.BaseTestCase import BaseTestCase


class Payment1(BaseTestCase):
    """ this class represent payment1 page elements manipulations and functions"""

    # Locators
    #Page1
    Product_1 = (By.CSS_SELECTOR, 'tr:nth-child(2) > td > span > a > img')
    SearchField = (By.CSS_SELECTOR, '#search_advanced_input')
    Dropdwn_Words = (By.CSS_SELECTOR, 'ul.attribute_select_search.attribute_select_search_part1 > li > select')
    Dropdwn_Cat = (By.CSS_SELECTOR, 'ul.attribute_select_search.attribute_select_search_part2 > li > select')
    Search_Btn = (By.CSS_SELECTOR, 'div.middle_column_repeat > form > div > input')
    Prdct_Type = (By.CSS_SELECTOR, 'tr:nth-child(1) > td > a > span')
    Prdct_Name = (By.CSS_SELECTOR, 'tr:nth-child(3) > td > div.description_text > a')
    #Sale Time details message = i think it needs iframe becouse if i take the selector, the message words will be taken not the frame itself

    #page2
    Quantity_Fld = (By.CSS_SELECTOR, 'tr > td > div.product_quantity.pull-left > input')
    AddToCard_Btn = (By.CSS_SELECTOR, 'div.product_order.pull-right > input')
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
    def Pay_Oneproduct(self):
        self.driver.find_element(*Payment1.Product_1).click()
        self.driver.find_element(*Payment1.Quantity_Fld).clear()
        self.driver.find_element(*Payment1.Quantity_Fld).send_keys('1')
        self.driver.find_element(*Payment1.AddToCard_Btn).click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(*Payment1.YourCart_Btn).click()
        self.driver.find_element(*Payment1.ShippingZone_Lst).click()
        self.driver.implicitly_wait(30)
        self.driver.find_element(*Payment1.MeansOfShipping_Lst).click()
        #The next page will be changed according to Means Of Shipping, So in this Method Pickup in store will be chosen
        self.driver.find_element(*Payment1.CompeleteUrOrder_Btn).click()

        #Page4 'Payment means'
    def Billing_Address(self, company, surename, firstname, email, phone, address, zipcode, town, country, comment):
        self.driver.find_element(*Payment1.Company_Fld).send_keys(company)
        self.driver.find_element(*Payment1.Surname_Fld).send_keys(surename)
        self.driver.find_element(*Payment1.FirstName_Fld).send_keys(firstname)
        self.driver.find_element(*Payment1.Email_Fld).clear()
        self.driver.find_element(*Payment1.Email_Fld).send_keys(email)
        self.driver.find_element(*Payment1.Phone_Fld).send_keys(phone)
        self.driver.find_element(*Payment1.Address_Fld).send_keys(address)
        self.driver.find_element(*Payment1.ZipCode_Fld).send_keys(zipcode)
        self.driver.find_element(*Payment1.Town_Fld).send_keys(town)
        self.driver.find_element(*Payment1.Country_Lst).send_keys(country)
        self.driver.find_element(*Payment1.Payment_RdBtn).click()
        self.driver.find_element(*Payment1.Comment_Fld).send_keys(comment)
        self.driver.find_element(*Payment1.TermsCond).click()
        self.driver.find_element(*Payment1.NextStep_Btn).click()
        #Page5
        self.driver.find_element(*Payment1.CompleteYourOrder_Page5_Btn).click()
        #Page6 'Confirmation page'--> Needs more Verifying and assertions
