#!/bin/bash
cat <<EOF          
"*****************************************************************"
"*Powered By HZY0000111175                                       *"
"*Version:2.0                                                    *"
"*Warning: Please obtain permission before executing the script! *"
"*****************************************************************"
EOF

#Waring：生产执行此脚本需谨慎！务必检查对应的变量，并且获得客户审批！并且自动化执行此脚本尤其针对一段时间文件进行移动，需要配置SCP免密钥。
#版本说明：2.0版本修改了部分展示逻辑。增加日志存储。 
#功能说明：此脚本用来从A IP选择一天或者一段时间的话单文件进行拷贝移动到B IP。
#TIP:SCP的所有输入输出路径需根据实际情况配置


#以下变量只针对批量的对一段时间文件进行移动时根据实际情况进行修改
maxtimes=15
startday=01
month=03
year=2023

#根据局点实际情况配置
path='/onip/cdr/ppscdr4qimport/bak/'
file1='rec*.unl'
file2='data*.unl'
file3='sms*.unl'
file4='vou*.unl'


##################################################################

rm -f  mvfile.log
unset flag
times=1


if [ $# -gt 0 ];
	then 
	
	#手动执行指定的一天，$1为脚本外输入的第一个入参 格式:sh mvfile.sh YYYYMMDD	
  echo "Manully exeuct" $1
  echo "Please confirm(yes or no):"
  read flag

  if [[ $flag = "yes" ]]
	 then 
   echo "Begin to mv" $file1
   scp -r -v cbpapp@192.168.51.47:$path/$1/$file1  /data/bdi/datastore/invcdr/pps/normal |& grep -v ^debug >> mvfile.log
   echo $?
   echo "*************************************************************"  >> mvfile.log
  
   echo "Begin to mv" $file2
     scp -r -v cbpapp@192.168.51.47:$path/$1/$file2  /data/bdi/datastore/invcdr/pps/normal |& grep -v ^debug >> mvfile.log
     echo $?
     echo "*************************************************************"  >> mvfile.log

   echo "Begin to mv" $file3
     scp -r -v  cbpapp@192.168.51.47:$path/$1/$file3  /data/bdi/datastore/invcdr/pps/normal |& grep -v ^debug >> mvfile.log
     echo $?
     echo "*************************************************************"  >> mvfile.log

  echo "Begin to mv" $file4
     scp -r -v  cbpapp@192.168.51.47:$path/$1/$file4  /data/bdi/datastore/invcdr/pps/normal |& grep -v ^debug >> mvfile.log
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
     scp -r -v cbpapp@192.168.51.47:$path/$year$month$startday/$file1  /data/bdi/datastore/invcdr/pps/normal |& grep -v ^debug >> mvfile.log
     echo $?
     echo "*************************************************************"  >> mvfile.log
     
     
     echo "Begin to mv" /$year$month$startday/$file2
     echo "start move $year$month$startday/$file2" >> mvfile.log
     scp -r -v cbpapp@192.168.51.47:$path/$year$month$startday/$file2 /data/bdi/datastore/invcdr/pps/normal |& grep -v ^debug >> mvfile.log
     echo $?	
     echo "*************************************************************" >> mvfile.log
     
     
     echo "Begin to mv" /$year$month$startday/$file3
     echo "start move $year$month$startday/$file3" >> mvfile.log
     scp -r -v cbpapp@192.168.51.47:$path/$year$month$startday/$file3  /data/bdi/datastore/invcdr/pps/normal |& grep -v ^debug >> mvfile.log
     echo $?
     echo "*************************************************************" >> mvfile.log

     
     echo "Begin to mv" /$year$month$startday/$file4
     echo "start move $year$month$startday/$file4" >> mvfile.log
     scp -r -v cbpapp@192.168.51.47:$path/$year$month$startday/$file4  /data/bdi/datastore/invcdr/pps/normal |& grep -v ^debug >> mvfile.log
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