#!/bin/bash
cat <<EOF          
"*****************************************************************"
"*Powered By HZY0000111175                                       *"
"*Version:2.0                                                    *"
"*Warning: Please obtain permission before executing the script! *"
"*****************************************************************"
EOF

#Waring������ִ�д˽ű����������ؼ���Ӧ�ı��������һ�ÿͻ������������Զ���ִ�д˽ű��������һ��ʱ���ļ������ƶ�����Ҫ����SCP����Կ��
#�汾˵����2.0�汾�޸��˲���չʾ�߼���������־�洢�� 
#����˵�����˽ű�������A IPѡ��һ�����һ��ʱ��Ļ����ļ����п����ƶ���B IP��
#TIP:SCP�������������·�������ʵ���������


#���±���ֻ��������Ķ�һ��ʱ���ļ������ƶ�ʱ����ʵ����������޸�
maxtimes=15
startday=01
month=03
year=2023

#���ݾֵ�ʵ���������
path='/onip/cdr/ppscdr4qimport/bak/'
file1='rec*.unl'
file2='datas*.unl'
file3='sms*.unl'
file4='vou*.unl'


##################################################################

rm -f  mvfile.log
unset flag
times=1


if [ $# -gt 0 ];
	then 
	
	#�ֶ�ִ��ָ����һ�죬$1Ϊ�ű�������ĵ�һ����� ��ʽ:sh mvfile.sh YYYYMMDD	
  echo "Manully exeuct" $1
  echo "Please confirm(yes or no):"
  read flag

  if [[ $flag = "yes" ]]
	 then 
   echo "Begin to mv" $file1
   scp -r -v cbpapp@192.168.51.47:$path/$1/$file1  /datas/bdi/datastore/invcdr/pps/normal |& grep -v ^debug >> mvfile.log
   echo $?
   echo "*************************************************************"  >> mvfile.log
  
   echo "Begin to mv" $file2
     scp -r -v cbpapp@192.168.51.47:$path/$1/$file2  /datas/bdi/datastore/invcdr/pps/normal |& grep -v ^debug >> mvfile.log
     echo $?
     echo "*************************************************************"  >> mvfile.log

   echo "Begin to mv" $file3
     scp -r -v  cbpapp@192.168.51.47:$path/$1/$file3  /datas/bdi/datastore/invcdr/pps/normal |& grep -v ^debug >> mvfile.log
     echo $?
     echo "*************************************************************"  >> mvfile.log

  echo "Begin to mv" $file4
     scp -r -v  cbpapp@192.168.51.47:$path/$1/$file4  /datas/bdi/datastore/invcdr/pps/normal |& grep -v ^debug >> mvfile.log
     echo $?
     echo "*************************************************************"  >> mvfile.log
     
     
   echo 'Manully exeuct Done'
   exit 0
               	
   else 
   	exit 1
  fi

else 
	
	 if [ ${#month} -lt 2 ]
     	then 
     	 month="0$month"
     fi
     
     if [ ${#startday} -lt 2 ]
     	then 
     	 startday="0$startday"
     fi
	
	echo "Auto exeuct start from"  $year$month$startday "Total" $maxtimes "days before the end of a month."
	echo "Please confirm(yes or no):"
  read flag

  if [[ $flag = "yes" ]]
	 then 
	 
    while [ $times -le $maxtimes ] && [ $startday -le 31 ]
    do
    
     if [ ${#month} -lt 2 ]
     	then 
     	 month="0$month"
     fi
     
     if [ ${#startday} -lt 2 ]
     	then 
     	 startday="0$startday"
     fi
     
     echo "Begin to mv" /$year$month$startday/$file1
     echo "start move $year$month$startday/$file1" >> mvfile.log
     scp -r -v cbpapp@192.168.51.47:$path/$year$month$startday/$file1  /datas/bdi/datastore/invcdr/pps/normal |& grep -v ^debug >> mvfile.log
     echo $?
     echo "*************************************************************"  >> mvfile.log
     
     
     echo "Begin to mv" /$year$month$startday/$file2
     echo "start move $year$month$startday/$file2" >> mvfile.log
     scp -r -v cbpapp@192.168.51.47:$path/$year$month$startday/$file2 /datas/bdi/datastore/invcdr/pps/normal |& grep -v ^debug >> mvfile.log
     echo $?	
     echo "*************************************************************" >> mvfile.log
     
     
     echo "Begin to mv" /$year$month$startday/$file3
     echo "start move $year$month$startday/$file3" >> mvfile.log
     scp -r -v cbpapp@192.168.51.47:$path/$year$month$startday/$file3  /datas/bdi/datastore/invcdr/pps/normal |& grep -v ^debug >> mvfile.log
     echo $?
     echo "*************************************************************" >> mvfile.log

     
     echo "Begin to mv" /$year$month$startday/$file4
     echo "start move $year$month$startday/$file4" >> mvfile.log
     scp -r -v cbpapp@192.168.51.47:$path/$year$month$startday/$file4  /datas/bdi/datastore/invcdr/pps/normal |& grep -v ^debug >> mvfile.log
     echo $?
     echo "*************************************************************" >> mvfile.log
     
     
     times=`expr $times + 1`
     startday=`expr $startday + 1`
     
     done 
     echo 'Auto exeuct Done'
     exit 0
    
    else
    	exit 1
    fi	

fi	