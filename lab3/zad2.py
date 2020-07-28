# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 08:40:18 2019

@author: Gloomy
"""

import numpy as np
import math

def Satty(matrix):
    eigvals = np.abs(np.linalg.eigvals(matrix))
    
    max_eig = max(eigvals)
    
    return (max_eig - len(matrix))/(len(matrix)-1)

def Koczkodaj(matrix):
    
    maxval = 0;
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == j:
                continue
            for k in range(len(matrix)):
                 if j == k:
                     continue
                 kocz = min(abs(1-(matrix[i][k]*matrix[k][j])/matrix[i][j]),abs(1-matrix[i][j]/(matrix[i][k]*matrix[k][j]))  )
                 if kocz > maxval:
                     maxval = kocz
    return maxval;
            

A=[[1,7,3] , [1/7,1,2] , [1/3,1/2,1]]
B=[[1,1/5,7,1] , [5,1,1/2,2] , [1/7,2,1,3] , [1,1/2,1/3,1]]
C=[[1,2,5,1,7] , [1/2,1,3,1/2,5] , [1/5,1/3,1,1/5,2] , [1,2,5,1,7] , [1/7,1/5,1/2,1/7,1]]
    
mats = [A,B,C]
sattys = np.ndarray.tolist(np.zeros(len(mats)))
koczkos = np.ndarray.tolist(np.zeros(len(mats)))

for index in range(len(mats)):
    sattys[index] = Satty(mats[index])
    koczkos[index] = Koczkodaj(mats[index])
    
print("Indexy Satty’ego: {0}".format(sattys))
print("Indexy Koczkodaja: {0}".format(koczkos))
    
    