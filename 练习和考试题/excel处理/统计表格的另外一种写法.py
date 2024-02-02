
import openpyxl, pprint
print('Opening workbook...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet =wb.active
countyData = {}
print('Reading rows...')
max_row=sheet.max_row
sheet['B2':'D'+str(max_row)]
#sheet['B2':'D'+str(max_row)本身就是生成一个由每一行对象组成的元组的元组((b2,c2,d2）,(b3,c3,d3)....)

for row in sheet['B2':'D'+str(max_row)]:
    #row是每一行的一个元组，这里元组内有三个对象元素分别是 b2c2d2
    object1,object2,object3 =row
    state=object1.value
    county=object2.value
    pop =object3.value

    # Make sure the key for this state exists.
    countyData.setdefault(state, {})
    # Make sure the key for this county in this state exists.
    countyData[state].setdefault(county, {})
    #countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})

    # Each row represents one census tract, so increment by one.
    countyData[state][county]['tracts']=countyData[state][county].get('tracts',0)+1
    # Increase the county pop by the pop in this census tract.
    countyData[state][county]['pop']=countyData[state][county].get('pop',0)+int(pop)

# Open a new text file and write the contents of countyData to it.
print('Writing results...')
resultFile = open('./census2010.txt', 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('Done.')
