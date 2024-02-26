#!/bin/bash
#test命令等价于普通if命令。if命令需要加大括号，test不需要

a=111
b=120

if test $a -eq $b
	then echo "a eq b"
	else echo "a ne b"
fi