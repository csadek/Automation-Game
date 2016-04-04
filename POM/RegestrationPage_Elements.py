from selenium.webdriver.common.by import By
from Utilities.BasePage_Mahran import BasePageObject


class RegistrationPageObject(BasePageObject):
    """ this class represent Registration elements manipulations and functions"""

    # Locators
    Email = By.ID('email')
    Nickname = By.ID('pseudo')
    FirstName = By.ID('prenom')
    Surname = By.ID('nom_famille')
    Company = By.ID('societe')
    Phone = By.ID('telephone')
    Mobile = By.ID('societe')
    Address = By.ID('adresse')
    Zipcode = By.ID('code_postal')
    Town = By.ID('ville')
    Title = By.XPATH("/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div/form/div[2]/div[1]/span[2]/input[3]")[0]
    Capacity = select_capacity = By.ID("fonction")
    Country = select_Country = By.ID("pays")
    How_do_you_know_our_website = select_Howdoyouknowourwebsite = By.ID("origin")
    FirstSelection = By.ID('newsletter')
    SecondSelection = By.ID('commercial')
    Error_LBL_Email = By.CSS_SELECTOR('div:nth-child(1) > div:nth-child(1) > div.alert.alert-danger.fade.in')
    OpenAccount = By.CSS_SELECTOR('tr:nth-child(2) > td > div > p.center > input.btn.btn-primary.btn-lg')

    def __init__(self, driver):
        super(RegistrationPageObject, self).__init__(driver)

    def Register_with_valid_input(self, email, nickname, firstname, surname, company, phone, mobile, address, zipcode, town, title, capacity, country, how_do_you_know_our_website, firstSelection, secondSelection):
        self.driver.find_element(*RegistrationPageObject.Email).send_keys(email)
        self.driver.find_element(*RegistrationPageObject.Nickname).send_keys(nickname)
        self.driver.find_element(*RegistrationPageObject.FirstName).send_keys(firstname)
        self.driver.find_element(*RegistrationPageObject.Surname).send_keys(surname)
        self.driver.find_element(*RegistrationPageObject.Company).send_keys(company)
        self.driver.find_element(*RegistrationPageObject.Phone).send_keys(phone)
        self.driver.find_element(*RegistrationPageObject.Mobile).send_keys(mobile)
        self.driver.find_element(*RegistrationPageObject.Address).send_keys(zipcode)
        self.driver.find_element(*RegistrationPageObject.Zipcode).send_keys(phone)
        self.driver.find_element(*RegistrationPageObject.Town).send_keys(town)
        self.driver.find_element(*RegistrationPageObject.Title).send_keys(title)
        self.driver.find_element(*RegistrationPageObject.Capacity).send_keys(capacity)
        self.driver.find_element(*RegistrationPageObject.Country).send_keys(country)
        self.driver.find_element(*RegistrationPageObject.How_do_you_know_our_website).send_keys(how_do_you_know_our_website)
        self.driver.find_element(*RegistrationPageObject.FirstSelection).send_keys(firstSelection)
        self.driver.find_element(*RegistrationPageObject.SecondSelection).send_keys(secondSelection)
        error_LBL_Email = self.driver.find_element(*RegistrationPageObject.Error_LBL_Email)
        self.assertTrue(error_LBL_Email.is_displayed())
        self.driver.find_element(*RegistrationPageObject.OpenAccount).click()