#!/bin/bash
#"*****************************************************************"
#"*Powered By HZY0000111175                                       *"
#"*Version:2.1                                                    *"
#"*Warning: Please obtain permission before executing the script! *"
#"*****************************************************************"

#Waring：生产执行此脚本需谨慎！务必检查对应的变量，并且获得客户审批！
#版本说明：2.0版本增加了日志打印，可方便crontab自动化运行后的日常检查维护。
#版本说明：2.1版本执行结果日志改为每个月清理一次，当月所有执行结果都会得到保留。
#功能说明：此脚本用来删除MED从cbpapp移动到BDI的多余话单，仅保留4种BDI需要的话单。

path='/data/bdi/datastore/invcdr/pps/normal'

#delete the MED mv in path file ,except file1~file4#
file1='rec.*.unl'
file2='data.*.unl'
file3='sms.*.unl'
file4='vou.*.unl'

#echo "$path/$file1|$path/$file2|$path/$file3|$path/$file4"

Dday=DATE=$(date +%d)

if [[ $Dday -eq 01 ]]
	then
	#echo $Dday 
	rm -f /data/bdi/datastore/data_clean/log/cleanfile.log
	fi 

delist=`ls $path/*.unl | egrep -wv "$path/$file1|$path/$file2|$path/$file3|$path/$file4"`
decount=`ls $path/*.unl | egrep -wv "$path/$file1|$path/$file2|$path/$file3|$path/$file4" | wc -l`


echo "Excute delete..." `date` >> /data/bdi/datastore/data_clean/log/cleanfile.log
echo 'Delete list save in /data/bdi/datastore/data_clean/log/cleanlist.log' >> /data/bdi/datastore/data_clean/log/cleanfile.log
echo "Delete list count:"$decount >> /data/bdi/datastore/data_clean/log/cleanfile.log


echo `date` 'Delete list follow:' > /data/bdi/datastore/data_clean/log/cleanlist.log
echo $delist >> /data/bdi/datastore/data_clean/log/cleanlist.log
rm -f $delist

if [[ $? -eq 0 ]]
then
        echo "Excute successed" >> /data/bdi/datastore/data_clean/log/cleanfile.log
else
        echo "Excute failed" >> /data/bdi/datastore/data_clean/log/cleanfile.log
fi

echo "*************************************************************" >> /data/bdi/datastore/data_clean/log/cleanfile.log


