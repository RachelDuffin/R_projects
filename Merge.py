#!/usr/bin/python
import os, sys, csv, glob
import pandas as pd

#Convert text files to csv files and add column headers "Genes", "above20x" and "average" to each file------------------------

from pandas import read_csv

import glob
for file in glob.glob("/home/rduffin/Desktop/R_projects/*new.txt"):
    df = read_csv(file, header=None, sep=',')
    df.columns = ["Genes", "above20x"]
    df.to_csv(file, index=False) 

#Merge data frames by "Genes" using outer join------------------------------------------- 

df = pd.DataFrame(columns=["Genes", "above20x"]) #Create empty database with which to merge

for file in glob.glob("/home/rduffin/Desktop/R_projects/*new.txt"):
    data = pd.read_csv(file)
    df.merge(data, on = "Genes", how = 'outer')
    
df.to_csv('/home/rduffin/Desktop/R_projects/mergedfile.csv', index=False) #write merged df to csv
#------------------------------------------------------------------------------------------

#path = "/home/rduffin/Desktop/R_projects/*.csv"

#     
