#!/bin/bash
cat <<EOF          
"*****************************************************************"
"*Powered By HZY0000111175                                       *"
"*Version:2.1                                                    *"
"*Warning: Please obtain permission before executing the script! *"
"*****************************************************************"
EOF

#版本说明：2.1版本 增加默认OOTB路径和字段。增加自定义变量支持修改话单的任意字段统计
#版本说明：2.0版本 支持人机交互模式下输入自定义路径 格式/xx/xx 将话单放入其中即可
#版本说明：1.7版本 追加支持统计成功入库的正常单，支持检查鉴权失败的错单功能，并且定制了recharge错单的一同检查
#Waring：生产执行此脚本需谨慎！务必检查对应的变量，并且获得客户审批！
#根据局点不同请对变量自定义中的参数进行修改！
#---------------------------------------------------------------------------------------#
####变量自定义####
#/onip/cdr#
cdr_path=$CBP_CDRPATH

#定制的normal入库路径。如需OOTB逻辑此变量请设为空，系统默认检查/onip/cdr/output/normal/backup下#
cust_path="ppscdr4qimport"

#normal的事件类型字段自定义。格式'13'。如需OOTB逻辑此变量请设为空，系统默认检查字段13位事件类型#
normal_field="13"

#错单的检查字段自定义。格式'$16,$27'。如需OOTB逻辑请设置为空，系统自动检查第16,27字段统计事件类型和对应的错误#
error_field='$16,$27'

#所罗门充值错单字段定制。格式'$24'.检查normal单中的充值记录也需此变量不为空#
rc_field='$24'

####变量自定义END####

##变量清理##
unset file
unset file_recharge
unset next_step
unset retryTimes
unset dateE
unset subPath
unset nflag
##变量清理END##


#函数定义#

help(){
	      echo "*****************************************************************"
	      echo "*AuthCheck:cdrCheck.sh -b date(yyyymm)                          *"
	      echo "*AuthCheck:cdrCheck.sh -b date(yyyymmdd)                        *"
        echo "*AuthCheck:cdrCheck.sh -b 1 date(yyyymm)                        *"
        echo "*AuthCheck:cdrCheck.sh -b 1 date(yyyymmdd)                      *"
        echo "*NormalCheck:cdrCheck.sh -b 2 date(yyyymmdd)                    *"
        echo "*Interactive:cdrCheck.sh                                        *"
        echo "*****************************************************************"
        exit 1	
	}

Interactive(){
	
	#人机交互模式的循环函数#
	next_step=input_path
  retryTimes=0
  echo "Script start..."
  while true
  do
	case $next_step in
	      input_path)
            input_path
            sleep 1s
            ;;
        check_path)
            check_path
            sleep 1s
            ;;
        dateinput)
            dateinput
            sleep 1s
            ;;         
        selectM)
            selectM 
            sleep 1s
            ;;
        exit_loop)
        echo "Quit Main process"
        break
            ;;
        *)
            break;
            ;;
        esac
        done
	}


input_path(){

echo "Please input the output and cdr path(defualt is CBP_CDRPATH):" 

read subPath

if [ "x$subPath" = "x" ]
	then 
	next_step=check_path
	retryTimes=3
  else 
  	cdr_path=$subPath
  	if [ ! -d $subPath  ]
  		then 
  			echo "Input path not exist please check!!!"
  			let retryTimes=retryTimes+1
  		 if [ $retryTimes -ge 3 ]
	          then
            exit 1
       fi 
       continue
  	else		
  	retryTimes=3
  	next_step=check_path
    fi
fi
	
	}

check_path(){
	   
echo "Start check_Path..."
if [ ! -d $cdr_path/cdrCheck/output ]
        then
  mkdir -p $cdr_path/cdrCheck/output
  if [ $? -eq 1 ]
  	then 
  		echo "Report Path Create path failed !!! please check!!!"
  	exit 1
  else 
  echo "Output path created..."
  sleep 1s
  fi
fi
next_step=dateinput
}


