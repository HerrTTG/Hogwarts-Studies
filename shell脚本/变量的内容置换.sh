#!/bin/bash

# -的时候优先x=$y值 除非y为unset 取x=new
# +的时候优先x=new值 除非y为unset 取x=$y
# =的时候除非y unset y先变为new值 其他情况优先x=$y
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