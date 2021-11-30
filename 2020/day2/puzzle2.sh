cat input |\
 sed 's/-/ /; s/://' |\
 cut -f 1-4 -d' ' |\
 awk -e '{
     split($4,pw_chars,"")
     first=pw_chars[$1]
     second=pw_chars[$2]
     if((first==$3 || second==$3) && (first != second)) print $0 " is valid " first second
 }' 