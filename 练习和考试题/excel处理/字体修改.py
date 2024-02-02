import openpyxl
from openpyxl.styles import  Font

wb=openpyxl.Workbook()
sheet=wb.active

myfon=Font(size=24,italic=True)
sheet['A1'].font=myfon
sheet['A1'].value='Hello world'
wb.save('./字体修改.xlsx')