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

c=("$a" "$b")   #定义数组，数组元素可用变量赋值
echo "${c[@]}"

 if [[ "${c[*]}" =~ ${a} ]] #变量a是否存在与数组C中 模糊查询非精确遍历
	then 
		echo "a includ c"
fi

if [ -z $a ]  #长度是否为0
	then 
		echo "a leath is 0"
	else 
	  echo "a leath is not 0"
fi

if [ -n $b ] #长度是否不为0
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