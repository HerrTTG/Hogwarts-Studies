#!/bin/bash

# -��ʱ������x=$yֵ ����yΪunset ȡx=new
# +��ʱ������x=newֵ ����yΪunset ȡx=$y
# =��ʱ�����y unset y�ȱ�Ϊnewֵ �����������x=$y
unset  y
x=${y-new}

echo 'unset y x=${y-new}':"x=$x y=$y"


y=""
x=${y-new}

echo 'y is null x=${y-new}':"x=$x y=$y"



y=aa
x=${y-new}

echo 'y is aa x=${y-new}':"x=$x y=$y"

echo "----------------------------------------------------------"

unset y 

x=${y+new}

echo 'unset y  x=${y+new}':"x=$x y=$y"

y=""

x=${y+new}
echo 'y is null  x=${y+new}':"x=$x y=$y"

y=aa
x=${y+new}
echo 'y is aa x=${y+new}':"x=$x y=$y"

echo "----------------------------------------------------------"

unset y 
x=${y=new}

echo 'unset y  x=${y=new}':"x=$x y=$y"

y=""
x=${y=new}
echo 'y is null  x=${y=new}':"x=$x y=$y"

y=aa
x=${y=new}
echo 'y is aa  x=${y=new}':"x=$x y=$y"