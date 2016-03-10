from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

driver.get('http://10.1.22.67/Jamaica/utilisateurs/enregistrement.php')
driver.implicitly_wait(30)

import xlrd
workbook = xlrd.open_workbook('C://Info.xlsx')
#workbook = xlrd.open_workbook("people.xls")
worksheet = workbook.sheet_by_name('Sheet1')
for current_row in range(worksheet.nrows):
    Email_text = worksheet.row(current_row)[0]
    Nickname_text = worksheet.row(current_row)[1]
    FirstName_text = worksheet.row(current_row)[2]
    SurName_text = worksheet.row(current_row)[3]
    Company_text = worksheet.row(current_row)[4]
    Phone_text = worksheet.row(current_row)[5]
    Mobile_text = worksheet.row(current_row)[6]
    Address_text = worksheet.row(current_row)[7]
    Zipcode_text = worksheet.row(current_row)[8]
    Town_text = worksheet.row(current_row)[9]

#import xlrd
#workbook = xlrd.open_workbook("people.xls")
#worksheet = workbook.sheet_by_name('Sheet1')

Email = driver.find_element_by_id('email')
Email.send_keys(Email_text)

Nickname = driver.find_element_by_id('pseudo')
Email.send_keys(Nickname_text)

FirstName = driver.find_element_by_id('prenom')
Email.send_keys(Nickname_text)

Surname = driver.find_element_by_id('nom_famille')
Surname.send_keys(SurName_text)

Company = driver.find_element_by_id('societe')
Company.send_keys(Company_text)

Phone = driver.find_element_by_id('telephone')
Phone.send_keys(Phone_text)

Mobile = driver.find_element_by_id('societe')
Mobile.send_keys(Mobile_text)

Address = driver.find_element_by_id('adresse')
Address.send_keys(Address_text)

Zipcode = driver.find_element_by_id('code_postal')
Zipcode.send_keys(Zipcode_text)

Town = driver.find_element_by_id('ville')
Town.send_keys(Town_text)

browser.find_elements_by_xpath(".//input[@type='radio' and @value='M.']")[0].click #for Mr #for radio button but i can't find the xpath or css from ie

browser.find_element_by_xpath("//select[@name='fonction']/option[value()='leader']").click() #dropdown list to select leader but we need it datadriven

browser.find_elements_by_xpath(".//input[@name='newsletter' and @value='1']")[0].click #for 1st one #for selections but i can't find the xpath or css from ie

browser.find_elements_by_xpath(".//input[@name='commercial' and @value='1']")[0].click #for 2nd one #for selections but i can't find the xpath or css from ie

Change = driver.find_element_by_class('btn btn-primary btn-lg') #should be by xpath or css
Change.send_keys(Keys.ENTER)

#<select name="fonction" class="form-control" id="fonction">
#				<option value="">Choose...</option>
#				<option value="leader">Leader</option><option value="manager">Manager</option><option selected="selected" value="employee">Employee</option>
#			</select>


#<input name="newsletter" type="checkbox" value="1">




driver.close()