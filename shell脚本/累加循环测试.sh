#!/bin/bash
#�ۼ�ѭ�����԰���#

for((i=1;i<=100;i++))
do
s=`expr $s + $i`
done

echo $s 