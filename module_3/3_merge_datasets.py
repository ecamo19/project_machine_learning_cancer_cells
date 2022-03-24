#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 16:57:21 2021

@author: ecamo19
"""

#Import modules ---------------------------------------------------------------
import numpy as np
import os
import glob
import pandas as pd

# -----------------------------------------------------------------------------


# Path to .csv files are stored
path = '/home/ecamo19/Documents/cursos_libros_tutoriales/cursos/VCU/image_analysis/project/part_3/data_for_knn'

# Empty list for storing the dataframes
list_of_dataframes = []    

# Read
for file in glob.glob(f"{path}/*.csv"):
    
        #Read the image in grey scale
        list_of_dataframes.append(pd.read_csv(file))


#Merge data frame
merged_df = pd.concat(list_of_dataframes)
merged_df.to_csv(f'{path}/dataset_merged_for_knn.csv',index=False)