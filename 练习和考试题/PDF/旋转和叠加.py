import PyPDF2


minutesFile=open('D:\\Python\\快速上手配套资料\\9.源代码\\meetingminutes.pdf','rb')
watermarkFile=open('D:\\Python\\快速上手配套资料\\9.源代码\\watermark.pdf','rb')
pdfreader1=PyPDF2.PdfReader(minutesFile)
pdfreader2=PyPDF2.PdfReader(watermarkFile)

page1=pdfreader1.pages[0]
page1.rotate(90)

page1.merge_page(pdfreader2.pages[0])

pdfwriter=PyPDF2.PdfWriter()
pdfwriter.add_page(page1)

outputfile=open('./watermerge.pdf','wb')
pdfwriter.write(outputfile)
outputfile.close()
minutesFile.close()
watermarkFile.close()

