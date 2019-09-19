#!/usr/bin/python
import os, sys, csv, glob, re, subprocess
import pandas as pd
import numpy as np

#Prepare the genesymbols.csv file for merging-------------------------------------------------------------------------------------------------------------------

db = pd.read_csv("genesymbols.csv", index_col=None) #Read genesymbols database
db.columns=["Gene", "Symbols"] #Assign column names to db
db.to_csv("genesymbolscopy.csv", index = False) #writes dataframe to csv- creates copy of original file with column names added

#Prepare all patient data files for merging and concatenate------------------------------------------------------------------------------!

li = []

for file in glob.glob("/home/rduffin/Desktop/R_projects/*.chanjo_txt"): #creates a list of filenames to use in the loop
    df = pd.read_csv(file, header = None, names=["Gene", "above20x", "average"], usecols=['Gene', "above20x"], delimiter='\t') #reads each csv file
    df = df.astype('str') #converts dataframe from int to str 
    df ['Sample'] = file.split("_")[3] #splits file name by _ and adds third item from split to a new column named 'Sample' for each dataframe
    li.append(df) #appends each dataframe to li

merged = pd.concat(li, axis=0, ignore_index=True) #concatenates all dataframes in li  

#Add gene symbols ready for use in the webapp-----------------------------------------------------------------------------------------

new = pd.merge(merged, db, how="left", on="Gene") #Perform left merge on "Gene"
final = new[['Sample', 'Gene', 'above20x']] #Create new dataframe with necessary columns in correct order
final.to_csv("forboxplot.csv", index = False) #Write to a csv file ready for the app
