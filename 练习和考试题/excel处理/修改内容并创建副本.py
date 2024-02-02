import openpyxl
wb = openpyxl.load_workbook('./censuspopdata.xlsx')
sheet=wb.active
sheet.title='Test copy'
#修改任意内容
wb.save('./censuspopdata_copy.xlsx')