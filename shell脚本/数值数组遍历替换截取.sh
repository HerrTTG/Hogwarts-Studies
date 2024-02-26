#!/bin/bash

#赋值的两种方式

arr=("haizhenyu" "liuyuzhen")
arr[2]='dongxinwang'



##遍历数组输出 下标：对应的元素值

for i in ${!arr[*]}
do 
  echo $i:${arr[$i]}
done 


#下标元素直接替换 dongxinwang 被替换为qianyang

arr[2]='qianyang'


#输出1以后的所有元素#

echo ${arr[@]:1}

#输出0往后的2个元素

echo ${arr[@]:0:2}



##输出
#0:haizhenyu#
#1:liuyuzhen#
#2:dongxinwang#
#liuyuzhen qianyang#
#haizhenyu liuyuzhen#