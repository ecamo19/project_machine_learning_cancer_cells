#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from PIL import Image, ImageOps
import h5py
#Gaussian noise function -----------------------------------------------------

# Gaussian noise definition
# Gaussian noise is the type of noise in which, at each pixel position (i, j), 
# the random noise value, that affects the true pixel value, is drawn from 
# Gaussian probability density function with mean μ(i, j) and standard 
# deviation σ(i, j). 


def gaussian_noise(img,perc,path, mean=0, std=1):
    
    #Get image from dataset
    hdf = h5py.File(f'{path}/cancerous_cell_smears.hdf5','r') 
    
    for i in hdf:
        group = hdf.get(i) 
        
        if img in group:
            image_array = np.array(group.get(img)) 
            break
        else:
            print(f'image not found')
    
    #Save image for use put pixel funtion
    image = Image.fromarray(image_array.astype(np.uint8))
    

    if perc == None  :
        print("\nPlease specify the percentage of noise that you want in the image"
              " Range: 0-100%")
     
    else:
        
        #Select n number of of pixels (percentage of noise)
        n = int(((image_array.shape[0]*image_array.shape[1])*perc)/100)
        
        #Sample pixels randomly
        x, y = np.random.randint(0,image_array.shape[1], n),np.random.randint(0,image_array.shape[0],n)
        
        #Sample a value from a gaussian distribution
        value_from_gaussian_dist1 = np.random.normal(mean, std)
        
        #use special normalization function for values out range 0-255 
        if value_from_gaussian_dist1 > 255 or value_from_gaussian_dist1 < 0:
            
            value_from_gaussian_dist = round((value_from_gaussian_dist1/(np.max(image_array) - np.min(image_array))) * 255) 

        else:
        
            value_from_gaussian_dist = round(value_from_gaussian_dist1)

            
        for (x,y) in zip(x,y):
            
                image.putpixel((x,y),value_from_gaussian_dist)
        
        return  image.show()  
    
    

#Test -------------------------------------------------------------------------
path1 = "/home/ecamo19/Documents/cursos_libros_tutoriales/cursos/VCU/image_analysis/project/part_1"
gaussian_noise("image_cyl03.BMP",perc = 50, path = path1,mean=5, std=2)
