#!/bin/bash

#Rename files as sequential numbers
n=1; 
for f in *.chanjo_txt; do 
    mv "$f" "$((n++))old.txt"; 
done

#Remove column 3 ---------------------------------------
n=1; 
for f in *old.txt; do 
    awk '{print $1", "$2}' "$f" > "$((n))new.txt"
     ((n++))
done

#Remove *old.csv files ----------------------------------

rm *old.txt