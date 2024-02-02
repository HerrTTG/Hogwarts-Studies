import  os,zipfile
from pathlib import Path

exampleZip=zipfile.ZipFile('D:\\Python\\练习和考试题\\文件处理\\example.zip')
#创建对象first
print(exampleZip.namelist())
#namelist方法将返回zip文件中包含的所有文件和文件夹的字符串列表

spamInfo=exampleZip.getinfo('spam.txt')
#namelist中的元素可以传递给新的对象spamInfo的getinfo方法

print(spamInfo.file_size)
print(spamInfo.compress_size)

exampleZip.close()
