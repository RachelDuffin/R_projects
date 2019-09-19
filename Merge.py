#!/usr/bin/python
import os, sys, csv, glob, re, subprocess
import pandas as pd
import numpy as np

#Import genesymbols and assign new header names-------------------------------------------------------------------------------------------------------------------

db = pd.read_csv("genesymbols.csv", index_col=None) #Read genesymbols database
db.columns=["Genes", "Symbols"]
db.to_csv("genesymbolscopy.csv", index = False)

#Adds column headers, removes average column, adds ID column and merges all files------------------------------------------------------------------------------!

li = []

for file in glob.glob("/home/rduffin/Desktop/R_projects/*.chanjo_txt"):
    df = pd.read_csv(file, header = None, names=["Genes", "above20x", "average"], usecols=['Genes', "above20x"], delimiter='\t') 
    df ['sampleID'] = file.split("_")[3]
    li.append(df)

merged = pd.concat(li, axis=0, ignore_index=True)
merged.to_csv("merged.csv", index=None, header=True) #write merged dataframe to CS

#Merge the dataframe with the database gene symbols/Entrez IDs-----------------------------------------------------------------------------------------
