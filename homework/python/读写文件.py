'''
作业要求
编写一个Python程序，将一些文本内容写入到文件中，并且能够从文件中读取内容并显示出来
'''


import os

path=os.getcwd()

def write(filename='./abc.txt'):
    p='''
    我在写作业
    作业好难
    '''
    f=open(filename,'w',encoding='utf-8')
    f.write(p)
    f.close()

def read(filename):
    try:
        if os.path.isfile(filename):
            with open(filename,'r',encoding='utf-8') as fo:
                print(fo.readlines())
                #print(fo.read())
        else:
            raise Exception('文件不存在')
    except:
        print('文件读取失败')
        f = open(filename, 'w', encoding='utf-8')
        f.write('原文件不存在,请检查')
        f.close()


if __name__=='__main__':
    write()
    read('abc.txt')
