#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 10:52:37 2021

@author: ecamo19
"""


#Modules used ----------------------------------------------------------------
import numpy as np
import argh
from PIL import Image
from matplotlib import pyplot as plt
from skimage.exposure import rescale_intensity
import h5py
import cv2
#------------------------------------------------------------------------------

@argh.arg('img_array', help = "Array of an image or name of the array inside a h5py file")
@argh.arg('direction', choices = ['vertical','horizontal'], help = "Direction on which the filter operates")
def sobel(img,direction, path_h5py_file = None): 
  
    """
    Name: sobel()
    
    Description:
        This function was build following the tutorial from:
            https://www.pyimagesearch.com/2016/07/25/convolutions-with-opencv-and-python/
        
        The function sobel() is a edge detection function that takes a grey 
        image and returns a plot with the edges detected.
        
        This function takes three arguments:
             + img: Name of the array inside the h5py file.
            The names of the images follow the notation image_tag.BMP e.g. image_svar99.BMP
            
            + direction: Direction that the filter will work e.g. on a vertical 
            direction or a horizontal direction.
            + path_h5py_file: Directory file path where a h5py file is stored locally.
        
        For more information and how the sobel algorithm works please read chapter 4 from the book 
        Image Processing and Acquisition using Python by Ravishankar Chityala and Sridevi Pudipeddi
        
    """
    #Load h5py File         
    hdf = h5py.File(f'{path_h5py_file}/cancerous_cell_smears.hdf5','r')
    for each_group in hdf:
        group = hdf.get(each_group) 
            
        if img in set(group):
            img_array = np.array(group.get(img))[:,:,0]
            print(img_array)
            break
    
    
    global sobel_kernel
    #Create Kernels, Vertical and Horizontal     
    if direction== "horizontal":
        
        sobel_kernel =  [[-1,0,1], [-2,0,2], [-1,0,1]] * (np.ones((int(3),int(3)), dtype="int"))  
        #print(sobel_kernel)
    
    elif direction == "vertical":
        
        sobel_kernel = [[-1,-2,-1], [0,0,0], [1,2,1]] * (np.ones((int(3),int(3)), dtype="int"))
        #print(sobel_kernel)
               
    # grab the spatial dimensions of the image
    (i_height, i_width) = img_array.shape[:2]
   
    # grab the spatial dimensions of the kernel
    (k_height, k_width) = sobel_kernel.shape[:2]
         
    #replicating the pixels along the border of the image
    #IS PADDING NECESSARY?????
    pad = (k_width - 1) // 2
    
    #Load image
    image = cv2.copyMakeBorder(img_array, pad, pad, pad, pad,cv2.BORDER_REPLICATE)
    output = np.zeros((i_height, i_width), dtype="float32")

    # loop over the input image, sliding the kernel across
    # each (x, y)-coordinate from left-to-right and top to
 	# bottom
    #“sliding” the kernel from left-to-right and top-to-bottom 
    #1 pixel at a time.
    
    for y in np.arange(pad, i_height + pad):
        for x in np.arange(pad, i_width + pad):
                 
            #Region of Interest (ROI)
 			# # Extract the ROI of the image by extracting the
 			# # *center* region of the current (x, y)-coordinates
 			# # dimensions 
             
            roi = image[y - pad:y + pad + 1, x - pad:x + pad + 1]
            
            # perform the actual convolution by taking the
 			# # element-wise multiplicate between the ROI and
 			# # the kernel, then summing the matrix
                     
            k = (roi * sobel_kernel).sum()
                 
                   
            # store the convolved value in the output (x,y)-
 			# # coordinate of the output image
                
            output[y - pad, x - pad] = k
                 
    #rescale the output image to be in the range [0, 255]                 
    output = rescale_intensity(output, in_range=(0, 255))
    output = (output * 255).astype("uint8")
         
    # return the output image
    plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,2,4),plt.imshow(output,cmap = 'gray')
    

if __name__ == '__main__':
    argh.dispatch_command(sobel)

    
#Test Function ---------------------------------------------------------------            
path_h5py = '/home/ecamo19/Documents/cursos_libros_tutoriales/cursos/VCU/image_analysis/project/part_2' 
sobel('image_cyl07.BMP', direction = "horizontal", path_h5py_file = path_h5py)
sobel('image_inter07.BMP', direction = "horizontal", path_h5py_file = path_h5py)
sobel('image_let07.BMP', direction = "horizontal", path_h5py_file = path_h5py)
sobel('image_mod07.BMP', direction = "horizontal", path_h5py_file = path_h5py)
sobel('image_para07.BMP', direction = "horizontal", path_h5py_file = path_h5py)
sobel('image_super07.BMP', direction = "horizontal", path_h5py_file = path_h5py)
sobel('image_svar07.BMP', direction = "horizontal", path_h5py_file = path_h5py)



