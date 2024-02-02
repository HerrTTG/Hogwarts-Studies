import openpyxl

wb=openpyxl.Workbook()

sheet=wb.active
sheet.title='Test'
sheet['A1']='Test'
sheet['B2']='HZY'
wb.save('./test.xlsx')