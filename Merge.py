#!/usr/bin/python
import os, sys, csv, glob
import pandas as pd

#Add column headers "Genes", "above20x" and "average" to each file------------------------

from pandas import read_csv

import glob
for file in glob.glob("/home/rduffin/Desktop/R_projects/*new.csv"):
    df = read_csv(file, header=None, index_col=False)
    df.columns = ["Genes", "above20x"]
    df.to_csv(file)
#WORKS NOW ! 

#Merge data frames by "Genes" using outer join------------------------------------------- 

df = pd.DataFrame(columns=["Genes", "above20x"]) #Create empty database with which to merge




#------------------------------------------------------------------------------------------

#path = "/home/rduffin/Desktop/R_projects/*.csv"

#     
