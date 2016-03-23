from selenium import webdriver
from selenium.webdriver.support.ui import Select
from ddt import ddt, data, unpack
from Tests.Regestration_DataFromExcelsheet import Regestration
from Utilities import ReadExcel
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Firefox()

driver.get('http://10.1.22.67/Jamaica/utilisateurs/enregistrement.php')
driver.implicitly_wait(30)

class RegestartionPageObject(webdriver):
    #def __init__(self, webdriver):
    Email = webdriver.find_element_by_name('email')
    '''try:
        Email = webdriver.find_element_by_name('email')
    except NoSuchElementException:
        webdriver.fail("Could not find 'Email' element on page")'''

    Nickname = webdriver.find_element_by_id('pseudo')
    FirstName = webdriver.find_element_by_id('prenom')
    Surname = webdriver.find_element_by_id('nom_famille')
    Company = webdriver.find_element_by_id('societe')
    Phone = webdriver.find_element_by_id('telephone')
    Mobile = webdriver.find_element_by_id('societe')
    Address = webdriver.find_element_by_id('adresse')
    Zipcode = webdriver.find_element_by_id('code_postal')
    Town = webdriver.find_element_by_id('ville')
    Title = webdriver.find_elements_by_xpath(
        "/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div/form/div[2]/div[1]/span[2]/input[3]")[0]
    Capacity = select_capacity = webdriver.find_element_by_id("fonction")
    Country = select_Country = webdriver.find_element_by_id("pays")
    How_do_you_know_our_website = select_Howdoyouknowourwebsite = webdriver.find_element_by_id("origin")
    FirstSelection = webdriver.find_element_by_id('newsletter')
    SecondSelection = webdriver.find_element_by_id('commercial')



    @data(*ReadExcel.get_data( '../Utilities/Data.xls','Regestration'))
    @unpack
    def test_RegestartionPage(self,Email,Nickname,FirstName,Surname,Company,Phone,Mobile,Address,Zipcode,Town):

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

        self.Title.click
        self.Capacity.send_keys(str("Manager"))
        self.Country.send_keys(str("Egypt"))
        self.How_do_you_know_our_website.send_keys(str("Other"))
        self.FirstSelection.click()
        self.SecondSelection.click()


webdriver.close()
