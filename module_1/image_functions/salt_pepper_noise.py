# -*- coding: utf-8 -*-

import numpy as np
from PIL import Image
import h5py


#Salt and peper funtion -------------------------------------------------------

#Salt and pepper noise definition

#Salt-and-pepper noise is characterized by black and white spots
#randomly distributed in an image

# This function adds noise of user-specified strengt to an 
#image by selecting pixels from the image randomly and then setting those 
#pixel values to black and the other to white.

#This function takes two arguments:
    # + img: This is a .png file 
    # + perc: This is an integer value between 0 and 100 that represents
    # the percentage of noise applied to the image


def salt_pepper(img,perc,path):
    
    perc = int(perc) 

     #Get image from dataset
    
    # hdf = h5py.File(f'{path}/cancerous_cell_smears.hdf5','r') 
    
    # for i in hdf:
    #     group = hdf.get(i) 
        
    #     if img in group:
    #         image_array = np.array(group.get(img)) 
    #         break
        
    # #Save array as image for use put pixel funtion
    image = Image.fromarray(image_array.astype(np.uint8))
    
    # #Convert grayscale image		
    image = image.convert("L")

    if perc == None  :
        print("\nPlease specify the percentage of salt and pepper that you want"
              " Range: 0-100%")
     
    else:
        
        #Select number of of pixels
        n = int(((image_array.shape[0]*image_array.shape[1])*perc)/100)
        
        #Sample pixels randomly
        x, y = np.random.randint(0,image_array.shape[1], n),np.random.randint(0,image_array.shape[0],n)
        
        #Save array as image for use put pixel funtion
        image = Image.fromarray(image_array.astype(np.uint8))
        
        for (x,y) in zip(x,y):
            if np.random.rand() < 0.5:
                image.putpixel((x,y),0)
       
            else:
                image.putpixel((x,y), 255)
        
        return  image.show()               
                
#Function test ----------------------------------------------------------------
path1 = "/home/ecamo19/Documents/cursos_libros_tutoriales/cursos/VCU/image_analysis/project/part_1"
# salt_pepper('image_inter38.BMP', perc = 50, path=path1) 






























