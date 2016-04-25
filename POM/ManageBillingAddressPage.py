from selenium.webdriver.common.by import By
from POM.BaseTestCase import BaseTestCase


class ManageBillingAddressPage(BaseTestCase):
    PageTitle = (By.CLASS_NAME,'page_title')
    BillingAddressLink = (By.PARTIAL_LINK_TEXT,'Manage my billing and shipping addresses')
    BillingAddressList = (By.ID , 'address_default')
    ShippingAddress = (By.NAME,'personal_address_ship')
    CreatAddressBtn = (By.PARTIAL_LINK_TEXT ,'Create another address')
    surnameAddress=(By.NAME,'name_adresse')
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

    def manage_billing(self):
        self.driver.find_element(*ManageBillingAddressPage.BillingAddressLink).click()


    def Create_Another_Address(self,surAddress,surName,firstName,email,company,address,zipCode,town,country,phone):
        self.driver.find_element(*ManageBillingAddressPage.CreatAddressBtn).click()
        self.driver.find_element(*ManageBillingAddressPage.surnameAddress).send_keys(surAddress)
        self.driver.find_element(*ManageBillingAddressPage.Surname).send_keys(surName)
        self.driver.find_element(*ManageBillingAddressPage.FirstName).send_keys(firstName)
        self.driver.find_element(*ManageBillingAddressPage.Email).send_keys(email)
        self.driver.find_element(*ManageBillingAddressPage.Company).send_keys(company)
        self.driver.find_element(*ManageBillingAddressPage.Address).send_keys(address)
        self.driver.find_element(*ManageBillingAddressPage.Zipcode).send_keys(zipCode)
        self.driver.find_element(*ManageBillingAddressPage.Town).send_keys(town)
        self.driver.find_element(*ManageBillingAddressPage.Country).send_keys(country)
        self.driver.find_element(*ManageBillingAddressPage.Phone).send_keys(phone)

        self.driver.find_element(*ManageBillingAddressPage.ValidateBtn).click()

    def __init__(self, driver):
        super(ManageBillingAddressPage, self).__init__(driver)
