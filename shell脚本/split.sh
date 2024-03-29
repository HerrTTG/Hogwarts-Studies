#!/bin/bash
## 入参1 为 'filename==$1,$2,$3,$4' 选取过滤列##

##制造测试数据##

awk 'BEGIN{print " MISIDN "", "" Active Time "", "" Status "", "" Main Account Balance "}' >temp.unl

sed -i '$a 6762323,20221213002243,2,2000' temp.unl

#入参赋值##

str=$1

#根据入参过滤过滤多余的列，并且分割为filename \n $1,$2,$3,$4 并且保存为数组 ##

file_field=(`awk 'BEGIN{len=split('"\"$str\""',newarray,"=="); for(i=1;i<=len;i++){print newarray[i]}}'`)

#将分割后的过滤列结果从数组中取出待引用##

sendfield=${file_field[1]}
##echo ${file_field[1]}##
##$1,$2##

#对文件进行指定列输出 awk -v 表示引用外部的变量$sendfield##

awk -F "," -v OFS="," '{print '$sendfield'}' temp.unl  > finnal.unl

rm -f temp.unl