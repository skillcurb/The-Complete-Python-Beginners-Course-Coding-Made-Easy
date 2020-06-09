#load the library to import data from excel workbook
import xlrd

book = xlrd.open_workbook('example1.xlsx')

print(book.nsheets)

print(book.sheet_names())

first_sheet = book.sheet_by_index(0)
print(first_sheet.nrows)

print(first_sheet.ncols)

print(first_sheet.row_values(1))

for i in range(first_sheet.nrows):
    print(first_sheet.row_values(i))

print(first_sheet.cell_value(2,1))