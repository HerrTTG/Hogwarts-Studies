#!/bin/bash


#�����п����Ի�����⣬�����鶨��ΪԪ�طָ��#

arr=(`awk 'BEGIN{RS = "|" ; ORS = " " }{print $0}' /onip/cdr/output/errorrecharge_107_149_00101_20221201110446_20877.dat`)

for i in ${!arr[*]}
do 
   echo "$i : ${arr[$i]} " 
  done 
 
