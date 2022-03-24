#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 10:52:37 2021

@author: ecamo19
"""
#Modules ----------------------------------------------------------------------
import argh
import numpy as np 
import matplotlib.pyplot as plt 
import random
import h5py
from PIL import Image

#------------------------------------------------------------------------------
def get_closest_centroid(x, centroids):
        # Initialise the list to keep distances from each centroid
        centroid_distances = [] 
        
        # Loop over each centroid and compute the distance from data point.
        for centroid in centroids:
            dist = compute_l2_distance(x, centroid)
            centroid_distances.append(dist)
        
        # Get the index of the centroid with the smallest distance to the data point 
        closest_centroid_index =  min(range(len(centroid_distances)), 
                                      key=lambda x: centroid_distances[x])
        
        return closest_centroid_index

def compute_l2_distance(x, centroid):
    # Initialise the distance to 0
    dist = 0
        
    # Loop over the dimensions. Take sqaured difference and add to dist
    for i in range(len(x)):
            dist += (centroid[i] - x[i])**2
            return dist

def compute_sse(data, centroids, assigned_centroids):
        
    # Initialise SSE 
        sse = 0
        
        # Compute the squared distance for each data point and add. 
        for i,x in enumerate(data):
        	# Get the associated centroid for data point
            centroid = centroids[assigned_centroids[i]]
                    
            # Compute the Distance to the centroid
            dist = compute_l2_distance(x, centroid)
            
            # Add to the total distance
            sse += dist
        
        sse /= len(data)
        return sse
#------------------------------------------------------------------------------

    

def slow_k_means(img,k = 3, num_iters = 50, path_h5py_file = None):
    """
    Name: slow_k_means()
    
    Description:
        This function was build following the tutorials from:
                https://towardsdatascience.com/a-complete-k-mean-clustering-algorithm-from-scratch-in-python-step-by-step-guide-1eb05cdcd461

                https://blog.paperspace.com/speed-up-kmeans-numpy-vectorization-broadcasting-profiling/

        
        The function slow_k_means() is a clustering method. This function returns a plot with the 
        image segmented by the number of clusters selected (k) and a plot with the SSE.
        
        
        This function takes three arguments:
            
            + img: Name of the array inside the h5py file.
            The names of the images follow the notation image_tag.BMP e.g. image_svar99.BMP
            + path_h5py_file: Directory file path where a h5py file is stored locally.
            + k = Number of centroids desired 
            + num_iters: Number of iterations.
            
            
        For more information and how the k-means algorithm works please read the 
        book Applied UnsupervisedLearning with Python by 
        Benjamin Johnston, Aaron Jones, and Christopher Kruger
    """
    #Load h5py File         
    hdf = h5py.File(f'{path_h5py_file}/cancerous_cell_smears.hdf5','r')
    for each_group in hdf:
        group = hdf.get(each_group) 
            
        if img in set(group):
            img_array = np.array(group.get(img))[:,:,0]
            print(img_array)
            break
    
    
    #Use grey channel
    img_array_grey = img_array
    
    #reshape array to one dimension
    img_array_grey_reshaped = img_array_grey.reshape(img_array_grey.shape[0]*img_array_grey.shape[1],1)
    
    #K-means main algorithm --------------------------------------------------
    
    # Initialise the list to store centroids
    centroids = []
    
    # Sample initial centroids
    random_indices = random.sample(range(img_array_grey_reshaped.shape[0]), k)
    
    for i in random_indices:
        centroids.append(img_array_grey_reshaped[i])
    
    # Create a list to store which centroid is assigned to each dataset
    assigned_centroids = [0] * len(img_array_grey_reshaped)
    
    # Number of dimensions in centroid
    num_centroid_dims = img_array_grey_reshaped.shape[1]
    
    # List to store SSE for each iteration 
    sse_list = []
        
    # Loop over iterations
    for n in range(num_iters):
        
        # Loop over each data point
        for i in range(len(img_array_grey_reshaped)):
            x = img_array_grey_reshaped[i]
            
            # Get the closest centroid
            closest_centroid = get_closest_centroid(x, centroids)
            
            # Assign the centroid to the data point.
            assigned_centroids[i] = closest_centroid
        
        # Loop over centroids and compute the new ones.
        for c in range(len(centroids)):
            
            # Get all the data points belonging to a particular cluster
            cluster_data = [img_array_grey_reshaped[i] for i in range(len(img_array_grey_reshaped)) if assigned_centroids[i] == c]
        
            # Initialise the list to hold the new centroid
            new_centroid = [0] * len(centroids[0])
            
            # Compute the average of cluster members to compute new centroid
            # Loop over dimensions of data
            
            for dim in range(num_centroid_dims): 
                dim_sum = [x[dim] for x in cluster_data]
                dim_sum = sum(dim_sum) / len(dim_sum)
                new_centroid[dim] = dim_sum
                
            # assign the new centroid
            centroids[c] = new_centroid
            
        # Compute the SSE for the iteration
        sse = compute_sse(img_array_grey_reshaped, centroids, assigned_centroids)
        sse_list.append(sse)
    
    #SSE plot
    plt.figure()
    plt.xlabel("Iterations")
    plt.ylabel("SSE")
    plt.plot(range(len(sse_list)), sse_list)
    plt.show()
        
    #Segmented image
    centers = np.uint8(centroids)
    segmented_image = centers[assigned_centroids]
    segmented_image = segmented_image.reshape(img_array_grey.shape[0],img_array_grey.shape[1])
    plt.imshow(Image.fromarray(segmented_image),cmap="gray")  


if __name__ == '__main__':
    argh.dispatch_command(slow_k_means)
    
# Function test --------------------------------------------------------------
path_h5py = '/home/ecamo19/Documents/cursos_libros_tutoriales/cursos/VCU/image_analysis/project/part_2' 
slow_k_means('image_cyl07.BMP',  k = 4, num_iters = 10, path_h5py_file = path_h5py)
slow_k_means('image_inter07.BMP',k = 4, num_iters = 10, path_h5py_file = path_h5py)
slow_k_means('image_let07.BMP',  k = 4, num_iters = 10, path_h5py_file = path_h5py)
slow_k_means('image_mod07.BMP',  k = 4, num_iters = 10, path_h5py_file = path_h5py)
slow_k_means('image_para07.BMP', k = 4, num_iters = 10, path_h5py_file = path_h5py)
slow_k_means('image_super07.BMP',k = 4, num_iters = 10, path_h5py_file = path_h5py)
slow_k_means('image_svar07.BMP', k = 4, num_iters = 10, path_h5py_file = path_h5py)



