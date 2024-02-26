#!/usr/bin/ksh
if [ `echo "$0" |grep -c "/"` -gt 0 ];then
    cd ${0%/*}
fi
interval=$1
date=`date -d "-${interval} day" +%Y%m%d`

for line in `cat data_clean.properties | awk -F "=" '{print $2}'`
#取文件内的内容用for循环赋值给变量line
#more data_clean.properties
#FILE_EXTRACT_DIR=/data/bdi/datastore/etldata
#FILE_EXTRACT_DIR_TEMP=/data/bdi/datastore/etldata/temp
#EXTRACT_LoanInfo_DIR=/data/bdi/datastore/SysAccuLoanInfo
do
        echo "Begin to clean ${line} before ${date}"
        find ${line} -mtime +${interval} -type f -exec rm -f {} \;
done




