# Project Cancer cell identification using machine learning techniques

This project was developed for the Image Analysis from the Computing science department at Virgiania Commonwealth University

## Module 1

In this module the following functions where develop

### Raw image processing 

+ store_BMP_images_as_h5py: This function takes a batch of images and creates a single file pf arrays  
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

+ This module was develop for using several techniques to segment an image
+ Implement dilation and erosion operators
+ Implement two segmentation techniques (they must be implemented by you, not API calls):
  histogram thresholding – single threshold that divides image into two segments: foreground (cells) and background (everything else)

+ clustering (k-means recommended, examine the effect of different values of k parameter on the
segmentation)

### Image segmentation

+ Implement one selected edge detection algorithm.

## Module 3
