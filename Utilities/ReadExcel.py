import xlrd

class ReadExcel:
        """ This class to read data from excel sheets """


def get_data(self,file_path,sheetname):
        # create an empty list to store rows
        rows = []
        # open the specified Excel spreadsheet as workbook
        book = xlrd.open_workbook(file_path,encoding_override='utf8')
        # get the first sheet
        sheet = book.sheet_by_name(sheetname)
        # iterate through the sheet and get data from rows in list
        for row_idx in range(1, sheet.nrows):
            rows.append(list(sheet.row_values(row_idx, 0, sheet.ncols)))
        return rows
