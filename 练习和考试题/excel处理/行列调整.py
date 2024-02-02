import openpyxl

wb=openpyxl.Workbook()
sheet=wb.active
sheet['A1'].value='Hello world'
sheet['B2'].value='Help'


sheet.row_dimensions[1].height = 20

sheet.column_dimensions['B'].width = 15


wb.save('./行列调整.xlsx')