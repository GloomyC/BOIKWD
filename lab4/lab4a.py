# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 08:11:37 2019

@author: Gloomy
"""


import numpy as np
import math

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

def KoczkodajThreshold(n,k):
    return 1-((1+ math.sqrt(4*(n-1)*(n-k-2)))/(2*(n-1)))

def HREknown(Comp, knownIndexes, knownVals):
    kocz = Koczkodaj(Comp)
    
    print("Koczkodaj's index: {0}".format(kocz))
    if kocz < KoczkodajThreshold(len(Comp),len(knownIndexes)):
        print("Koczkodaj passes")
    else:
        print("Koczkodaj fails")
    
    knownSize = len(knownIndexes)
    unknownSize = len(Comp) - len(knownIndexes)
    
    unknownIndexes = list(range(len(Comp)))
    for index in knownIndexes:
        unknownIndexes.remove(index)
    
    A = np.ndarray.tolist(np.zeros([unknownSize,unknownSize]))
    B = np.ndarray.tolist(np.zeros([unknownSize,knownSize]))
    
    for i in range(unknownSize):
        for j in range(unknownSize):
            x = 1
            if i != j:
                x = (-1/(len(Comp)-1))
            A[i][j] = x* Comp[unknownIndexes[i]][unknownIndexes[j]]
            
    for i in range(unknownSize):
        for j in range(knownSize):
            B[i][j] = Comp[unknownIndexes[i]][knownIndexes[j]]
            
    Bhat = np.ndarray.tolist(np.matmul(B,knownVals))
    Bhat = np.matmul(1/(len(Comp)-1)*np.identity(len(Bhat)),Bhat)
    
    result = np.ndarray.tolist(np.linalg.solve(A,Bhat))
            
    return result

A=[[    1,2/3,2,5/2,5/3,5],[
        3/2,1,3,10/3,3,9],[
        1/2,1/3,1,4/3,7/8,5/2],[
        2/5,3/10,3/4,1,5/6,12/5],[
        3/5,1/3,8/7,6/5,1,3],[
        1/5,1/9,2/5,5/12,1/3,1]]

AknownIndexes = [4,5]
AknownVals = [3,1]

B=[[1,2/5,3,7/3,1/2,1],[
5/2,1,4/7,5/8,1/3,3],[
1/3,7/4,1,1/2,2,1/2],[
3/7,8/5,2,1,4,2],[
2,3,1/2,1/4,1,1/2],[
1,1/3,2,1/2,2,1]]

BknownIndexes = [3,4,5]
BknownVals = [2,1/2,1]


C=[[1,17/4,17/20,8/5,23/6,8/3],[
4/17,1,1/5,2/5,9/10,2/3],[
20/17,5,1,21/10,51/10,10/3],[
5/8,5/2,10/21,1,5/2,11/6],[
6/23,10/9,10/51,2/5,1,19/30],[
3/8,3/2,3/10,6/11,30/19,1]]


CknownIndexes = [1,3]
CknownVals = [2,5]

Aresult = HREknown(A,AknownIndexes,AknownVals)

print("final rating HRE matrix A:\n {0}".format(Aresult))

Bresult = HREknown(B,BknownIndexes,BknownVals)

print("final rating HRE matrix B:\n {0}".format(Bresult))

Cresult = HREknown(C,CknownIndexes,CknownVals)

print("final rating HRE matrix C:\n {0}".format(Cresult))







