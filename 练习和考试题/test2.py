ls=[['a','123'],['a','123'],['a','123']]
fw=open("test.csv","w")
fw.seek(0)
for item in ls :
	fw.write(','.join(item)+'\n')