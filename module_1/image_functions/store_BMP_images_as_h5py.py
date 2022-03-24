#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import h5py
import numpy as np
import os
import glob
import time
import cv2


#Processing time---------------------------------------------------------------
start_time = time.time()

#crear diccionary y lista

def images_to_hdf5(path1, path2):
    #This function takes the path where the images are, read them and save a
    # hdf5 file
    #Path2 where the hdf5 file will be saved
    
    
    # Create empty dictionary for storing images and ids
    images_dict = {}
    
    for file in glob.glob(f"{path1}/*.BMP"):
    
        #Get image id
        img_id = os.path.basename(file)
    
        #Read the image
        img = cv2.imread(file,0)
       
        #append key and value to dictionary
        images_dict[img_id] = img
        
    # Create a new HDF5 file
    file = h5py.File(f'{path2}/cancerous_cell_smears.hdf5', "w")
    
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


#Test function----------------------------------------------------------------- 
path1= '/home/ecamo19/Documents/cursos_libros_tutoriales/cursos/VCU/image_analysis/project/cancerous_cell_smears'
path2="/home/ecamo19/Documents/cursos_libros_tutoriales/cursos/VCU/image_analysis/project/part_3"

images_to_hdf5(path1,path2)

#Performace measures-----------------------------------------------------------


# #Processing time for the entire batch 
# print("--- %s seconds ---" % (time.time() - start_time))


# #Averaged processing time per image per each procedure
# print((time.time() - start_time)/499)

# #Result
# # The cancerous_cell_smears.hdf5 file was save on: 

# # /home/ecamo19/Documents/cursos_libros_tutoriales/cursos/VCU/image_analysis/project/part_1
# # --- 1.393442153930664 seconds ---
# # 0.0028107892535253615



