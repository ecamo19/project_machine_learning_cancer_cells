#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 10:52:37 2021

@author: ecamo19
"""

#This code was develop using the code from:
#https://medium.com/@ami25480/morphological-image-processing-operations-dilation-erosion-opening-and-closing-with-and-without-c95475468fca

import numpy as np
import argh
from PIL import Image
from matplotlib import pyplot as plt


@argh.arg('erosion_level',choices=[3,7,9,11])
def erode_image(image_array_binary, erosion_level = 3):
   """
    Name: erode_image
    
    Description:
        This function was build following the tutorial from:
            https://medium.com/@ami25480/morphological-image-processing-operations-dilation-erosion-opening-and-closing-with-and-without-c95475468fca
 
        The function erode_imageis a morphological operation that takes a binary
        image and returns a plot.
        
        his function takes two arguments:
            + img_array_binary: Is an array from of a binary image. 
            The binary image can be obtain using the funtion called otsu_thresholding()
            
            + erosion_level: Level of erosion desired
          
          
        For more information and how the sobel algorithm works please read chapter 9 from the book 
        Image Processing and Acquisition using Python by Ravishankar Chityala and Sridevi Pudipeddi
        
    """
   
   m,n = image_array_binary.shape
    
    # Define the structuring element
    # k= 11,15,45 -Different sizes of the structuring element 
    
   k = erosion_level
   se = np.ones((k,k), dtype=np.uint8)
   constant = (k-1)//2
    
    #Define new image
   img_erode = np.zeros((m,n), dtype=np.uint8)


   #Erosion operation
   for i in range(constant, m-constant):
       for j in range(constant,n-constant):
            temp = image_array_binary[i-constant:i+constant+1, j-constant:j+constant+1]
            product= temp*se
            img_erode[i,j] = np.min(product)
    
   plt.imshow(img_erode,cmap="gray")



if __name__ == '__main__':
    argh.dispatch_commands(erode_image)


#Funtion test------------------------------------------------------------------ 
erode_image(img_binary)


    

