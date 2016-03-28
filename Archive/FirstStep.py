from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://timelive.integrantinc.com/")

username = driver.find_element_by_name('CtlLogin1$Login1$UserName')
password = driver.find_element_by_name('CtlLogin1$Login1$Password')
Go = driver.find_element_by_name('CtlLogin1$Login1$LoginButton')

username.send_keys('MRihan@integrant.com')
password.send_keys('123@sta.com')
Go.send_keys(Keys.ENTER)

MyTimesheet = driver.find_element_by_id('ctl00_ctl00_ContentPlaceHolderLeftMenu_CtlAccountAdminSiteMenu1_menu_ctl00_Repeater1_ctl04_HyperLink2')
MyTimesheet.send_keys(Keys.ENTER)
Value=4816
select = driver.find_element_by_id('ctl00_ctl00_ContentPlaceHolderBody_ContentPlaceHolderBody_CtlAccountEmployeeTimeEntryDayView1_BulkEditGridViewVB1_ctl07_ddlAccountProjectTaskId').click()


#for option in select.find_elements_by_tag_name('option'):
    #if option.text == '4816':
        #option.click() # select() in earlier versions of webdriver
        #break
#select.select_by_visible_text("Select Tasks")
#select.send_keys(Keys.ENTER)

#select.find_element_by_xpath("//select[@name='ctl00$ctl00$ContentPlaceHolderBody$ContentPlaceHolderBody$CtlAccountEmployeeTimeEntryDayView1$BulkEditGridViewVB1$ctl07$ddlAccountProjectTaskId']/option[value()='4782']").click()

#assert "Your login attempt was not successful. Please try again." not in driver.page_source

Save = driver.find_element_by_id('ctl00_ctl00_ContentPlaceHolderBody_ContentPlaceHolderBody_CtlAccountEmployeeTimeEntryDayView1_btnSave')
Save.send_keys(Keys.ENTER)

driver.close()