from selenium.webdriver.common.by import By
from POM.BaseTestCase import BaseTestCase


class AddProduct(BaseTestCase):

    """ this class represents add product page elements manipulations and functions"""

    # Locators
    AddProductMenu = By.CSS_SELECTOR("a[href^=\"http://10.1.22.67/Jamaica/administrer/produits.php?mode=ajout\"]")
    SelectCategory = By.NAME("categories[]")
    Position = By.NAME("position")




    def __init__(self, driver):
        super(AddProduct, self).__init__(driver)




