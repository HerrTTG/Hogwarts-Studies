
import openpyxl

wb = openpyxl.load_workbook('./produceSales.xlsx')
sheet = wb['Sheet']

sheet.freeze_panes='A2'
wb.save('./冻结ProduceSales.xlsx')