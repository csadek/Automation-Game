from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

driver.get('http://10.1.22.67/jamaica/')
driver.implicitly_wait(30)

Login = driver.find_element_by_id("header_login").click()

Email = driver.find_element_by_id("header_login")
Email.select_by_visible_text("email")
Email.send_keys("eng.mohammadrihan@gmail.com")

Password = driver.find_element_by_id("header_login")
Password.select_by_visible_text("email")
Password.send_keys("")

Login = driver.find_element_by_id("header_login")
Login.select_by_visible_text("log in")
Login.click()

#here should be an assertion to verify openning the next page after logging in.

Logout = driver.find_element_by_class_name('glyphicon glyphicon-log-out')
Logout.click()
driver.close()
