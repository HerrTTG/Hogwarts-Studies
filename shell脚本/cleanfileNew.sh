#!/bin/bash
#"*****************************************************************"
#"*Powered By HZY0000111175                                       *"
#"*Version:2.1                                                    *"
#"*Warning: Please obtain permission before executing the script! *"
#"*****************************************************************"

#Waring������ִ�д˽ű����������ؼ���Ӧ�ı��������һ�ÿͻ�������
#�汾˵����2.0�汾��������־��ӡ���ɷ���crontab�Զ������к���ճ����ά����
#�汾˵����2.1�汾ִ�н����־��Ϊÿ��������һ�Σ���������ִ�н������õ�������
#����˵�����˽ű�����ɾ��MED��cbpapp�ƶ���BDI�Ķ��໰����������4��BDI��Ҫ�Ļ�����

path='/data/bdi/datastore/invcdr/pps/normal'

#delete the MED mv in path file ,except file1~file4#
file1='rec.*.unl'
file2='data.*.unl'
file3='sms.*.unl'
file4='vou.*.unl'

#echo "$path/$file1|$path/$file2|$path/$file3|$path/$file4"

Dday=DATE=10#$(date +%d)

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