dateinput(){
	
#判断是否有入参，无则表示为人机模式，读取用户输入变量值#	
if [ $# -gt 0 ]
 then 
 	dateE=$1
else 
 if [ -z $dateE ]
 	then 
  read  -p "Plase input check date:"  dateE
    #检查date长度是符合格式的#
   if [ ! ${#dateE} -eq 6 ] && [ ! ${#dateE} -eq 8 ]
        then 
        	echo "Wrong date format!!!"
           echo "Please input correct date!!!YYYYMMDD or YYYYMM "   
             unset dateE
           retryTimes=`expr $retryTimes + 1`
           #三次重试机会#
           if [ $retryTimes -ge 6 ]
	          then
            exit 1
            else continue
           fi    
        else 
          #为后面的重试机会重新赋值#
          retryTimes=6
          next_step=selectM   
     fi
  else
  read  -p "Plase input check date:"  dateE
  normal_check
  continue
 fi
fi        
}


selectM(){
unset checkM

#打印#
cat <<EOF
Available Mode:
1.Auth faild check
2.Normal check
EOF

echo "please select:"
  read checkM
        case $checkM in
        1) authcheck
        ;;
        2) 
        retryTimes=9
        normal_check
        ;;
        *) echo "Wrong mode!!!"
           echo "Please input 1~2 !!!"
           let retryTimes=retryTimes+1
           #从3开始，重试机会为3次#
           if [ $retryTimes -ge 9 ];then
            exit 1
            elif [ -z "$retryTimes" ]
              then
              exit 1 
            else continue
           fi
        ;;
esac
        }
        
clear_file(){
echo "Start clear_file..."

#根据入参判断需要清理的文件类型是什么，防止执行其他mode的同时清理掉其他mode的输出结果文件#
if [ "x$1" = "x" ] || [ "x$1" = "x1" ]
	then 
		if [ -e $cdr_path/cdrCheck/output/AuthAnaly_$dateE.txt ]
        then
        rm -f $cdr_path/cdrCheck/output/AuthAnaly_$dateE.txt
        echo "Clear auth error report file..."
        sleep 1s
    fi
    if [ -e $cdr_path/cdrCheck/output/AuthAnaly_rc_$dateE.txt ]
        then
    rm -f $cdr_path/cdrCheck/output/AuthAnaly_rc_$dateE.txt
    echo "Clear Rc error report file..."
    sleep 1s
    fi
  elif [ "x$1" = "x2" ]
    then
    if [ -e $cdr_path/cdrCheck/output/Normal_check_$dateE.txt ]
        then
        rm -f $cdr_path/cdrCheck/output/Normal_check_$dateE.txt
        echo "Clear Normal report file..."
        sleep 2s
    fi
fi
}


