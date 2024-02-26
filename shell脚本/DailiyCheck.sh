#!/bin/bash        
#"*****************************************************************"
#"*Powered By HZY0000111175                                       *"
#"*Version:1.0                                                    *"
#"*Warning: Please obtain permission before executing the script! *"
#"*****************************************************************"


#Waring：生产执行此脚本需谨慎！无比检查对应的变量，并且获得客户审批！
#功能说明：此脚本用于日常检查是否有BDI处理失败的话单。


path='/data/bdi/datastore/filein/*/*.unl'

#echo $path

k=`find $path | wc -l `

#echo $k

if [[ $k -gt 0 ]]
	then 
	find  $path
	else 
	exit 0 
	fi 	


