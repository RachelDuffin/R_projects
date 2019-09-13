#!/usr/bin/python
import os, sys, csv, glob, re, subprocess
import pandas as pd
from pandas import read_csv

#Convert text files to csv files and add column headers "Genes", "above20x" and "toremove" to each file-----------------------------

filenames = glob.glob("/home/rduffin/Desktop/R_projects/*.chanjo_txt") #grab filenames

for file in glob.glob("/home/rduffin/Desktop/R_projects/*.chanjo_txt"):
    df = read_csv(file, header=None, sep='\t')
    df.columns = ["Genes", "above20x", "toremove"]
    df["PatientID"] = ""
    df.to_csv(file, index=False) 

#Add patient IDs to the ID column ---------------------------------------------------------------------------------------------NEEDS WORK!

for fname in filenames:
    res = re.findall("^(?:[^_]+_){3}([^_]+)", fname)
    if not res: continue
    print res[0] # You can append the result to a list

#Run shell script------------------------------------------------------------------------------------------------------------------

subprocess.call(['./Rename.sh']) #Shell script removes third column and renames files


#Writes each row of each file to one file-------------------------------------------

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
