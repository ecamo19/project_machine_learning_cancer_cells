#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Histogram calculation for each individual image.

from PIL import Image, ImageOps
import numpy as np
from matplotlib import pyplot as plt
import h5py

def hist_for_each_image(img, path): 
    
    #Get image from dataset
    hdf = h5py.File(f'{path}/cancerous_cell_smears.hdf5','r') 
    
    for i in hdf:
        group = hdf.get(i) 
        
        if img in group:
            image_array = np.array(group.get(img)) 
            break
        else:
            print(f'image not found')
    
    colors = ("red", "green", "blue")
    channel_ids = (0, 1, 2)

    plt.xlim([0, 256])
    
    for channel_id, color in zip(channel_ids, colors):
        
        #Generate Histogram
        histogram, bin_edges = np.histogram(
             image_array[:, :, channel_id], bins=256, range=(0, 256))
        
        plt.plot(bin_edges[0:-1], histogram, color=color)
        #plt.legend(['Red Channel', 'Green Channel', 'Blue Channel'])
        plt.title(f'Histgram for all the pixels')      
    
    plt.show()

#Function test ----------------------------------------------------------------
path1 = "/home/ecamo19/Documents/cursos_libros_tutoriales/cursos/VCU/image_analysis/project/part_1"
hist_for_each_image("image_cyl03.BMP", path=path1)






































