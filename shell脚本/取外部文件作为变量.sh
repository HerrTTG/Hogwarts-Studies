#!/usr/bin/ksh
if [ `echo "$0" |grep -c "/"` -gt 0 ];then
    cd ${0%/*}
fi
interval=$1
date=`date -d "-${interval} day" +%Y%m%d`

for line in `cat data_clean.properties | awk -F "=" '{print $2}'`
#ȡ�ļ��ڵ�������forѭ����ֵ������line
#more data_clean.properties
#FILE_EXTRACT_DIR=/datas/bdi/datastore/etldata
#FILE_EXTRACT_DIR_TEMP=/datas/bdi/datastore/etldata/temp
#EXTRACT_LoanInfo_DIR=/datas/bdi/datastore/SysAccuLoanInfo
do
        echo "Begin to clean ${line} before ${date}"
        find ${line} -mtime +${interval} -type f -exec rm -f {} \;
done




