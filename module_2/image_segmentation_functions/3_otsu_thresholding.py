#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 10:52:37 2021

@author: ecamo19
"""

#Modules ----------------------------------------------------------------------
import argh
import numpy as np
from PIL import Image
import cv2
import matplotlib.pyplot as plt
import h5py
#------------------------------------------------------------------------------

def otsu_thresholding(img, path_h5py_file = None): 
    """
    Name: otsu_thresholding
    
    Description:
        This function was build following the tutorial from:
            https://theailearner.com/tag/otsu-method-opencv/
        
        The function otsu_thresholding() is a threshold selection method from 
        gray level histogram. This function returns a plot with the binarized 
        image and array called img_binary that cam be used with other functions.
        
        It is important to mention that the Otsu algorithm works best if the 
        histogram of the image is bimodal.
        
        This function takes three arguments:
            
            + img: Name of the array inside the h5py file.
            The names of the images follow the notation image_tag.BMP e.g. image_svar99.BMP
            + path_h5py_file: Directory file path where a h5py file is stored locally.
        
        For more information and how the Otsu algorithm works please read chapter 
        8 from the book Image Processing and Acquisition using Python by 
        Ravishankar Chityala and Sridevi Pudipeddi
    """
    
    #Load h5py File         
    hdf = h5py.File(f'{path_h5py_file}/cancerous_cell_smears.hdf5','r')
    for each_group in hdf:
        group = hdf.get(each_group) 
            
        if img in set(group):
            img_array = np.array(group.get(img))[:,:,0]
            print(img_array)
            break
             
    # Set minimum value to infinity
    final_min = np.inf
        
    #Calculate hist for later use    
    hist = plt.hist(img_array.ravel(),255,[0,255]) 
    plt.show()
    
    # total pixels in an image
    total = np.sum(hist[0])
    
    for each_bin in range(256):
        
        # Split regions based on threshold
        left, right = np.hsplit(hist[0],[each_bin])
        
        # Splt intensity values based on threshold
        left_bins, right_bins = np.hsplit(hist[1],[each_bin])
        
        # Only perform thresholding if neither side empty
        if np.sum(left) !=0 and np.sum(right) !=0:
            
            # Calculate weights on left and right sides
            w_0 = np.sum(left)/total
            w_1 = np.sum(right)/total
            
            # Calculate the mean for both sides
            mean_0 = np.dot(left,left_bins)/np.sum(left)
            mean_1 = np.dot(right,right_bins[:-1])/np.sum(right)  # right_bins[:-1] because matplotlib has uses 1 bin extra
            
            # Calculate variance of both sides
            var_0 = np.dot(((left_bins-mean_0)**2),left)/np.sum(left)
            var_1 = np.dot(((right_bins[:-1]-mean_1)**2),right)/np.sum(right)
            
            # Calculate final within class variance
            final = w_0*var_0 + w_1*var_1
            
            # if variance minimum, update it
            if final < final_min:
                final_min = final
                thresh2 = each_bin
  
    #Make binary image available for other functions        
    global img_binary
   
    # Get binary image
    img_binary = img_array
    img_binary[img_array > thresh2] = 255
    img_binary[img_array < thresh2] = 0
    
    #Invert image
    img_binary = np.invert(img_binary)
    
    #plot image
    plt.imshow(Image.fromarray(img_binary), cmap="gray")


if __name__ == '__main__':
    argh.dispatch_command(otsu_thresholding)
    

#Test function-----------------------------------------------------------------
path_h5py = '/home/ecamo19/Documents/cursos_libros_tutoriales/cursos/VCU/image_analysis/project/part_2' 
otsu_thresholding('image_cyl07.BMP',   path_h5py_file = path_h5py)
otsu_thresholding('image_inter07.BMP', path_h5py_file = path_h5py)
otsu_thresholding('image_let07.BMP',   path_h5py_file = path_h5py)
otsu_thresholding('image_mod07.BMP',   path_h5py_file = path_h5py)
otsu_thresholding('image_para07.BMP',  path_h5py_file = path_h5py)
otsu_thresholding('image_super07.BMP', path_h5py_file = path_h5py)
otsu_thresholding('image_svar07.BMP',  path_h5py_file = path_h5py)
