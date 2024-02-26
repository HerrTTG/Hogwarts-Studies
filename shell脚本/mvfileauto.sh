#!/bin/bash

rm mvfile.log

times=1
startday=01
month=01
year=2023

path='/onip/cdr/ppscdr4qimport/bak/'
file1='rec*.unl'
file2='data*.unl'
file3='sms*.unl'
file4='vou*.unl'


while [ $times -le 10 ] && [ $startday -le 31 ]
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
  echo "*************************************************************"  >> mvfile.log
  echo $?	
  
  echo "Begin to mv" /$year$month$startday/$file2
  echo "start move $year$month$startday/$file2" >> mvfile.log
  scp -r -v cbpapp@192.168.51.47:$path/$year$month$startday/$file2 /data/bdi/datastore/invcdr/pps/normal |& grep -v ^debug >> mvfile.log
  echo "*************************************************************" >> mvfile.log
  echo $?	
  
  echo "Begin to mv" /$year$month$startday/$file3
  echo "start move $year$month$startday/$file3" >> mvfile.log
  scp -r -v cbpapp@192.168.51.47:$path/$year$month$startday/$file3  /data/bdi/datastore/invcdr/pps/normal |& grep -v ^debug >> mvfile.log
  echo "*************************************************************" >> mvfile.log
  echo $?	
  
  echo "Begin to mv" /$year$month$startday/$file4
  echo "start move $year$month$startday/$file4" >> mvfile.log
  scp -r -v cbpapp@192.168.51.47:$path/$year$month$startday/$file4  /data/bdi/datastore/invcdr/pps/normal |& grep -v ^debug >> mvfile.log
  echo "*************************************************************" >> mvfile.log
  echo $?	
  
  
  times=`expr $times + 1`
  startday=`expr $startday + 1`
  
done 

