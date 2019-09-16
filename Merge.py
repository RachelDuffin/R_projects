#!/usr/bin/python
import os, sys, csv, glob, re, subprocess
import pandas as pd
import numpy as np

#Add column headers, remove average column and add new patientID column. Rename files as copies. Add the patient IDs in a column. ----------------------------- DONE !

for file in glob.glob("/home/rduffin/Desktop/R_projects/*.chanjo_txt"):
    df = pd.read_csv(file, header = None, names=["Genes", "above20x", "average"], usecols=['Genes', "above20x"], sep = '\t') 
    df ['sampleID'] = file.split("_")[3]
    outfile = file.replace("chanjo_txt", "copy_chanjo_txt")
    df.to_csv(outfile, index=False) #write to CSV

#Writes each row of each file to one file-------------------------------------------------------------------------------------------------------------

filenames = glob.glob("/home/rduffin/Desktop/R_projects/*copy_chanjo_txt")

li = []

for filename in filenames:
    df = pd.read_csv(filename, index_col=None)
    li.append(df)

merged = pd.concat(li, axis=0, ignore_index=True)
merged.to_csv(r"/home/rduffin/Desktop/R_projects/merged.csv", index = None, header=True) #write df to csv

#Give new header names for genesymbols file-------------------------------------------------------------------------------------------------------------------
db = pd.read_csv("genesymbols.csv", index_col=None) #Read genesymbols database
new_header = ['Genes', 'Symbols'] 
db.to_csv("genesymbolscopy.csv", index = None, header=new_header)


#Merge the dataframe with the database gene symbols/Entrez IDs-----------------------------------------------------------------------------------------
