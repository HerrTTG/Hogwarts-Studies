#!/bin/bash
#���ݾ���·���µ��ļ�������·��#
#����1Ϊ��� ��Ҫ���ݵ�·��#

if [ $# -ne 1 ]
then
echo "Incorrect number of parameters! You should enter a parameter as the name of the archive directory"
exit
fi

# �Ӳ����л�ȡĿ¼����#
if [ ! -d $1 ]
	then 
	echo "The archive path does not exist"
	exit	
fi 


DIR_NAME=$(basename $1)
DIR_PATH=$(dirname $1)

# ��ȡ��ǰ����#
DATE=$(date +%y%m%d)
# �������ɵĹ鵵�ļ�����#
TAR_NAME=Archiv_${DIR_NAME}_$DATE.tar.gz
TAR_DEST=$1/$TAR_NAME
# ��ʼ�鵵Ŀ¼�ļ�#x`
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