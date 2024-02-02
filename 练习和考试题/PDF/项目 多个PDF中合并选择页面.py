import PyPDF2,os

path=os.path.abspath('D:\\Python\\快速上手配套资料\\9.源代码\\')
pdflist=[]
for filename in os.listdir('D:\\Python\\快速上手配套资料\\9.源代码\\'):
    if filename.endswith('.pdf'):
        pdflist.append(filename)

pdflist.sort()

pdfwriter=PyPDF2.PdfWriter()

for filename in pdflist:
    readfile=open(path+'\\'+filename,'rb')
    pdfreader=PyPDF2.PdfReader(readfile)
    if pdfreader.is_encrypted is True:
        pdfreader.decrypt('rosebud')
    for page in pdfreader.pages[1:]:
        pdfwriter.add_page(page)
    readfile.close()

outputfile=open('./allminutes.pdf','wb')
pdfwriter.write(outputfile)
outputfile.close()





