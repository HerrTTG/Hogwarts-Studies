#!/bin/bash

#test �ж��ַ� &&
#��ʾtest����true(��$?����0) ִ��&&������� 
#test �ж��ַ�  && ����1 || ����2 
#��ʾtest�жϷ���true(��$?����0)ִ������1  �жϷ���false(��$?����1)ִ������2

y=""
x=123

test -z $y
echo $?

test -z $y && echo "Yes,is null" || echo "Not,is not null"

test -z $x
echo $?

test -n $x && echo "Yes,is not null" || echo "Not,is null"