#!/bin/bash
#Powered By HZY0000111175#
#Version:1.76#
#版本说明：1.7版本 追加支持统计成功入库的正常单，支持检查鉴权失败的错单功能，并且定制了recharge错单的一同检查#
#更新说明：1.76在1.7的基础上修改了函数格式 脚本语法 支持date和mode的试错退出 支持人机交互或者入参调用#
#并且增加了输出文件文件名时间格式。修改了清理逻辑#
#输出结果的排序逻辑变更#
#Reader ME：生产执行此脚本需谨慎！务必检查对应的变量，并且获得客户审批！#

#---------------------------------------------------------------------------------------#
####变量定义####

cdr_path=$CBP_CDRPATH
#/onip/cdr#
cust_path="ppscdr4qimport"


####变量定义END####

##变量清理##
unset file
unset file_recharge
unset next_step
unset retryTimes
unset dateE
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
	next_step=check_path
  retryTimes=0
  echo "Script start..."
  while true
  do
	case $next_step in
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
        sleep 1s
        break
            ;;
        *)
            break;
            ;;
        esac
        done
	}


check_path(){
	   
echo "Start check_Path..."
if [ ! -d $cdr_path/cdrCheck/output ]
        then
  mkdir -p $cdr_path/cdrCheck/output
  echo "Output path created..."
  sleep 1s
fi
next_step=dateinput
}


dateinput(){
	
#判断是否有入参，无则表示为人机模式，读取用户输入变量值#	
if [ $# -gt 0 ]
 then 
 	dateE=$1
else 
read  -p "Plase input check date:"  dateE
fi
        
#检查date长度是符合格式的#
     if [ ! ${#dateE} -eq 6 ] && [ ! ${#dateE} -eq 8 ]
        then echo "Wrong date format!!!"
             echo "Please input correct date!!!YYYYMMDD or YYYYMM "   
           retryTimes=`expr $retryTimes + 1`
           #三次重试机会#
           if [ $retryTimes -ge 3 ]
	          then
            exit 1
             #变量为空则表示为入参模式，则因为时间长度不符合，直接跳出程序，不进行重试#
             elif [ -z "$retryTimes" ]
             then 
             exit 1
            else continue
           fi    
        else 
          #为后面的重试机会重新赋值#
          retryTimes=3
          next_step=selectM   
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
        next_step=exit_loop
        ;;
        2) normal_check
        next_step=exit_loop
        ;;
        *) echo "Wrong mode!!!"
           echo "Please input 1~2 !!!"
           let retryTimes=retryTimes+1
           #从3开始，重试机会为3次#
           if [ $retryTimes -ge 6 ];then
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
        file=$cdr_path"/output/error/error_*_*_*"$dateE"*.dat"
        file_recharge=$cdr_path"/output/error/errorrecharge_*_*_*_"$dateE"*_*.dat"

        echo "--------------------------------------------"
        echo "Auth Error cdr check process start..."
        sleep 1s


        #错单字段根据局点定制#
        awk -F"|" '{print $16,$27}' $file | sort |uniq -c | sort -t ' ' -rnk 2 >$cdr_path/cdrCheck/output/AuthAnaly_$dateE.txt

        sleep 1s


        #局点定制的充值话单#
        echo "Recharge auth check process start..."
        sleep 1s
        
        awk -F"|" '{print $24}' $file_recharge | sort | uniq -c | sort -rn >$cdr_path/cdrCheck/output/AuthAnaly_rc_$dateE.txt
         
        echo "--------------------------------------------"
        sleep 1s
         
        #检查输出文件是否为空# 
          if [ -s $cdr_path/cdrCheck/output/AuthAnaly_$dateE.txt ]
                then  echo "Auth cdr check Excute successed "
                      echo "Result save in $cdr_path/cdrCheck/output/AuthAnaly_$dateE.txt"  
                      echo "--------------------------------------------" 
                      if  [ -s $cdr_path/cdrCheck/output/AuthAnaly_rc_$dateE.txt ]  
                      then  echo "Erorr Recharge cdr check Excute successed"
                            echo "Result save in $cdr_path/cdrCheck/output/AuthAnaly_rc_$dateE.txt "
                            echo "--------------------------------------------"
                      else 
                            echo "Not have such error file ,Recharge output report is empty!!!"
                            echo "Please check if recharge file is exist on select date!!!" 
                            echo "--------------------------------------------"    
                            rm -f $cdr_path/cdrCheck/output/AuthAnaly_rc_$dateE.txt 
                      fi   
                 elif   [ -s $cdr_path/cdrCheck/output/AuthAnaly_rc_$dateE.txt ]   
                      then  echo "Erorr Recharge cdr check Excute successed"
                            echo "Result save in $cdr_path/cdrCheck/output/AuthAnaly_rc_$dateE.txt "   
                            echo "--------------------------------------------"  
                      if  [ ! -s $cdr_path/cdrCheck/output/AuthAnaly_$dateE.txt ]  
                      	then   
                            echo "Not have such error file ,output report is empty!!!"
                            echo "please check if cdr file is exist on select date !!!"
                            echo "--------------------------------------------"
                            rm -f $cdr_path/cdrCheck/output/AuthAnaly_$dateE.txt
                      fi                               
                 elif [ ! -s $cdr_path/cdrCheck/output/AuthAnaly_$dateE.txt ]  &&  [ ! -s $cdr_path/cdrCheck/output/AuthAnaly_rc_$dateE.txt ]   
                 then 
                 	   echo "Both file not exist!!!"
                     echo "Excute Wrong !!!"
                     rm -f $cdr_path/cdrCheck/output/AuthAnaly_rc_$dateE.txt 
                     rm -f $cdr_path/cdrCheck/output/AuthAnaly_$dateE.txt
                     exit 1                           
        fi

}

normal_check(){
	
	      clear_file 2
        file=$cdr_path"/"$cust_path"/bak/"$dateE
        #判断时间长度是否为8位#
        if [ ${#dateE} -ne 8 ]
                then
                echo "Excute Wrong !!!"
                echo $file" is not exist !!!"
                echo "Date in Normal check must be YYYYMMDD!!!"
                exit 1
              elif [ ! -d $file ]
              then 
              	echo "Excute Wrong !!!"
              	echo $file" is not exist !!!"
                exit 1
                else
                        echo "--------------------------------------------"
                        echo "Normal check start..."
                        sleep 1s
                        
                        #取13列，在对13列中账期格式的数据进行替换，最后统计输出#
                        cut -d "|" -f 13 $file/*.unl >> $cdr_path/cdrCheck/output/Normal_check_$dateE_temp.txt
                        sed -r -i 's#^[0-9]{8}$#recharge#g' $cdr_path/cdrCheck/output/Normal_check_$dateE_temp.txt
                        cat $cdr_path/cdrCheck/output/Normal_check_$dateE_temp.txt | uniq -c |sort -t ' ' -nrk 1 >>$cdr_path/cdrCheck/output/Normal_check_$dateE.txt
                        rm -f $cdr_path/cdrCheck/output/Normal_check_$dateE_temp.txt
                        
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
              next_step=exit_loop
   echo "--------------------------------------------"

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
