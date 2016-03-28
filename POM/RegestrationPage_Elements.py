from selenium import webdriver
from selenium.webdriver.support.ui import Select
from ddt import ddt, data, unpack
from Tests.Regestration_DataFromExcelsheet import Regestration
from Utilities import ReadExcel
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('http://10.1.22.67/Jamaica/utilisateurs/enregistrement.php')
driver.implicitly_wait(30)

class RegistrationPageObject(driver):
    def __init__(self):
        driver.get('http://10.1.22.67/Jamaica/utilisateurs/enregistrement.php')
        driver.implicitly_wait(30)

    Email = driver.find_element_by_class_name('email')
    Nickname = driver.find_element_by_id('pseudo')
    FirstName = driver.find_element_by_id('prenom')
    Surname = driver.find_element_by_id('nom_famille')
    Company = driver.find_element_by_id('societe')
    Phone = driver.find_element_by_id('telephone')
    Mobile = driver.find_element_by_id('societe')
    Address = driver.find_element_by_id('adresse')
    Zipcode = driver.find_element_by_id('code_postal')
    Town = driver.find_element_by_id('ville')
    Title = driver.find_elements_by_xpath("/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div/form/div[2]/div[1]/span[2]/input[3]")[0]
    Capacity = select_capacity = driver.find_element_by_id("fonction")
    Country = select_Country = driver.find_element_by_id("pays")
    How_do_you_know_our_website = select_Howdoyouknowourwebsite = driver.find_element_by_id("origin")
    FirstSelection = driver.find_element_by_id('newsletter')
    SecondSelection = driver.find_element_by_id('commercial')

    Read = ReadExcel.ReadExcel.get_data('../Utilities/Data.xls', 'Registration')
    data(*(Read))
    #@data(*(ReadExcel.ReadExcel.get_data('../Utilities/Data.xls', 'Registration')))
    @unpack
    def test_registration(self, Email, Nickname, FirstName, Surname, Company, Phone, Mobile, Address, Zipcode,Town):
        self.Email.send_keys(Email)
        self.Nickname.send_keys(Nickname)
        self.FirstName.send_keys(FirstName)
        self.Surname.send_keys(Surname)
        self.Company.send_keys(Company)
        self.Phone.send_keys(Phone)
        self.Mobile.send_keys(Mobile)
        self.Address.send_keys(Address)
        self.Zipcode.send_keys(Zipcode)
        self.Town.send_keys(Town)
        self.Title.click()
        self.Capacity.send_keys(str("Manager"))
        self.Country.send_keys(str("Egypt"))
        self.How_do_you_know_our_website.send_keys(str("Other"))
        self.FirstSelection.click()
        self.SecondSelection.click()


driver.close()
