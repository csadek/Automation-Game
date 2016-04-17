from selenium.webdriver.common.by import By
from POM.BaseTestCase import BaseTestCase

class createBillingAddress(BaseTestCase):
    surnameAddress = (By.ID,'name_adresse')
    TypeList= (By.NAME, "address_type")   # type drop down list

    Surname = (By.ID, 'nom_famille')
    FirstName = (By.ID, 'prenom')
    Email = (By.ID,'email')
    Company = (By.ID, 'societe')
    Address = (By.ID, 'adresse')
    Zipcode = (By.ID, 'code_postal')
    Town = (By.ID, 'ville')
    Country =(By.CLASS_NAME, "form-control")   #country drop list
    Phone = (By.ID, 'telephone')
    ValidateBtn = (By.NAME ,'Validate' )

    def new_address_vaild_input(self,surAddress,type,surName,firstName,email,company,address,zipCode,town,country,phone):
        self.driver.find_element(*createBillingAddress.surnameAddress).send_keys(surAddress)
        self.driver.find_element(*createBillingAddress.TypeList).send_keys(type)
        #title radio button
        #self.driver.find_element(*createBillingAddress.Title).click()

        self.driver.find_element(*createBillingAddress.Surname).send_keys(surName)
        self.driver.find_element(*createBillingAddress.FirstName).send_keys(firstName)
        self.driver.find_element(*createBillingAddress.Email).send_keys(email)
        self.driver.find_element(*createBillingAddress.Company).send_keys(company)
        self.driver.find_element(*createBillingAddress.Address).send_keys(address)
        self.driver.find_element(*createBillingAddress.Zipcode).send_keys(zipCode)
        self.driver.find_element(*createBillingAddress.Town).send_keys(town)
        self.driver.find_element(*createBillingAddress.Country).send_keys(country)
        self.driver.find_element(*createBillingAddress.Phone).send_keys(phone)

        self.driver.find_element(*createBillingAddress.ValidateBtn).click()


