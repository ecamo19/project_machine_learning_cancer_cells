#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import h5py
import numpy as np
import os
import glob
import cv2
import argh


def images_to_hdf5(path1, path2):
    """
    Name: images_to_hdf5
    
    Description:
        This function takes several .BMP images and save them as arrays in a 
        single hdf5 file. 
        
        Path2 where the hdf5 file will be saved
        the path where the images are,
        read them
            
        This function takes two arguments:
            + path1: The path to the folder where all the .BMP images are stored
            + path2: Path where the hdf5 file will be saved locally.
    """
    
    # Create empty dictionary for storing images and ids
    images_dict = {}
    
    for file in glob.glob(f"{path1}/*.BMP"):
    
        #Get image id
        img_id = os.path.basename(file)
    
        #Read the image
        img = cv2.imread(file)
       
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
    
    print(f'\nThe cancerous_cell_smears_grey.hdf5 file was save on: ')
    print(f'\n{path2}')

if __name__ == '__main__':
    argh.dispatch_command(images_to_hdf5)
    

#Test function----------------------------------------------------------------- 
path1= '/home/ecamo19/Documents/cursos_libros_tutoriales/cursos/VCU/image_analysis/project/part_2/cancerous_cell_smears'
path2='/home/ecamo19/Documents/cursos_libros_tutoriales/cursos/VCU/image_analysis/project/part_2'
images_to_hdf5(path1,path2)

