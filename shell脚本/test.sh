
a=`ls *.sh`

for i in $a:
do
  echo 'cat' $i>test.txt
done