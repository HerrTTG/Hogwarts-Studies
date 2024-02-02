import pathlib

myFiles = ['123.txt', 'detail.csv', 'invite.docx']

for filename in myFiles:
    print(pathlib.Path(r'd:\User\Python', filename))

homeFloder=pathlib.Path('C:/user/AI')
subFloder=pathlib.Path('spam')
print(str(homeFloder/subFloder))

