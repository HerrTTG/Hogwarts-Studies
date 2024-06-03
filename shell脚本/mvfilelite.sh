#!/bin/bash

path='/onip/cdr/ppscdr4qimport/bak/'$1

file1='rec*.unl'
file2='datas*.unl'
file3='sms*.unl'
file4='vou*.unl'
#file5='normal*'$1'*.dat'


#echo $path
#echo $file1
#echo $file2
#echo $file3
#echo $file4




#echo "scp -r cbpapp@172.31.72.116:"$path/$file1  "/datas/bdi/datastore/invcdr/pps/normal"
#scp -r cbpapp@172.31.72.116:/onip/cdr/output/normal/$file5  /onip/app/inv/hzy/bak
#scp -r cbpapp@172.31.72.116:/onip/cdr/output/normal/$file5  /onip/app/inv/hzy/bak


echo "Begin to mv" $file1
scp -r cbpapp@192.168.51.47:$path/$file1  /datas/bdi/datastore/invcdr/pps/normal

echo "Begin to mv" $file2
        scp -r cbpapp@192.168.51.47:$path/$file2  /datas/bdi/datastore/invcdr/pps/normal

echo "Begin to mv" $file3
           scp -r cbpapp@192.168.51.47:$path/$file3  /datas/bdi/datastore/invcdr/pps/normal

echo "Begin to mv" $file4
                scp -r cbpapp@192.168.51.47:$path/$file4  /datas/bdi/datastore/invcdr/pps/normal
