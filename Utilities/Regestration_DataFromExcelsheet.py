import xlrd
import os.path
import unittest


class ReadData:
    """ This class to read data from excel sheets """

    def InsertData(self):
        file_location = 'C:\Info.xlsx'
        workbook = xlrd.open_workbook(file_location)
        workbook = xlrd.open_workbook('C:\Info.xlsx')
        inputfields = []
        worksheet = workbook.sheet_by_name('Sheet1')
        for current_row in range(worksheet.nrows):
            inputfields.append(worksheet.cell_value(current_row,0))
        print(inputfields)