authcheck(){     
	
	      clear_file 1
	      if [ -z "$subPath" ]
	      	then 
	      	file=$cdr_path"/output/error/error_*_*_*"$dateE"*.*"
          file_recharge=$cdr_path"/output/error/errorrecharge_*_*_*_"$dateE"*_*.*"
	      	else 
	      	file=$cdr_path"/error_*_*_*"$dateE"*.*"
	      	file_recharge=$cdr_path"/errorrecharge_*_*_*_"$dateE"*_*.*"
	      fi
	      
	      
	      if [ ${#dateE} -eq 8 ] || [ ${#dateE} -eq 6 ]
                then
                
               echo "--------------------------------------------"
               echo "Auth Error cdr check process start..."  	
                
                #判断是否有定制的检查字段，在脚本最初进行定义#
                if [ -z $error_field ] && [ -z $rc_field ]     
                 	then 
                 	#OOTB逻辑#
                 	  awk -F"|" '{print $16,$27}' $file | sort |uniq -c | sort -t ' ' -rnk 2 >$cdr_path/cdrCheck/output/AuthAnaly_$dateE.txt
                     
                     elif [ ! -z $error_field ] && [ -z $rc_field ]  
                     then 
                     #定制错单单逻辑#
                 	  awk -F"|" '{print '$error_field'}' $file | sort |uniq -c | sort -t ' ' -rnk 2  >$cdr_path/cdrCheck/output/AuthAnaly_$dateE.txt
                 	  sleep 1s   
                 	   
                 	  elif [ ! -z $rc_field ]   &&  [  -z $error_field ] 
                 	  then 
                 	  awk -F"|" '{print $16,$27}' $file | sort |uniq -c | sort -t ' ' -rnk 2 >$cdr_path/cdrCheck/output/AuthAnaly_$dateE.txt
                 	  #局点定制的充值话单#
                     echo "Recharge auth check process start..."
                     awk -F"|" '{print '$rc_field' }' $file_recharge | sort | uniq -c | sort -rn >$cdr_path/cdrCheck/output/AuthAnaly_rc_$dateE.txt	
                 	  sleep 1s     
                 	  
                 	  elif  [ ! -z $error_field ] && [ ! -z $rc_field ]
                 	  then 
                 	  #定制normal单逻辑#
                 	  awk -F"|" '{print '$error_field'}' $file | sort |uniq -c | sort -t ' ' -rnk 2  >$cdr_path/cdrCheck/output/AuthAnaly_$dateE.txt	
                 	  #局点定制的充值话单#
                     echo "Recharge auth check process start..."
                     awk -F"|" '{print '$rc_field' }' $file_recharge | sort | uniq -c | sort -rn >$cdr_path/cdrCheck/output/AuthAnaly_rc_$dateE.txt        
                     sleep 1s 
                 	     
                 	fi
                  
                 echo "--------------------------------------------"
                 sleep 1s
                  
                 #检查输出文件是否为空# 
                   if [ -s $cdr_path/cdrCheck/output/AuthAnaly_$dateE.txt ]
                         then  echo "Auth cdr check Excute successed "
                               echo "Result save in $cdr_path/cdrCheck/output/AuthAnaly_$dateE.txt"  
                               echo "--------------------------------------------" 
                               if [[ ! -z $rc_field ]]
                               then  
                                 if  [ -s $cdr_path/cdrCheck/output/AuthAnaly_rc_$dateE.txt ] 
                                 then  
                                     echo "Erorr Recharge cdr check Excute successed"
                                     echo "Result save in $cdr_path/cdrCheck/output/AuthAnaly_rc_$dateE.txt "
                                     echo "--------------------------------------------"
                                 else   
                                     echo "Not have such error file ,Recharge output report is empty!!!"
                                     echo "Please check if recharge file is exist on select date!!!" 
                                     echo "--------------------------------------------"    
                                     rm -f $cdr_path/cdrCheck/output/AuthAnaly_rc_$dateE.txt 
                                 fi    
                               fi                                        
                          elif [[ ! -z $rc_field  ]]
                              then
                          	   if [ ! -s $cdr_path/cdrCheck/output/AuthAnaly_$dateE.txt ]  &&  [ ! -s $cdr_path/cdrCheck/output/AuthAnaly_rc_$dateE.txt ]   
                                 then 
                          	        echo "Both file not exist!!!"
                                   echo "Excute Wrong !!!"
                                   rm -f $cdr_path/cdrCheck/output/AuthAnaly_rc_$dateE.txt 
                                   rm -f $cdr_path/cdrCheck/output/AuthAnaly_$dateE.txt
                                   exit 1   
                                 elif [ -s $cdr_path/cdrCheck/output/AuthAnaly_rc_$dateE.txt ] 
                                   then 
                                   echo "Erorr Recharge cdr check Excute successed"
                                   echo "Result save in $cdr_path/cdrCheck/output/AuthAnaly_rc_$dateE.txt "
                                   echo "--------------------------------------------"
                                   echo "Not have such error file ,output report is empty!!!"
                                   echo "please check if cdr file is exist on select date !!!"
                                   echo "--------------------------------------------"               
                              fi   
                          else    
                          echo "Not have such error file ,output report is empty!!!"
                          echo "please check if cdr file is exist on select date !!!"
                          echo "--------------------------------------------"
                          rm -f $cdr_path/cdrCheck/output/AuthAnaly_$dateE.txt	  
                          exit 1                
                 fi
                 next_step=exit_loop
                 
               else 
               echo "Excute Wrong !!!"
                echo "Date in auth check must be YYYYMMDD or YYYYMM!!!"
                exit 1                	
	                  
        fi
}

normal_check(){
	      clear_file 2
	      if [ "x$subPath" = "x"  ]
	      	then 
	      	#file_normal=$cdr_path"/"$cust_path"/bak/"$dateE"/*.*"
	      	nflag=1
	      	else 
	      	file_normal=$subPath"/*"$dateE"*.*"
	      fi
	      
        #判断时间长度是否为8位#
        if [ ${#dateE} -ne 8 ]
                then
                echo "Excute Wrong !!!"
                echo "Date in Normal check must be YYYYMMDD!!!"
                exit 1 
           else          
               if [[ $nflag -eq 1 ]]
               then 
              	 if [ ! -d $cdr_path"/"$cust_path"/bak/"$date ] && [[ ! -z $cust_path ]]
              		 then 
              		  echo "Excute Wrong !!!"
              			echo "$cdr_path"/"$cust_path"/bak/"$date is not exist!!!"
              			exit 1
              	   elif [[ -z $cust_path ]] && [ -d $cdr_path"/cdr4qimport/bak/"$dateE ] 
              	       then 
              	       file_normal=$cdr_path"/cdr4qimport/bak/"$dateE"/*.*"
              	   elif [[ -z $cust_path ]] && [ -d $cdr_path"/output/normal/backup" ] 
              	       then 
              	       file_normal=`echo $cdr_path"/output/normal/backup/normal*$dateE*.*"`
              	   elif [[ -z $cust_path ]] &&  [ ! -d $cdr_path"/cdr4qimport/bak/"$dateE ]  && [ ! -d $cdr_path"/output/normal/backup" ]
              	       then      		
              	       echo "Excute Wrong !!!"
              	       echo "$cdr_path/cdr4qimport/bak/$dateE and $cdr_path/output/normal/backup both not exist!"
              	       exit 1
              	   else 
              		 file_normal=`echo "$cdr_path/$cust_path/bak/$dateE/*.*"`     			                                  
                fi   
              fi
                        echo "--------------------------------------------"
                        echo "Normal check start..."
                        
                        if [[ ! -z $normal_field ]]
	                         then 
	                         #定制内容：取13列，在对13列中账期格式的数据进行替换，最后统计输出#
                           cut -d "|" -f $normal_field $file_normal >> $cdr_path/cdrCheck/output/Normal_check_$dateE_temp.txt 
                           #定制内容：对充值的话单进行字段替换，最终展示为recharge
                           if [ !-z  $rc_field ]
                           	then 
                            sed -r -i 's#^[0-9]{8}$#recharge#g' $cdr_path/cdrCheck/output/Normal_check_$dateE_temp.txt
                           fi
                           cat $cdr_path/cdrCheck/output/Normal_check_$dateE_temp.txt |sort -t ' ' -nrk 1 | uniq -c >>$cdr_path/cdrCheck/output/Normal_check_$dateE.txt
                           rm -f $cdr_path/cdrCheck/output/Normal_check_$dateE_temp.txt
                           else 
                           #OOTB逻辑处理#
                           cut -d "|" -f 16 $file_normal >> $cdr_path/cdrCheck/output/Normal_check_$dateE_temp.txt
                           cat $cdr_path/cdrCheck/output/Normal_check_$dateE_temp.txt |sort -t ' ' -nrk 1 | uniq -c >>$cdr_path/cdrCheck/output/Normal_check_$dateE.txt
                           rm -f $cdr_path/cdrCheck/output/Normal_check_$dateE_temp.txt
                       fi 
                        
                        sleep 1s
                        if [ -s $cdr_path/cdrCheck/output/Normal_check_$dateE.txt ]
                        	then 
                        	echo "Normal check execute successed"
                          echo "Result save in $cdr_path/cdrCheck/output/Normal_check_$dateE.txt"
                          else 
                          echo "Excute Wrong !!!"
                          echo "Not have such Normal file ,Normal output report is empty!!!"
                          rm -f $cdr_path/cdrCheck/output/Normal_check_$dateE.txt
                          exit 1
                        fi     
             
             
   fi
   echo "--------------------------------------------"
   next_step=exit_loop
}


#函数定义END#

#--------------------------------------------------------------------------------------------------------#

#######主程序######

##检查调用方式，入参或者人机交互##

if [ $# -gt 0 ];
	then 
	   if [ "x$1" = "x-b" ];then
	     	shift 1
		    if [ $# -eq 1 ]
		    	then 
		      dateinput $1
		    	check_path
		    	authcheck 
			  elif [ "x$1" = "x1" ]
			    then 
			    dateinput $2
			    check_path
			    authcheck 
			  elif [ "x$1" = "x2" ]
			  then
			  	dateinput $2
			    check_path
			    normal_check 
        else 
        	help
		  	fi 
		  else 	
		    echo "invalid use of cdrCheck.sh, no parameter is needed."
		  	help
		 fi 
	else 
  Interactive
fi 

echo "Quit Script"
exit 0 

#######主程序END######