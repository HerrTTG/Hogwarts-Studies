#! python3
# backupToZip.py
# Copies an entire folder and its contents into
# a zip file whose filename increments.

import zipfile, os

def backupToZip(folder):
    # Backup the entire contents of "folder" into a zip file.

    folder = os.path.abspath(folder) # Make sure folder is absolute

    # Figure out the filename this code should used based on what
    # files already exist.
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            #检查文件名是否存在，存在就不满足跳出break的条件，执行下面的number+1来确保文件名不重复
            break
        number = number + 1

    # Create the zip file.
    print('Creating %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        # Add the current folder to the zip file.
        backupZip.write(foldername)

        # Add all the files in this folder to the zip file.
        for filename in filenames:
            if filename.endswith('.zip'):
                continue # Don't backup the backup zip files.
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done.')


backupToZip('D:\\Python\\练习和考试题\\文件处理')