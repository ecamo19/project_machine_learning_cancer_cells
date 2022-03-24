#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 10:44:22 2021

@author: ecamo19
"""
import numpy as np
import argparse
import cv2
from PIL import Image
import h5py



def list_dataset(name,node):
    if isinstance(node, h5py.Dataset):
            print(f'\t-{name}')



def images_available_for_analisys(path_h5py_file):
    
            #save data in the environment
            #global  cancer_images_hdf5
    
            #Read data file
            #cancer_images_hdf5 = h5py.File(f'{path}/cancer_images.hdf5','r')   
            with h5py.File(f'{path_h5py_file}/cancerous_cell_smears.hdf5','r' ) as cancer_images_hdf5:
                 base_items = list(cancer_images_hdf5.items())
    
            
            #Print each class loaded
            
                 print('\nImages clases loaded:')
                 for key,value in base_items:
                     print(f'\t-{key}')

            #Print the files load
                 print(f'\nImages available for analisys:')
                 cancer_images_hdf5.visititems(list_dataset)
                
#Test function-----------------------------------------------------------------
path = "/home/ecamo19/Documents/cursos_libros_tutoriales/cursos/VCU/image_analysis/project/part_1/"
images_available_for_analisys(path_h5py_file = path) 
                
                
                
                
                
                
                