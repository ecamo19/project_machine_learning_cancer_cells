# Project: Cancer cell detection using machine learning techniques

**This project was developed for the Image Analysis course from the Computing science Department at Virgiania Commonwealth University

**The data versioning of the hdf5 files was done using git lfs

## Module 1

In this module the following functions where develop

### Raw image processing 

+ store_BMP_images_as_h5py: This function takes a batch of images and creates a single file of arrays  
+ images_available_for_analysis: Searches in a folder the images available

### Noise reduction 

+ Salt and pepper noise for removing this kind 
+ Gaussian noise of user-specified parameters
+ Median filter 
+ averaged_linear_filter

### Image processing 

+ extract_color_channels: Convert color images to selected single color spectrum
+ averaged_histogram_for_each_class
+ histogram_for_each_image.py: Checks the distribution of pixel values in a image

## Module 2

This module was developed for implementing several techniques to segment an image

### Image segmentation

+ edge_detection: Implement the edge detection algorithm.

+ kmeans_segmentation: Uses the k-means algorithm for segmenting a image

## Module 3

In this module I develop a Machine Learning workflow for detecting cancer cells.

![alt text](./module_3/results//diagram.png)



