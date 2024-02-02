#遍历目录寻找大文件，并做移动到回收站的操作

import os.path,send2trash


def checkbigfile(folder):
    absfolder=os.path.abspath(folder)

    ls={}
    for currentfolder,subfolder,filenames in os.walk(absfolder):
        print('Checking in {} ...'.format(currentfolder))
        for filename in filenames:
            if os.path.getsize(os.path.join(currentfolder,filename))>=104857600:
               ls[os.path.join(currentfolder,filename)]=os.path.getsize(os.path.join(currentfolder,filename))

    if ls !={}:
        for item in ls:
            print('{}       {:.2f}MB'.format(item,ls[item]/1024/1024))
            #send2trash.send2trash(item)

    else:
        print('{} not have such file great than 100MB'.format(absfolder))

checkbigfile('D:\\backup')