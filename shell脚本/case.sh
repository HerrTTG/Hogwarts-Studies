#!/bin/bash

echo 'plese input a number 1~4'
echo 'you number is :'
read num
case $num in
1) echo 'you select  1'
;;
2) echo 'you select  2'
;;
3) echo 'you select  3'
;;
4) echo 'you select  4'
;;
*) echo 'you number is not betwent 1~4'
;;
esac