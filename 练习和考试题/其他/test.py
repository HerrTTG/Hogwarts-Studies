import os.path,shutil


def select_copy(folder):
    absfolder=os.path.abspath(folder)
    newfolder=os.path.join(absfolder,'pybackup')

    for currentfolder,subfolder,filenames in os.walk(absfolder):
        print('Checking in {} ...'.format(currentfolder))

        for filename in filenames:
            if not filename.endswith('.py'):
                continue
            else:
                if not os.path.exists(newfolder):
                    os.mkdir(newfolder)
                shutil.copy(os.path.join(currentfolder,filename),newfolder)
    print('Backup py files in {}'.format(newfolder))

select_copy('D:\\Python\\练习和考试题\\文件处理')