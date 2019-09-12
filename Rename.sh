#!/bin/bash

#Rename files as sequential numbers
n=1; 
for f in *.chanjo_txt; do 
    mv "$f" "$((n++))old.csv"; 
done

#Remove column 3 ---------------------------------------
n=1; 
for f in *.csv; do 
    awk '{print $1", "$2}' "$f" > "$((n))new.csv"
     ((n++))
done

#Remove *old.csv files ----------------------------------

rm *old.csv