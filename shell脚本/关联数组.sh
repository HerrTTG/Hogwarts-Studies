#!/bin/bash
  
#关联数组定义必不可少，不定义默认为数值数组#
declare -A ass_array1

#一次性批量数组赋值#
ass_array1=([contry]='China' [height]=180 [weight]=75)

#单下标追加赋值#
ass_array1[name]="zhangsan"
ass_array1[age]="18"

#列出数组下标#

echo ${!ass_array1[*]}

echo ${ass_array1[@]}



echo "Name: ${ass_array1[name]},Age:${ass_array1[age]}"



######输出##############
###weight name age height contry####
###75 zhangsan 18 180 China####
###Name: zhangsan,Age:18###