#!/usr/bin/python
import os, sys, csv, glob, re, subprocess
import pandas as pd
import numpy as np

#Prepare the genesymbols.csv file for merging----------------------------------------------------------------------------------------------------------------------------------

db = pd.read_csv("genesymbols.csv", index_col=None) #Read genesymbols database
db.columns=["Entrez", "Gene"] #Assign column names to db

#Prepare all patient data files for merging and concatenate--------------------------------------------------------------------------------------------------------------------

li = []

for file in glob.glob("/home/rduffin/Desktop/R_projects/*.chanjo_txt"): #creates a list of filenames to use in the loop
    df = pd.read_csv(file, header = None, names=["Entrez", "above20x", "average"], usecols=['Entrez', "above20x"], delimiter='\t') #reads each csv file
    df = df.astype('str') #converts dataframe from int to str 
    df ['Sample'] = file.split("_")[3] #splits file name by _ and adds third item from split to a new column named 'Sample' for each dataframe
    li.append(df) #appends each dataframe to li

merged = pd.concat(li, axis=0, ignore_index=True) #concatenates all dataframes in li  

#Add gene symbols ready for use in the webapp, and remove all rows with Entrez IDs that have no gene symbols--------------------------------------------------------------------

new = pd.merge(merged, db, how="left", on="Entrez") #Perform left merge on "Gene"
new.replace('', np.nan, inplace=True) #Replace blank cells with NaN values
new.dropna(subset=['Gene'], inplace=True) #Drop rows that contain NaN from data frame 
final = new[['Sample', 'Gene', 'above20x']] #Create new dataframe with necessary columns in correct order
final.to_csv("forboxplot.csv", index = False) #Write to a csv file ready for the app

#Create list of gene names (no repeats) ----------------------------------------------------------------------------------------------------------------------------------------
my_list = final["Gene"].values #Creates list of gene names from dataframe
names = np.unique(my_list) #finds unique gene names and returns sorted elements
np.savetxt("names.csv", names, header = "Gene", fmt='%s') #Write numpy array to a csv file ready for the app
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


