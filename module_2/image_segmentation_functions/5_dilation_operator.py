#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 10:52:37 2021

@author: ecamo19
"""

import numpy as np
import argh
from PIL import Image
from matplotlib import pyplot as plt


@argh.arg('img_array_binary', help = "Array of a binarized image")
def dilation_image(image_array_binary):
    """
    Name: delation_image
    
    Description:
        This function was build following the tutorial from:
            https://medium.com/@ami25480/morphological-image-processing-operations-dilation-erosion-opening-and-closing-with-and-without-c95475468fca
 
        The function delation() is a morphological operation that takes a binary
        image and returns a plot.
        
        This function takes one argument:
            + img_array_binary: Is an array from of a binary image. 
            The binary image can be obtain using the funtion called otsu_thresholding()
          
        For more information and how the sobel algorithm works please read chapter 9 from the book 
        Image Processing and Acquisition using Python by Ravishankar Chityala and Sridevi Pudipeddi
        
    """
    p,q= image_array_binary.shape
    
    #Empty image with the size of the original 
    img_dilate = np.zeros((p,q), dtype=np.uint8)
    
    #Kernel
    kernel = [[0,1,0], [1,1,1],[0,1,0]] #* (np.ones((int(3),int(3)), dtype="int"))
              
              
    #Dilation operation
    for i in range(1, p-1): 
        for j in range(1, q-1):
      
            temp = image_array_binary[i-1 : i+1+1, j-1 : j + 1 + 1]
            product = temp * kernel
            img_dilate[i,j] = np.max(product)
    
    plt.imshow(img_dilate, cmap="gray")

    
if __name__ == '__main__':
   argh.dispatch_command(dilation_image)
    
#Test code --------------------------------------------------------------------
dilation_image(img_binary)

