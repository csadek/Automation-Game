import pymysql
from selenium.webdriver.common.by import By
from POM.Administrator.AdminBase import AdminBase


class AddPromotionCodePage(AdminBase):
    """ this class represent add promotion code page to specific product elements manipulations and functions"""

    # Locators
    promotion_code = (By.NAME, 'nom')
    start_date = (By.NAME,'date_debut')
    end_date = (By.NAME, 'date_fin')
    discount = (By.NAME,'remise_valeur')
    status_active = (By.NAME,'etat')
    add_coupon_button = (By.CSS_SELECTOR,'#total > div.container > div > div > p > a:nth-child(4)')
    submitbutton = (By.CSS_SELECTOR,'#total > div.container > div > div > form > table > tbody > tr:nth-child(15) > td > p > input')

    # Alert
    alert = (By.CSS_SELECTOR,'div[class=\'alert alert-success fade in\']')

    # Add coupon
    def AddCoupon(self,username,password,code_name,start,end,sale):
        # Open coupon codes page
        AdminBase.navigate_to_admin(self,username,password)
        AdminBase.add_coupon_navigator(self)
        # Add coupon
        self.driver.find_element(*AddPromotionCodePage.add_coupon_button).click()
        self.driver.find_element(*AddPromotionCodePage.promotion_code).send_keys(code_name)
        self.driver.find_element(*AddPromotionCodePage.start_date).clear()
        self.driver.find_element(*AddPromotionCodePage.start_date).send_keys(start)
        self.driver.find_element(*AddPromotionCodePage.end_date).clear()
        self.driver.find_element(*AddPromotionCodePage.end_date).send_keys(end)
        self.driver.find_element(*AddPromotionCodePage.discount).click()
        self.driver.find_element(*AddPromotionCodePage.discount).send_keys(int(sale))
        self.driver.find_element(*AddPromotionCodePage.status_active).click()

        # submit
        self.driver.find_element(*AddPromotionCodePage.submitbutton).click()
        return self.driver.find_element(*AddPromotionCodePage.alert).text

    def get_valid_coupon_data(self, end_date):
        # Connect to database to search for valid code using end date and state active
        #TODO: this should be added at utilities
        conn = pymysql.connect(host='10.1.22.67', port=3306, user='Selenium', passwd='python', db='peel')
        cur = conn.cursor()
        cur.execute("SELECT `nom`, `remise_valeur` FROM `peel_codes_promos` WHERE `date_fin`> {} && `etat` = 1".format(end_date))
        coupon_data = cur.fetchone()[0][1]
        return coupon_data


