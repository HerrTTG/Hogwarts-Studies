#!/bin/bash

#��ֵ�����ַ�ʽ

arr=("haizhenyu" "liuyuzhen")
arr[2]='dongxinwang'



##����������� �±꣺��Ӧ��Ԫ��ֵ

for i in ${!arr[*]}
do 
  echo $i:${arr[$i]}
done 


#�±�Ԫ��ֱ���滻 dongxinwang ���滻Ϊqianyang

arr[2]='qianyang'


#���1�Ժ������Ԫ��#

echo ${arr[@]:1}

#���0�����2��Ԫ��

echo ${arr[@]:0:2}



##���
#0:haizhenyu#
#1:liuyuzhen#
#2:dongxinwang#
#liuyuzhen qianyang#
#haizhenyu liuyuzhen#