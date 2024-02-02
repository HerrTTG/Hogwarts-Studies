import PyPDF2

f=open('D:\\Python\\快速上手配套资料\\9.源代码\\encrypted.pdf','rb')
pdfreader=PyPDF2.PdfReader(f)
if pdfreader.is_encrypted:
    #判断是否加密，是则用密码解密。否则会报错File has not been decrypted
    pdfreader.decrypt('rosebud')
pdfobject=pdfreader.pages[0]
print(pdfobject.extract_text())