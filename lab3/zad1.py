# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 08:03:44 2019

@author: Gloomy
"""
import numpy as np
import math

def normalise(vec):
    total = sum(np.abs(vec))
    result = np.matmul((1/total)*np.identity(len(vec)),vec)
    return result

def prioGMM(matrix):
    rating = np.ndarray.tolist(np.zeros(len(matrix)))
    for i in range(len(matrix)):
            val =1;
            for j in range(len(matrix)):
                val= val * matrix[i][j]
            rating[i] = math.pow(val,1/len(matrix))
    rating = normalise(rating)
    return rating

def GMM(criteria, criteria_comp):
    
    subratings =np.ndarray.tolist(np.zeros(len(criteria)))
    
    for index in range(len(criteria)):
        matrix = criteria[index]
        subratings[index] =  prioGMM(matrix)
        
    criteria_prio = prioGMM(criteria_comp)
    criteria_prio = np.transpose(criteria_prio)
    print("criteria priorities:\n {0}".format(criteria_prio))
    
    final_rating = np.matmul(criteria_prio,subratings)
    final_rating = normalise(final_rating)
    print("final rating:\n {0}".format(final_rating))
    
    return final_rating
            
            

C1=[[1,1/7,1/5] , [7,1,3] , [5,1/3,1]]
C2=[[1,5,9] , [1/5,1,4] , [1/9,1/4,1]] 
C3=[[1,4,1/5] , [1/4,1,1/9] , [5,9,1]]
C4=[[1,9,4] , [1/9,1,1/4] , [1/4,4,1]] 
C5=[[1,1,1] , [1,1,1] , [1,1,1]] 
C6=[[1,6,4] , [1/6,1,1/3] , [1/4,3,1]]
C7=[[1,9,6] , [1/9,1,1/3] , [1/6,3,1]] 
C8=[[1,1/2,1/2] , [2,1,1] , [2,1,1]]


C_parametry=[[1,4,7,5,8,6,6,2] , [1/4,1,5,3,7,6,6,1/3] , [1/7,1/5,1,1/3,5,3,3,1/5] , [1/5,1/3,3,1,6,3,4,1/2] , [1/8,1/7,1/5,1/6,1,1/3,1/4,1/7] , [1/6,1/6,1/3,1/3,3,1,1/2,1/5] , [1/6,1/6,1/3,1/4,4,2,1,1/5] , [1/2,3,5,2,7,5,5,1]]

criteria = [C1,C2,C3,C4,C5,C6,C7,C8]

rating = GMM(criteria,C_parametry)