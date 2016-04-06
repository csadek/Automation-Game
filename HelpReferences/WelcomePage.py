from selenium.webdriver.common.by import By
from HelpReferences import basetestcase


class welcomepage(basetestcase):
    """ this class represent login page elements manipulations and functions"""

    # Locators
    logoutbutton = (By.CLASS_NAME,"btn btn-primary pull-right")

    def __init__(self):
        pass




