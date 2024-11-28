import  openpyxl

wb=openpyxl.load_workbook('./example.xlsx')

sheet1=wb['Sheet1']
# sheet1['A1':'C3'] 是一个元组
#这个元组包含三个元组，每一个元组代表一行。每一组中包含指定区域的一行对象。即((A1,B1,C1),(A2,B2,C2),(A3,B3,C3))

for row in sheet1['A1':'C3']:
    #每一行的单独元组
    for object in row:
        #每一个对象
        print(object.coordinate,object.value)
    print('--- END OF ROW ---')
