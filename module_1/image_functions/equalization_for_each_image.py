#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 16:12:29 2021

@author: ecamo19

"""

import numpy as np
from PIL import Image
import h5py
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style("white")

#Function definition
# The goal is to improve the contrast of an image by rescaling the histogram so 
# that the histogram of the new image is spread out and the pixel intensities 
# range over all possible gray-level values.
#The histogram of the input image is normalized so that the range of the 
#normalized histogram is [0, 1].

#Code made following the book called Image Processing and Acquisition using 
#Python pp-108


def equalization_hist(img,path): 
 #   Get image from dataset
    hdf = h5py.File(f'{path}/cancerous_cell_smears.hdf5','r') 
    
    for i in hdf:
        group = hdf.get(i) 
        
        if img in group:
            image_array = np.array(group.get(img)) 
            break
        else:
            print(f'image not found')
    
    
    #Save array as image 
    image = Image.fromarray(image_array.astype(np.uint8))
        
    #convert image to a 1D array.
    image_array_flat = image_array.flatten() 

    # Histogram and the bins of the image 
    hist,bins = np.histogram(image_array,256,[0,255])
   
    # cumulative distribution function 
    cdf = hist.cumsum()
    
    # Places where cdf=0 is masked or ignored and
    # rest is stored in cdf_m.
    cdf_m = np.ma.masked_equal(cdf,0)

    # Histogram equalization is performed.
    num_cdf_m = (cdf_m - cdf_m.min())*255
    den_cdf_m = (cdf_m.max()-cdf_m.min())
    cdf_m = num_cdf_m/den_cdf_m
    
    # The masked places in cdf_m are now 0.
    cdf = np.ma.filled(cdf_m,0).astype('uint8')

    
    # cdf values are assigned in the flattened array.
    image_cdf = cdf[image_array_flat] 
    
    image_equalized = np.reshape(image_cdf,image_array.shape)
    image_equalized = Image.fromarray(image_equalized)
    
    #Convert grayscale image		
    image_equalized = image_equalized.convert("L")
    
    #image_equalized.show()
    
    #Generate histogram pre and post

    fig, ax = plt.subplots(1,2, figsize=(12,7), sharex=True, sharey=True)
    ax[0].title.set_text(f' Image with no equalization')
    ax[1].title.set_text(f' Image with equalization')

    #Histogram of image before equalization
    sns.distplot(image, hist=True,kde=True, bins=45, color = "dodgerblue",
                 kde_kws={'linewidth': 2}, ax=ax[0])
    

    sns.distplot(image_equalized, hist=True,kde=True, bins=45, 
                 color = "dodgerblue",kde_kws={'linewidth': 2})  
   
#Test Function ---------------------------------------------------------------            
path1 = "/home/ecamo19/Documents/cursos_libros_tutoriales/cursos/VCU/image_analysis/project/part_1/"
equalization_hist("image_cyl03.BMP", path = path1)

    