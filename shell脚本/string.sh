#!/bin/bash

a="abc"
b="efg"

if [ $a = $b ]
 then 
 	echo "a eq b"
else
  echo "a ne b"
fi
  
if [ $a != $b ]
	then 
		echo "a ne b is true"
	else
	  echo "a ne be is false"
fi

c=("$a" "$b")   #�������飬����Ԫ�ؿ��ñ�����ֵ
echo "${c[@]}"

 if [[ "${c[*]}" =~ ${a} ]] #����a�Ƿ����������C�� ģ����ѯ�Ǿ�ȷ����
	then 
		echo "a includ c"
fi

if [ -z $a ]  #�����Ƿ�Ϊ0
	then 
		echo "a leath is 0"
	else 
	  echo "a leath is not 0"
fi

if [ -n $b ] #�����Ƿ�Ϊ0
	then 
		echo "b leath is not 0"
	else 
	  echo "b leath is 0"	
fi

if [ $a ]  
	then 
		echo "a is not null"
	else 
	  echo "a is null"
fi