#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 11 17:06:10 2021

@author: ecamo19
"""

# Modules --------------------------------------------------------------------
import re
import math
import numpy as np
import pandas as pd
import string
import scipy as sp
import nltk
import time
import operator
from random import randrange
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import warnings
warnings.filterwarnings('ignore')
# -----------------------------------------------------------------------------

# This code was develop following this tutorial:    
# https://towardsdatascience.com/build-knn-from-scratch-python-7b714c47631a



# Step 1: Class for calculating Euclidean metrics -----------------------------
class distanceMetrics:
    '''
    Description:
        This class contains methods to calculate various distance metrics
    '''
    def __init__(self):
        '''
        Description:
            Initialization/Constructor function
        '''
        pass
        
    def euclideanDistance(self, vector1, vector2):
        '''
        Description:
            Function to calculate Euclidean Distance
                
        Inputs:
            vector1, vector2: input vectors for which the distance is to be calculated
        Output:
            Calculated euclidean distance of two vectors
        '''
        self.vectorA, self.vectorB = vector1, vector2
        if len(self.vectorA) != len(self.vectorB):
            raise ValueError("Undefined for sequences of unequal length.")
        distance = 0.0
        for i in range(len(self.vectorA)-1):
            distance += (self.vectorA[i] - self.vectorB[i])**2
        return (distance)**0.5


# Step 2: Predict -------------------------------------------------------------
class kNNClassifier:
    '''
    Description:
        This class contains the functions to calculate distances
    '''
    def __init__(self,k = 3, distanceMetric = 'euclidean'):
        '''
        Description:
            KNearestNeighbors constructor
        Input    
            k: total of neighbors. Defaulted to 3
            distanceMetric: type of distance metric to be used. Defaulted to euclidean distance.
        '''
        pass
    
    def fit(self, xTrain, yTrain):
        '''
        Description:
            Train kNN model with x data
        Input:
            xTrain: training data with coordinates
            yTrain: labels of training data set
        Output:
            None
        '''
        assert len(xTrain) == len(yTrain)
        self.trainData = xTrain
        self.trainLabels = yTrain

    def getNeighbors(self, testRow):
        '''
        Description:
            Train kNN model with x data
        Input:
            testRow: testing data with coordinates
        Output:
            k-nearest neighbors to the test data
        '''
        
        calcDM = distanceMetrics()
        distances = []
        for i, trainRow in enumerate(self.trainData):
            if self.distanceMetric == 'euclidean':
                distances.append([trainRow, calcDM.euclideanDistance(testRow, trainRow), self.trainLabels[i]])
            elif self.distanceMetric == 'manhattan':
                distances.append([trainRow, calcDM.manhattanDistance(testRow, trainRow), self.trainLabels[i]])
            elif self.distanceMetric == 'hamming':
                distances.append([trainRow, calcDM.hammingDistance(testRow, trainRow), self.trainLabels[i]])
            distances.sort(key=operator.itemgetter(1))

        neighbors = []
        for index in range(self.k):
            neighbors.append(distances[index])
        return neighbors
        
    def predict(self, xTest, k, distanceMetric):
        '''
        Description:
            Apply kNN model on test data
        Input:
            xTest: testing data with coordinates
            k: number of neighbors
            distanceMetric: technique to calculate distance metric
        Output:
            predicted label 
        '''
        self.testData = xTest
        self.k = k
        self.distanceMetric = distanceMetric
        predictions = []
        
        for i, testCase in enumerate(self.testData):
            neighbors = self.getNeighbors(testCase)
            output= [row[-1] for row in neighbors]
            prediction = max(set(output), key=output.count)
            predictions.append(prediction)
        
        return predictions
    
# Get Metrics -----------------------------------------------------------------

def printMetrics(actual, predictions):
    '''
    Description:
        This method calculates the accuracy of predictions
    '''
    assert len(actual) == len(predictions)
    correct = 0
    for i in range(len(actual)):
        if actual[i] == predictions[i]:
            correct += 1
    return (correct / float(len(actual)) * 100.0)

# Cross Validation function ---------------------------------------------------

class kFoldCV:
    '''
    This class is to perform k-Fold Cross validation on a given dataset
    '''
    def __init__(self):
        pass
    
    def crossValSplit(self, dataset, numFolds):
        '''
        Description:
            Function to split the data into number of folds specified
        Input:
            dataset: data that is to be split
            numFolds: integer - number of folds into which the data is to be split
        Output:
            split data
        '''
        dataSplit = list()
        dataCopy = list(dataset)
        foldSize = int(len(dataset) / numFolds)
        for _ in range(numFolds):
            fold = list()
            while len(fold) < foldSize:
                index = randrange(len(dataCopy))
                fold.append(dataCopy.pop(index))
            dataSplit.append(fold)
        return dataSplit
    
    
    def kFCVEvaluate(self, dataset, numFolds, *args):
        '''
        Description:
            Driver function for k-Fold cross validation 
        '''
        knn = kNNClassifier()
        folds = self.crossValSplit(dataset, numFolds)
        scores = list()
        for fold in folds:
            trainSet = list(folds)
            trainSet.remove(fold)
            trainSet = sum(trainSet, [])
            testSet = list()
            for row in fold:
                rowCopy = list(row)
                testSet.append(rowCopy)
                
            trainLabels = [row[-1] for row in trainSet]
            trainSet = [train[:-1] for train in trainSet]
            knn.fit(trainSet,trainLabels)
            
            actual = [row[-1] for row in testSet]
            testSet = [test[:-1] for test in testSet]
            
            predicted = knn.predict(testSet, *args)
            
            accuracy = printMetrics(actual, predicted)
            scores.append(accuracy)

        print('*'*20)
        print('Scores: %s' % scores)
        print('*'*20)        
        print('\nMaximum Accuracy: %3f%%' % max(scores))
        print('\nMean Accuracy: %.3f%%' % (sum(scores)/float(len(scores))))

# -----------------------------------------------------------------------------

def readData(fileName):
    '''
    Description:
        This method is to read the data from a given file
    '''
    data = []
    labels = []

    with open(fileName, "r") as file:
        lines = file.readlines() 
    for line in lines:
        splitline = line.strip().split(',')
        data.append(splitline)
        labels.append(splitline[-1])
    return data, labels
# -----------------------------------------------------------------------------

#Path where the file is located
cancer_cell_file = '/home/ecamo19/Documents/cursos_libros_tutoriales/cursos/VCU/image_analysis/project/part_3/data_for_knn/dataset_merged_for_knn.csv'

#Read file
cancer_cell_data, cancer_labels = readData(cancer_cell_file)

cdf = pd.DataFrame(cancer_cell_data)

cdf = cdf.apply(preprocessing.LabelEncoder().fit_transform)

cancerFeatures = cdf.values.tolist()


kfcv = kFoldCV()
neighbors_3  = kfcv.kFCVEvaluate(cancerFeatures, 10, 3, 'euclidean')
neighbors_5  = kfcv.kFCVEvaluate(cancerFeatures, 10, 5, 'euclidean')
neighbors_7  = kfcv.kFCVEvaluate(cancerFeatures, 10, 7, 'euclidean')
neighbors_9  = kfcv.kFCVEvaluate(cancerFeatures, 10, 9, 'euclidean')
neighbors_11 = kfcv.kFCVEvaluate(cancerFeatures, 10, 11, 'euclidean')



