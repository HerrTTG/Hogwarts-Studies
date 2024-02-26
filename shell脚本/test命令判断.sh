#!/bin/bash

#test 判断字符 &&
#表示test返回true(即$?返回0) 执行&&后的命令 
#test 判断字符  && 命令1 || 命令2 
#表示test判断返回true(即$?返回0)执行命令1  判断返回false(即$?返回1)执行命令2

y=""
x=123

test -z $y
echo $?

test -z $y && echo "Yes,is null" || echo "Not,is not null"

test -z $x
echo $?

test -n $x && echo "Yes,is not null" || echo "Not,is null"