#!/bin/bash
  
#�������鶨��ز����٣�������Ĭ��Ϊ��ֵ����#
declare -A ass_array1

#һ�����������鸳ֵ#
ass_array1=([contry]='China' [height]=180 [weight]=75)

#���±�׷�Ӹ�ֵ#
ass_array1[name]="zhangsan"
ass_array1[age]="18"

#�г������±�#

echo ${!ass_array1[*]}

echo ${ass_array1[@]}



echo "Name: ${ass_array1[name]},Age:${ass_array1[age]}"



######���##############
###weight name age height contry####
###75 zhangsan 18 180 China####
###Name: zhangsan,Age:18###