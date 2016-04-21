from selenium.webdriver.common.by import By
from POM.BaseTestCase import BaseTestCase

class CreateBillingAddress(BaseTestCase):
    '''assert on billing address
    pay and select the created billing address'''
    surnameAddress = (By.ID,'name_adresse')
    TypeList= (By.NAME, "address_type")   # type drop down list

    Surname = (By.ID, 'nom_famille')
    FirstName = (By.ID, 'prenom')
    Email = (By.ID,'email')
    Company = (By.ID, 'societe')
    Address = (By.ID, 'adresse')
    Zipcode = (By.ID, 'code_postal')
    Town = (By.ID, 'ville')
    Country = select_Country = (By.ID, "pays")
    Phone = (By.ID, 'portable')
    ValidateBtn = (By.CSS_SELECTOR ,'#main_content > div:nth-child(1) > div > div > div.middle_column_repeat > form > fieldset > p > input' )

    def new_address_vaild_input(self,surAddress,surName,firstName,email,company,address,zipCode,town,country,phone):
        self.driver.find_element(*CreateBillingAddress.surnameAddress).send_keys(surAddress)
        #title radio butto6`n
        #self.driver.find_element(*createBillingAddress.Title).click()

        self.driver.find_element(*CreateBillingAddress.Surname).send_keys(surName)
        self.driver.find_element(*CreateBillingAddress.FirstName).send_keys(firstName)
        self.driver.find_element(*CreateBillingAddress.Email).send_keys(email)
        self.driver.find_element(*CreateBillingAddress.Company).send_keys(company)
        self.driver.find_element(*CreateBillingAddress.Address).send_keys(address)
        self.driver.find_element(*CreateBillingAddress.Zipcode).send_keys(zipCode)
        self.driver.find_element(*CreateBillingAddress.Town).send_keys(town)
        self.driver.find_element(*CreateBillingAddress.Country).send_keys(country)
        self.driver.find_element(*CreateBillingAddress.Phone).send_keys(phone)

        self.driver.find_element(*CreateBillingAddress.ValidateBtn).click()


