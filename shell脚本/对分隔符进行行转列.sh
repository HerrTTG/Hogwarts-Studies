#!/bin/bash
 
read  -p "Please in put file direct folder:" dir_path

awk 'BEGIN{RS="|";ORS="\n";OFS = "|"}{print FNR,$0}' $dir_path >123.txt

out_file=$(cd $(dirname $0);pwd)

echo "Execut successed.Record save in $out_file/123.txt "
