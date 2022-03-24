#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Averaged histograms of pixel values for each class of images.


import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
sns.set_style("white")

#Code example 
#https://realpython.com/storing-images-in-python/



#Class of images
# 50 columnar epithelial cells
# 50 parabasal squamous epithelial cells
# 50 intermediate squamous epithelial cells
# 50 superficial squamous epithelial cells
# 100 mild nonkeratinizing dysplastic cells
# 100 moderate nonkeratinizing dysplastic cells
# 100 severe nonkeratinizing dysplastic cells


#Plot arrays ------------------------------------------------------------------

def plot_density_cancer_cells(classe, array):
        
        classe = classe.lower()
                
        if classe == 'cyl':
         
            plot_cyl = sns.distplot(array, hist=True, 
                                    kde=True, bins=45, color = "dodgerblue",
                                    kde_kws={'linewidth': 2})
            

            plot_cyl.set(xlim=(0, 256), xlabel="Pixel Value", title="Class Cyl")
            plt.show()

        elif classe == 'inter':
            
            plot_inter = sns.distplot(array, hist=True, 
                                    kde=True, bins=45, color = "dodgerblue",
                                    kde_kws={'linewidth': 2})


            plot_inter.set(xlim=(0, 256), xlabel="Pixel Value", title="Class Inter")
            plt.show()
            
        elif classe == 'let':
            
            plot_let = sns.distplot(array, hist=True, 
                                    kde=True, bins=45, color = "dodgerblue",
                                    kde_kws={'linewidth': 2})


            plot_let.set(xlim=(0, 256), xlabel="Pixel Value", title="Class Let")
            plt.show()
            
        elif classe == 'mod':
            
            plot_mod = sns.distplot(array, hist=True, 
                                    kde=True, bins=45, color = "dodgerblue",
                                    kde_kws={'linewidth': 2})


            plot_mod.set(xlim=(0, 256), xlabel="Pixel Value", title="Class Mod")
            plt.show()
             
        elif classe == 'para':
            
            plot_para = sns.distplot(array, hist=True, 
                                    kde=True, bins=45, color = "dodgerblue",
                                    kde_kws={'linewidth': 2})


            plot_para.set(xlim=(0, 256), xlabel="Pixel Value", title="Class Para")
            plt.show()
            
        elif classe == 'super':
            
            plot_super = sns.distplot(array, hist=True, 
                                    kde=True, bins = 30, color = "dodgerblue",
                                    kde_kws={'linewidth': 2})


            plot_super.set(xlim=(0, 256), xlabel="Pixel Value", title="Class Super")
            plt.show()
            
        elif classe == 'svar':
         
            plot_svar = sns.distplot(array, hist=True, 
                                    kde=True, bins=45, color = "dodgerblue",
                                    kde_kws={'linewidth': 2})


            plot_svar.set(xlim=(0, 256), xlabel="Pixel Value", title="Class Svar")
            plt.show()
            
        else:
            print(f'{classe} is not available please seleted a class from:')
            print(f'\t-cyl')
            print(f'\t-inter')
            print(f'\t-let')
            print(f'\t-mod')
            print(f'\t-para')
            print(f'\t-super')
            print(f'\t-svar')
            

#Test code -------------------------------------------------------------------        
#plot_density_cancer_cells('cyl')




