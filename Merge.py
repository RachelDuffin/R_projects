#!/usr/bin/python
import os, sys, csv, glob
import pandas as pd

#Convert text files to csv files and add column headers "Genes", "above20x" and "average" to each file------------------------

from pandas import read_csv

import glob
for file in glob.glob("/home/rduffin/Desktop/R_projects/*new.csv"):
    df = read_csv(file, header=None, sep=',')
    df.columns = ["Genes", "above20x"]
    df.to_csv(file, index=False) 


#Merge data frames by "Genes" using outer join------------------------------------------- merges them into one file but only 2 columns (repeated gene names)

df = pd.DataFrame(columns=["Genes", "above20x"]) #Create empty database with which to merge
df.to_csv(r"/home/rduffin/Desktop/R_projects/merged.csv", index = None, header=True) #write df to csv

filenames = glob.glob("/home/rduffin/Desktop/R_projects/*new.csv")

with open('merged.csv', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)

  #  data = pd.read_csv(file)
 #   merged = pd.merge(df, data, on = "Genes", how = 'outer')
    
#df.to_csv('/home/rduffin/Desktop/R_projects/mergedfile.csv', index=False) #write merged df to csv
#------------------------------------------------------------------------------------------

#path = "/home/rduffin/Desktop/R_projects/*.csv"

#     
