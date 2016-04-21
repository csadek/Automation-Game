from selenium.webdriver.common.by import By
from POM.BaseTestCase import BaseTestCase


class AddPromotionCodePage(BaseTestCase):
    """ this class represent login page elements manipulations and functions"""
    '''use coupon at payment - calculate price & check price'''
   # Navigators
    admin_button = (By.CSS_SELECTOR,'#main_content > div:nth-child(1) > div > div > div.middle_column_repeat > div > a.btn.btn-warning.pull-right')
    main_menu = (By.CSS_SELECTOR, '#menu_label_users')
    sub_menu = (By.CSS_SELECTOR, '#menu_bc24ec8e')
    add_coupon = (By.CSS_SELECTOR,'a[href^=\"http://10.1.22.67/Jamaica/administrer/codes_promos.php\"]')
    add_coupon_link = (By.CSS_SELECTOR,'#total > div.container > div > div > p > a:nth-child(4)')

    # Locators
    promotion_code = (By.NAME, 'nom')
    end_date = (By.NAME, 'date_fin')
    discount = (By.NAME,'remise_valeur')
    status_active = (By.NAME,'etat')
    add_coupon_button = (By.CSS_SELECTOR,'#total > div.container > div > div > form > table > tbody > tr:nth-child(15) > td > p > input')

    #Notification
    page_title = (By.CSS_SELECTOR,'#total > div.container > div > div > div.entete')

    #Add coupon
    def AddCoupon(self,code_name,end,sale):
        # Open Add product page
        self.driver.find_element(*AddPromotionCodePage.admin_button).click()
        self.driver.find_element(*AddPromotionCodePage.main_menu).click()
        self.driver.find_element(*AddPromotionCodePage.sub_menu).click()
        self.driver.find_element(*AddPromotionCodePage.add_coupon).click()
        self.driver.find_element(*AddPromotionCodePage.add_coupon_link).click()

        #Add coupon
        self.driver.find_element(*AddPromotionCodePage.promotion_code).send_keys(code_name)
        self.driver.find_element(*AddPromotionCodePage.end_date).clear()
        self.driver.find_element(*AddPromotionCodePage.end_date).send_keys(end)
        self.driver.find_element(*AddPromotionCodePage.discount).send_keys(sale)
        self.driver.find_element(*AddPromotionCodePage.status_active).click()

        #submit
        self.driver.find_element(*AddPromotionCodePage.add_coupon_button).click()

    def get_page_name(self):
        return self.driver.find_element(*AddPromotionCodePage.page_title).text



