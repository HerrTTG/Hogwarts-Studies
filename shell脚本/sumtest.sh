#!/bin/bash
a=10
b=20

if [ $a -eq $b ]
   then
     echo "a eq b,a==$10 "
   else
     echo "a ne b,a==$a,b==$b"
fi

c=`expr $a + $b` #�����ʽexpr �Ż�Ա�����������
echo "a+b=c,c==$c"

if [ $a -gt $c ]
    then
     echo "a great than c"
    else
      echo "a less than c"
fi