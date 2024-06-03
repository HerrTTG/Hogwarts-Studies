#!/bin/bash        
#"*****************************************************************"
#"*Powered By HZY0000111175                                       *"
#"*Version:1.0                                                    *"
#"*Warning: Please obtain permission before executing the script! *"
#"*****************************************************************"


#Waring������ִ�д˽ű���������ޱȼ���Ӧ�ı��������һ�ÿͻ�������
#����˵�����˽ű������ճ�����Ƿ���BDI����ʧ�ܵĻ�����


path='/datas/bdi/datastore/filein/*/*.unl'

#echo $path

k=`find $path | wc -l `

#echo $k

if [[ $k -gt 0 ]]
	then 
	find  $path
	else 
	exit 0 
	fi 	


