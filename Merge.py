#!/usr/bin/python
import os, sys, csv, glob, re, subprocess
import pandas as pd
import numpy as np

#Add column headers, remove average column and add new patientID column. Rename files as copies. Add the patient IDs in a column. ----------------------------- DONE !

for file in glob.glob("/home/rduffin/Desktop/R_projects/*.chanjo_txt"):
    df = pd.read_csv(file, header = None, names=["Genes", "above20x", "average"], usecols=['Genes', "above20x"], sep = '\t') 
    df ['patientID'] = file.split("_")[3]
    outfile = file.replace("chanjo_txt", "copy_chanjo_txt")
    df.to_csv(outfile, index=False) #write to CSV

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
