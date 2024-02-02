import openpyxl
wb=openpyxl.Workbook()
sheet=wb.active

for i in range(1,11):
    sheet['A'+str(i)]='I'+str(i)
refobj=openpyxl.chart.Reference(sheet,1,1,1,10)
seriesobj=openpyxl.chart.Series(refobj,title='First series')

chartobj=openpyxl.chart.BarChart()
chartobj.title='My chart'
chartobj.append(seriesobj)

sheet.add_chart(chartobj,'C5')
wb.save('./图表简单示例.xlsx')