cat input |\
 sed 's/-/ /; s/://' |\
 cut -f 1-4 -d' ' |\
 awk -e '{
     n=split($4,a,$3)-1
     if(n>=$1 && n<=$2) print $0 " is valid [" n "] "
 }'