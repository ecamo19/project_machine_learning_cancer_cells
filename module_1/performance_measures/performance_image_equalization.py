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
from image_functions.equalization_for_each_image import *



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
        
        equalization_hist(grey_image_array)
        
  
#Performace measures-----------------------------------------------------------

#Processing time for the entire batch 
print("--- %s seconds ---" % (time.time() - start_time))

#Averaged processing time per image per each procedure
print((time.time() - start_time)/499) 

#Result
# --- 2489.9639978408813 seconds ---
# 4.989908055934256



