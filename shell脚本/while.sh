#!/bin/bash
#let��expr�����ۼӵȼۣ��������ڸ�ʽ
#�������ʽ�ȼ�
i=1
while ((i <= 5))
do
   echo "$i"
   let "i++"
done



a=6
while ((a <= 10))
   do
   echo "$a"
   a=`expr $a + 1`
  done
  
c=11
while [ $c -le 15 ]
	do 
		echo "$c"
		let "c++"
	done