#!/bin/bash

a=("1" "2" "3")
echo "${a[@]}"

for loop in ${a[@]}
do 
 echo "you num is : ${a[loop-1]}"
 done
 
 
 
echo "liuyuzhen haizhenyu" >namelist.txt

for str in namelist.txt
do 
 echo "you name is :$str"
 done