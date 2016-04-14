from selenium import webdriver

driver = webdriver.Firefox()

driver.get('http://10.1.22.67/Jamaica/utilisateurs/enregistrement.php')
driver.implicitly_wait(30)

import xlrd
import unittest

class Regestration(unittest.TestCase):
    def InsertData(self):
        file_location = 'C:\Info.xlsx'
        workbook = xlrd.open_workbook(file_location)
        workbook = xlrd.open_workbook('C:\Info.xlsx')
        inputfields = []
        #worksheet = workbook.sheet_by_indix(0)
        worksheet = workbook.sheet_by_name('Sheet1')
        for current_row in range(worksheet.nrows):
            inputfields.append(worksheet.cell_value(current_row,0))
        print(inputfields)
"""  Email_text = worksheet.row(current_row)[0]
    Nickname_text = worksheet.row(current_row)[0][1]
    FirstName_text = worksheet.row(current_row)[0][2]
    SurName_text = worksheet.row(current_row)[0][3]
    Company_text = worksheet.row(current_row)[0][4]
    Phone_text = worksheet.row(current_row)[0][5]
    Mobile_text = worksheet.row(current_row)[0][6]
    Address_text = worksheet.row(current_row)[0][7]
    Zipcode_text = worksheet.row(current_row)[0][8]
    Town_text = worksheet.row(current_row)[0][9]"""
#import xlrd
#workbook = xlrd.open_workbook("people.xls")
#worksheet = workbook.sheet_by_name('Sheet1')

Email = driver.find_element_by_id('email')
Email.send_keys(inputfields[0])

Nickname = driver.find_element_by_id('pseudo')
Email.send_keys(inputfields[1])

FirstName = driver.find_element_by_id('prenom')
Email.send_keys(inputfields[2])

Surname = driver.find_element_by_id('nom_famille')
Surname.send_keys(inputfields[3])

Company = driver.find_element_by_id('societe')
Company.send_keys(inputfields[4])

Phone = driver.find_element_by_id('telephone')
Phone.send_keys(inputfields[5])

Mobile = driver.find_element_by_id('societe')
Mobile.send_keys(inputfields[6])

Address = driver.find_element_by_id('adresse')
Address.send_keys(inputfields[7])

Zipcode = driver.find_element_by_id('code_postal')
Zipcode.send_keys(inputfields[8])

Town = driver.find_element_by_id('ville')
Town.send_keys(inputfields[9])

driver.find_elements_by_xpath("/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div/form/div[2]/div[1]/span[2]/input[3]")[0].click #for Mr #for radio button but i can't find the xpath or css from ie

#driver.find_element_by_xpath("//select[@name='fonction']/option[value()='leader']").click() #dropdown list to select leader but we need it datadriven
select_capacity = driver.find_element_by_id("fonction")
select_capacity.send_keys(str("Manager"))

#driver.find_elements_by_xpath(".//input[@name='newsletter' and @value='1']")[0].click #for 1st one #for selections but i can't find the xpath or css from ie
select_Country = driver.find_element_by_id("pays")
select_Country.send_keys(str("Egypt"))

#driver.find_elements_by_xpath(".//input[@name='commercial' and @value='1']")[0].click #for 2nd one #for selections but i can't find the xpath or css from ie
select_Howdoyouknowourwebsite = driver.find_element_by_id("origin")
select_Howdoyouknowourwebsite.send_keys(str("Other"))

FirstSelection = driver.find_element_by_id('newsletter').click() #should be by xpath or css
#FirstSelection.send_keys(Keys.ENTER)

SecondSelection = driver.find_element_by_id('commercial').click() #should be by xpath or css
#SecondSelection.send_keys(Keys.ENTER)

#<select name="fonction" class="form-control" id="fonction">
#				<option value="">Choose...</option>
#				<option value="leader">Leader</option><option value="manager">Manager</option><option selected="selected" value="employee">Employee</option>
#			</select>


#<input name="newsletter" type="checkbox" value="1">




driver.close()