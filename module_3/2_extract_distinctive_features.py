#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 14:41:30 2021

@author: ecamo19
"""

#Import Modules ---------------------------------------------------------------
import cv2
import h5py
import numpy as np
import pandas as pd
from PIL import Image
from skimage import measure
import matplotlib.pyplot as plt
import matplotlib.pyplot as pylab
from skimage.io import imread, imshow
from skimage.filters import gaussian, threshold_otsu
from skimage.measure import label, regionprops, regionprops_table

#------------------------------------------------------------------------------

# From segmented cell images (choose any segmentation technique you prefer) 
# extract at least four distinctive features + assign class label according to 
# cell type from documentation (as last column) – there should be seven 
# distinctive classes.


#Path where h5py file is stored -----------------------------------------------
path = "/home/ecamo19/Documents/cursos_libros_tutoriales/cursos/VCU/image_analysis/project/part_3"

#Load h5py file with segmented images ----------------------------------------- 
hdf = h5py.File(f'{path}/cancerous_cell_smears_grey_enhanced_and_segmentated.hdf5','r') 


# Properties to measure -------------------------------------------------------
properties = ('area','perimeter','orientation',
              'eccentricity','convex_area','centroid',
              'major_axis_length','minor_axis_length')


#Calculate features -----------------------------------------------------------

for each_cell_type in hdf:
        
        # Each cell group        
        cell_type = hdf.get(each_cell_type)         
        
        # For each image in the group
        for each_image_label in cell_type:
            
            #Get image id
            label_id = each_image_label 
            #print(label)

            #Get image array
            image_array = np.array(cell_type.get(each_image_label))

            #Get lables from image
            labels_image = measure.label(image_array, background = 1)

            #Measure feature in image array
            props_img = regionprops_table(labels_image, separator = '_', properties = properties)

            # Save features as pandas dataframe
            df = pd.DataFrame.from_dict(props_img)
            
            #Create a new column that contains the label id
            df['label'] = f'{label_id}'

            #Save data frame
            df.to_csv(f'{path}/data_for_knn/{label_id}.csv',encoding='utf-8-sig') 

