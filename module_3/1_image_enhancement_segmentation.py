#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  9 12:22:28 2021

@author: ecamo19
"""

#Modules-----------------------------------------------------------------------

import numpy as np
import os
import glob
import cv2
import h5py
from PIL import Image
import matplotlib.pyplot as plt
from skimage import restoration
from scipy.ndimage import label
import matplotlib.pyplot as plt
from skimage import morphology
import matplotlib.pyplot as pylab
from skimage.filters import sobel
from skimage.segmentation import clear_border


#crear diccionary y lista

def images_enhaged_segmented_to_hdf5(path1, path2):
    # This function takes the path where the images are, read them and save a
    # hdf5 file
    # Path2 where the hdf5 file will be saved
    
    
    # Create empty dictionary for storing images and ids
    images_dict = {}
    
    for file in glob.glob(f"{path1}/*.BMP"):
    
        #Get image id
        img_id = os.path.basename(file)
    
        #Read the image in grey scale
        image = cv2.imread(file, 0)
         
        #Enhance and segement image-------------------------------------------- 
        
        #Invert colors of image
        image_array_grey = np.invert(np.array(image))
        
        # remove artifacts connected to image border
        image_array_grey_buffer = clear_border(image_array_grey, buffer_size= 10)
        
        # Enhance image  
        
        # Median filter
        img_median = cv2.medianBlur(image_array_grey_buffer, 61)
        
        # Dilate image 
        kernel = np.ones((11,11), np.uint8)
        img_median_dilate = cv2.dilate(img_median, kernel, iterations = 1) 
        
               
        # Gauusian filter
        image_median_dilate_gaussian = cv2.GaussianBlur(img_median_dilate,(9,9), 1) 
        
        # Segement image: Using Region Based water shed algorithm
        
        #Edge detection sobel Filter
        elevation_map_median_dilate_gaussian = sobel(image_median_dilate_gaussian)
        
        # Markers
        markers = np.zeros_like(image_median_dilate_gaussian)
        
        #This markes were chosen based on try and error, not sure if this are
        #correct
        markers[image_median_dilate_gaussian < 90] = 1
        markers[image_median_dilate_gaussian  > 115] = 2
        
        #Segmentation Watershed
        img_segmented = morphology.watershed(elevation_map_median_dilate_gaussian, markers)
        
       
        #append key and value to dictionary-----------------------------------
        images_dict[img_id] = img_segmented
        
    #Save segemented images in single file --------------------------------
        
    # Create a new HDF5 file
    file = h5py.File(f'{path2}/cancerous_cell_smears_grey_enhanced_and_segmentated.hdf5', "w")
        
    # Create a dataset for each image stored in the h5py file
    for key, value in images_dict.items():
            
        #Type 1
        if 'cyl' in key: 
            key = file.create_dataset(
                (f'class_cyl/image_{key}'), np.shape(value), h5py.h5t.STD_U8BE, data=value)
            
        #Type 2
        elif 'inter' in key:
            key = file.create_dataset(
                (f'class_inter/image_{key}'), np.shape(value), h5py.h5t.STD_U8BE, data=value)
            
        #Type 3
        elif 'let' in key:
            key = file.create_dataset(
                (f'class_let/image_{key}'), np.shape(value), h5py.h5t.STD_U8BE, data=value)
            
        #Type 4
        elif 'mod' in key:
            key = file.create_dataset(
                (f'class_mod/image_{key}'), np.shape(value), h5py.h5t.STD_U8BE, data=value)
            
        #Type 5
        elif 'para' in key:
            key = file.create_dataset(
                (f'class_para/image_{key}'), np.shape(value), h5py.h5t.STD_U8BE, data=value)
            
        #Type 6  
        elif 'super' in key:
            key = file.create_dataset(
                (f'class_super/image_{key}'), np.shape(value), h5py.h5t.STD_U8BE, data=value)
            
        #Type 7
        elif 'svar' in key:
            key = file.create_dataset(
                (f'class_svar/image_{key}'), np.shape(value), h5py.h5t.STD_U8BE, data=value)
            
            
        #Prin how many images were read and id of each one    
        print(f'\n{len(images_dict)} images were read:')
        for key in images_dict:
            print(f'\t- {key}')    
        
        print(f'\nThe cancerous_cell_smears.hdf5 file was save on: ')
        print(f'\n{path2}')
        
    
path1 = '/home/ecamo19/Documents/cursos_libros_tutoriales/cursos/VCU/image_analysis/project/cancerous_cell_smears'
path2 ="/home/ecamo19/Documents/cursos_libros_tutoriales/cursos/VCU/image_analysis/project/part_3"

images_enhaged_segmented_to_hdf5(path1,path2)

# #Read h5py file and one image for testing

# #Get image from dataset
# hdf = h5py.File(f'{path2}/cancerous_cell_smears_grey_test.hdf5','r') 

# #Image that I want    
# img = 'image_super38.BMP'
# for i in hdf:
#         group = hdf.get(i) 
#         #print(group)        
#         if img in group:
#             image_array = np.array(group.get(img)) 
#             break
    
# #Save image for use put pixel funtion
# Image.fromarray(image_array.astype(np.uint8))

