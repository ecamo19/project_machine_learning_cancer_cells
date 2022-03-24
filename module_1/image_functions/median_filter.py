#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Main code from:
#https://www.pyimagesearch.com/2016/07/25/convolutions-with-opencv-and-python/

from skimage.exposure import rescale_intensity
import numpy as np
import cv2
from PIL import Image
import h5py


def median_convolve(img,mask_size, path,pixel_weights = [1]): 
    
    global kernel
    if mask_size % 2 != 0:
         
        
         #  #Get image from dataset
         # hdf = h5py.File(f'{path}/cancerous_cell_smears.hdf5','r') 
    
         # for i in hdf:
         #    group = hdf.get(i) 
         #    if img in group:
         #        image_array = np.array(group.get(img)) 
         #        break
        
          #Save array as image for use put pixel funtion
         image_rgb = Image.fromarray(image_array.astype(np.uint8))
    
          #Convert image to grayscale and get the array		
         image = image_rgb.convert("L")
         image = np.array(image)
         
          #Build the kernel or mask
         
         #nonlocal mean_kernel
         
         if int(mask_size) != len(str(pixel_weights)) and pixel_weights != [1]: 
                 print("")
                 print(f'\t-Please provide a vector with the pixel weights of lenght equals to {mask_size}')
         
         elif int(mask_size) != len(str(pixel_weights)) and pixel_weights == [1]:
                 
                 average_kernel =  (1/(int(mask_size)*int(mask_size))) * (np.ones((int(mask_size),int(mask_size)), dtype="int"))   
               #print(kernel)
         else:
              
                 average_kernel = (1/(int(mask_size)*int(mask_size))) * (np.ones((int(mask_size),int(mask_size)), dtype="int") * [pixel_weights]) 

          # grab the spatial dimensions of the image
	       # grab the spatial dimensions of the kernel

         (i_height, i_width) = image.shape[:2]
         (k_height, k_width) = average_kernel.shape[:2]
         
          #replicating the pixels along the border of the image
         pad = (k_width - 1) // 2
    
          #Load image
         image = cv2.copyMakeBorder(image, pad, pad, pad, pad,cv2.BORDER_REPLICATE)
         output = np.zeros((i_height, i_width), dtype="float32")
         
        # loop over the input image, sliding the kernel across
       	# each (x, y)-coordinate from left-to-right and top to
 	    # bottom
    
        #“sliding” the kernel from left-to-right and top-to-bottom 
        #1 pixel at a time.

         
         for y in np.arange(pad, i_height + pad):
              for x in np.arange(pad, i_width + pad):
                 
            #Region of Interest (ROI)
 			# Extract the ROI of the image by extracting the
 			# *center* region of the current (x, y)-coordinates
 			# dimensions 

                  roi = image[y - pad:y + pad + 1, x - pad:x + pad + 1]
            
            # perform the actual convolution by taking the
 			# element-wise multiplicate between the ROI and
 			# the kernel, then summing the matrix
                     
                  k =  (roi * np.median(average_kernel)).sum()
                 
                   
            # store the convolved value in the output (x,y)
 			# coordinate of the output image
                
                  output[y - pad, x - pad] = k
                 
            # rescale the output image to be in the range [0, 255]                 
         output = rescale_intensity(output, in_range=(0, 255))
         output = (output * 255).astype("uint8")
         output_grey = Image.fromarray(output.astype(np.uint8))
         
          # return the output image
         return output_grey.show()
     
    else:
            print("")
            print(f'\t-Mask size should be an odd integer number')
         

#Test Function ---------------------------------------------------------------            
#path_h5py = "/home/ecamo19/Documents/cursos_libros_tutoriales/cursos/VCU/image_analysis/project/part_1/"
# images_available_for_analisys(path_h5py_file = path_h5py)

# path1 = "/home/ecamo19/Documents/cursos_libros_tutoriales/cursos/VCU/image_analysis/project/part_1"
# median_convolve('image_cyl03.BMP', mask_size = 9M , path=path1, pixel_weights = [1])
# 		



