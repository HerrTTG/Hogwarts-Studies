#!/bin/bash
#备份绝对路径下的文件，包含路径#
#参数1为入参 需要备份的路径#

if [ $# -ne 1 ]
then
echo "Incorrect number of parameters! You should enter a parameter as the name of the archive directory"
exit
fi

# 从参数中获取目录名称#
if [ ! -d $1 ]
	then 
	echo "The archive path does not exist"
	exit	
fi 


DIR_NAME=$(basename $1)
DIR_PATH=$(dirname $1)

# 获取当前日期#
DATE=$(date +%y%m%d)
# 定义生成的归档文件名称#
TAR_NAME=Archiv_${DIR_NAME}_$DATE.tar.gz
TAR_DEST=$1/$TAR_NAME
# 开始归档目录文件#x`
echo "Start Archiving..."
echo " "
tar -zcvf $TAR_DEST  $1/*
if [ $? -eq 0 ]
then
echo " "
echo "Archiving success! "
echo "The archive file is: $TAR_DEST"
echo " "
else
echo "Archiving problems! "
echo " "
fi
exit