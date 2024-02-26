#!/bin/bash


#行中有空属性会出问题，被数组定义为元素分割符#

arr=(`awk 'BEGIN{RS = "|" ; ORS = " " }{print $0}' /onip/cdr/output/errorrecharge_107_149_00101_20221201110446_20877.dat`)

for i in ${!arr[*]}
do 
   echo "$i : ${arr[$i]} " 
  done 
 
