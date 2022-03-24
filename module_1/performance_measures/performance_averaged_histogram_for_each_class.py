#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 16:03:21 2021

@author: ecamo19
"""
#from modules.validate import *

import h5py
import numpy as np
from PIL import Image
import time
from image_functions.averaged_histogram_for_each_class import *

#Processing time---------------------------------------------------------------
start_time = time.time()

#Path where the h5py file is stored--------------------------------------------
path = "/home/ecamo19/Documents/cursos_libros_tutoriales/cursos/VCU/image_analysis/project/part_1"


#Read the hdf5 file------------------------------------------------------------ 
hdf = h5py.File(f'{path}/cancerous_cell_smears.hdf5','r') 


#Run Function------------------------------------------------------------------

for group_name in hdf:
    group = hdf.get(group_name) 
    
    for i in group:

        #Create empty arrays for use in the plots
        histograms_cyl = np.array([])
        histogram_inter = np.array([])
        histogram_let = np.array([])
        histogram_mod = np.array([])
        histogram_para = np.array([])
        histogram_svar = np.array([])
        histogram_super = np.array([])
        
        
        if 'cyl' in i:
            
            array_img_cyl = np.array(group.get(i))  
            #Extract grey channel
            array_img_cyl = array_img_cyl[:,:,0]            
            
            histograms_plot_cyl = np.append(histograms_cyl, array_img_cyl)
               
        elif 'inter' in i:
            
            array_img_inter = np.array(group.get(i))
            #Extract grey channel
            array_img_inter = array_img_inter[:,:,0]
            
            histograms_plot_inter = np.append(histogram_inter, array_img_inter)
            
            
        elif 'let' in i:
            
            array_img_let = np.array(group.get(i))       
            #Extract grey channel
            array_img_let = array_img_let[:,:,0]
            
            
            histograms_plot_let = np.append(histogram_let, array_img_let)
            
                         
        elif 'mod' in i:
            
            array_img_mod = np.array(group.get(i))       
            #Extract grey channel
            array_img_mod = array_img_mod[:,:,0]
            
            histograms_plot_mod = np.append(histogram_mod, array_img_mod)
        
        elif 'para' in i:
            
            array_img_para = np.array(group.get(i))       
            #Extract grey channel
            array_img_para = array_img_para[:,:,0]
            
            histograms_plot_para = np.append(histogram_mod, array_img_para)
        
        elif 'super' in i:
            
            array_img_super = np.array(group.get(i))       
            #Extract grey channel
            array_img_super = array_img_super[:,:,0]
            
            histograms_plot_super = np.append(histogram_super, array_img_super)
        
        elif 'svar' in i:
            		
            array_img_svar = np.array(group.get(i))       
            #Extract grey channel
            array_img_svar = array_img_svar[:,:,0]
            
            histograms_plot_svar = np.append(histogram_svar, array_img_svar)

#Run plots---------------------------------------------------------------------

#Class cyl
plot_density_cancer_cells('cyl', array = histograms_plot_cyl )

#Class inter
plot_density_cancer_cells('inter', array = histograms_plot_inter)

#Class let
plot_density_cancer_cells('let', array = histograms_plot_let)

#Class mod
plot_density_cancer_cells('mod', array = histograms_plot_mod)

#Class para
plot_density_cancer_cells('para', array = histograms_plot_para)

#Class super
plot_density_cancer_cells('super', array = histograms_plot_super )

#Class svar
plot_density_cancer_cells('svar', array = histograms_plot_svar)


#Performace measures-----------------------------------------------------------

#Processing time for the entire batch 
print("--- %s seconds ---" % (time.time() - start_time))

#Averaged processing time per image per each procedure
print(f'Averaged processing time per image: {(time.time() - start_time)/499}')

#Result
# --- 21.026267290115356 seconds ---
# Averaged processing time per image: 0.04213698784669559


