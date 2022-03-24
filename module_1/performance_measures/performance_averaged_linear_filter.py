#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 16:03:21 2021

@author: ecamo19
"""
#from modules.validate import *

import h5py
import numpy as np
from PIL import Image
import time
from image_functions.averaged_linear_filter import *


#Processing time---------------------------------------------------------------
start_time = time.time()

#Path where the h5py file is stored--------------------------------------------
path = "/home/ecamo19/Documents/cursos_libros_tutoriales/cursos/VCU/image_analysis/project/part_1"


#Read the hdf5 file------------------------------------------------------------ 
hdf = h5py.File(f'{path}/cancerous_cell_smears.hdf5','r') 

#Run Function------------------------------------------------------------------
for group in hdf:
    
    group = hdf.get(group)         
    
    for image in group:
        #hdf.get(image) z
        image_array = np.array(group.get(image))
        
        #extract grey image
        grey_image_array = image_array[:,:,0]
                
        mean_convolve(grey_image_array, mask_size = 3, pixel_weights = [1])
        
        
  
#Performace measures-----------------------------------------------------------

#Processing time for the entire batch 
print("--- %s seconds ---" % (time.time() - start_time))

#Averaged processing time per image per each procedure
print(((time.time() - start_time))/499) 

#Result
# --- 3059.4868488311768 seconds ---
# 6.131236375453238
