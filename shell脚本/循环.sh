#!/bin/bash
#循环对输入的参数进行打印 
# $@是一个一个打印
# $*是合并打印

for i in "$@"
do

echo "liuyuzhen is $i"
done 


for s in "$*"
do

echo "liuyuzhen is $s"
done 


#输出#
#liuyuzhen is fupo#
#liuyuzhen is dalao#
#liuyuzhen is fupo dalao#