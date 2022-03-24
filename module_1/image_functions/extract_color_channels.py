#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from PIL import Image, ImageOps
import h5py

# Converting color images to selected single color spectrum function ----------   

# arr[..., 0]  # All Red values
# arr[..., 1]  # All Green values
# arr[..., 2]  # All Blue values

#Definition
#An image is an array  
# The amount of the primary color added is represented as an integer in the 
# closed range [0, 255]. Therefore, there are 256 discrete amounts of each 
# primary color that can be added to produce another color. The number of 
# discrete amounts of each color, 256, corresponds to the number of bits used 
# to hold the color channel value, which is eight (28=256). Since we have three 
# channels, this is called 24-bit color depth.


#Function
def extract_color(img,path,color = ...):
    
    #   Get image from dataset
       hdf = h5py.File(f'{path}/cancerous_cell_smears.hdf5','r')  
    
       for i in hdf:
            group = hdf.get(i) 
            
            if img in group:
                image_array = np.array(group.get(img)) 
                break
            # else:
            #     print(f'image not found')
        
    #     #Lower case color
       color_lower = color.lower()
       
        #Select channel
       if color_lower != "red" and color_lower != "green" and color_lower != "blue":
                print(f'\nPlease select a color channel that is Red, Green or Blue')
        
       elif color_lower == "red":
                
            # extract red channel
            red_channel =  image_array[:,:,0]

            # create empty image with same shape as the image
            red_img = np.zeros(image_array.shape)

            #assign the red channel of src to empty image
            red_img[:,:,0] = red_channel
            
            #Transform array to img
            img_single_color = Image.fromarray(red_img.astype(np.uint8))
            
            img_single_color.show()
         
       elif color_lower == "green":
                
            # extract red channel
            green_channel = image_array[:,:,1]

            # create empty image with same shape as the image
            green_img = np.zeros(image_array.shape)

            #assign the red channel of src to empty image
            green_img[:,:,1] = green_channel
            
            #Transform array to img
            img_single_color = Image.fromarray(green_img.astype(np.uint8))
            
            img_single_color.show()

       elif color_lower == "blue":
                
            # extract red channel
            blue_channel = image_array[:,:,2]

            # create empty image with same shape as the image
            blue_img = np.zeros(image_array.shape)

            #assign the red channel of src to empty image
            blue_img[:,:,2] = blue_channel
            
            #Transform array to img
            img_single_color = Image.fromarray(blue_img.astype(np.uint8))
        
            img_single_color.show()

#Function test ----------------------------------------------------------------
path1 = "/home/ecamo19/Documents/cursos_libros_tutoriales/cursos/VCU/image_analysis/project/part_1"
extract_color("image_inter38.BMP",path = path1 ,color = "green", )




