#!/bin/bash
while true
 do
  echo -n " please input number 1~5: "
  read aNum
   case $aNum in
   1|2|3|4|5) echo "Your number is $aNum!"
   ;;
   *) echo "wrong number!"
      continue
   ;;
   esac
 done