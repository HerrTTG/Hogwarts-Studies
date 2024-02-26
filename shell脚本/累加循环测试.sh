#!/bin/bash
#ÀÛ¼ÓÑ­»·²âÊÔ°¸Àı#

for((i=1;i<=100;i++))
do
s=`expr $s + $i`
done

echo $s 