import openpyxl

wb=openpyxl.load_workbook('./example.xlsx')
sheet1=wb.active

for obj in list(sheet1.columns)[1]:
    print(obj.coordinate,obj.value)
#要将.columns或者.rows 转为list类型。list中的每一个元素代表一行或者一列的全部对象组成的元组
#如在此处为[(a1,a2,a3,a4,a5,a6,a7),(b1,b2,b3,b4,b5,b6,b7),(c1,c2,c3,c4,c5,c6,c7)]
#list(sheet1.columns)[1] 表示取第二个元素 (b1,b2,b3,b4,b5,b6,b7) for循环遍历其中每一个对象给obj
