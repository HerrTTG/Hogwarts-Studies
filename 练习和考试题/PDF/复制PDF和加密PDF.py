import PyPDF2

pdffile1=open('D:\\Python\\快速上手配套资料\\9.源代码\\meetingminutes.pdf','rb')
pdffile2=open('D:\\Python\\快速上手配套资料\\9.源代码\\meetingminutes2.pdf','rb')
pdfread1=PyPDF2.PdfReader(pdffile1)
pdfread2=PyPDF2.PdfReader(pdffile2)
pdfwriter=PyPDF2.PdfWriter()

for pageNum in range(len(pdfread1.pages)):
    pageobj=pdfread1.pages[pageNum]
    pdfwriter.add_page(pageobj)

for pageNum in range(len(pdfread1.pages)):
    pageobj=pdfread2.pages[pageNum]
    pdfwriter.add_page(pageobj)

    pdfoutputfile=open('./combinedminutes.pdf','wb')
    pdfwriter.encrypt('rosebud')
    pdfwriter.write(pdfoutputfile)

pdffile1.close()
pdffile2.close()
pdfoutputfile.close()
