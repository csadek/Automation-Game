from selenium.webdriver.common.by import By
import pymysql
from Tests.BaseTestCase import BaseTestCase
import ConfigReader as Conf
from POM.LoginLogoutPage import LoginLogoutPage


class RegistrationPage(BaseTestCase):
    """ this class represent Registration elements manipulations and functions"""
    # Locators
    Email = (By.CSS_SELECTOR,'#email')
    Nickname = (By.CSS_SELECTOR,'#pseudo')
    Password = (By.CSS_SELECTOR,'#mot_passe')
    FirstName = (By.ID, 'prenom')
    Surname = (By.ID, 'nom_famille')
    Company = (By.ID, 'societe')
    Phone = (By.ID, 'telephone')
    Mobile = (By.ID, 'societe')
    Address = (By.ID, 'adresse')
    Zipcode = (By.ID, 'code_postal')
    Town = (By.ID, 'ville')
    Title =(By.NAME,'civilite')
    #Title = (By.CSS_SELECTOR,'div:nth-child(2) > div:nth-child(1) > span.enregistrementdroite > input[type="radio"]:nth-child(1)')
    Capacity = select_capacity = (By.ID, "fonction")
    DateOfBirth = (By.CSS_SELECTOR,'#naissance')
    Country = select_Country = (By.ID, "pays")
    How_do_you_know_our_website = select_Howdoyouknowourwebsite = (By.ID, "origin")
    Code = (By.CSS_SELECTOR,'#code')
    FirstSelection = (By.ID, 'newsletter')
    SecondSelection = (By.ID, 'commercial')
    OpenAccount = (By.CSS_SELECTOR, 'tr:nth-child(2) > td > div > p.center > input.btn.btn-primary.btn-lg')
    Thanks_Msg = (By.CSS_SELECTOR, 'div.middle_column_repeat > p')

    def Register_with_valid_input(self,email, nickname, password, firstname, surname, company, capacity, dateofbirth, phone, mobile,address, zipcode, town, country, how_do_you_know_our_website):
        self.driver.get(Conf.read_ini_config('Paths','RegisterURL'))
        self.driver.find_element(*RegistrationPage.Email).send_keys(email)
        self.driver.find_element(*RegistrationPage.Nickname).send_keys(nickname)
        self.driver.find_element(*RegistrationPage.Password).send_keys(password)
        self.driver.find_element(*RegistrationPage.FirstName).send_keys(firstname)
        self.driver.find_element(*RegistrationPage.Surname).send_keys(surname)
        self.driver.find_element(*RegistrationPage.Company).send_keys(company)
        self.driver.find_element(*RegistrationPage.Phone).send_keys(phone)
        self.driver.find_element(*RegistrationPage.Mobile).send_keys(mobile)
        self.driver.find_element(*RegistrationPage.Address).send_keys(address)
        self.driver.find_element(*RegistrationPage.Zipcode).send_keys(zipcode)
        self.driver.find_element(*RegistrationPage.Phone).send_keys(phone)
        self.driver.find_element(*RegistrationPage.Town).send_keys(town)
        self.driver.find_element(*RegistrationPage.Title).click()
        self.driver.find_element(*RegistrationPage.Capacity).send_keys(capacity)
        self.driver.find_element(*RegistrationPage.DateOfBirth).send_keys(dateofbirth)
        self.driver.find_element(*RegistrationPage.Country).send_keys(country)
        self.driver.find_element(*RegistrationPage.How_do_you_know_our_website).send_keys(how_do_you_know_our_website)
        self.driver.find_element(*RegistrationPage.Code).send_keys('12340')
        self.driver.find_element(*RegistrationPage.FirstSelection).click()
        self.driver.find_element(*RegistrationPage.SecondSelection).click()
        self.driver.find_element(*RegistrationPage.OpenAccount).click()
        alert =self.driver.find_element(*RegistrationPage.Thanks_Msg).text
        LoginLogoutPage.logout(self)
        return alert

    def verify_user_at_DB(self, username):
        # Connect to database to search for user using username
        #TODO: this should be added at utilities
        conn = pymysql.connect(host='10.1.22.67', port=3306, user='Selenium', passwd='python', db='peel')
        cur = conn.cursor()
        cur.execute("SELECT `email` FROM `peel_utilisateurs` WHERE `pseudo` ='{}' ".format(username))
        email = cur.fetchone()
        return email