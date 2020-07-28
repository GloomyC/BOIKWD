# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 15:52:00 2019

@author: Gloomy
"""

import numpy as np
import math

def HREgeomknown(Comp, knownIndexes, knownVals):

    knownSize = len(knownIndexes)
    unknownSize = len(Comp) - len(knownIndexes)
    unknownIndexes = list(range(len(Comp)))
    
    for index in knownIndexes:
        unknownIndexes.remove(index)
        
    b = np.ndarray.tolist(np.zeros(unknownSize))
    
    for i in range(unknownSize):
        val =1
        for j in range(unknownSize):
            val = val*Comp[unknownIndexes[i]][unknownIndexes[j]]
        for j in knownVals:
            val = val* j
        val = np.log10(val)
        b[i] = val
        
    

    A = np.ndarray.tolist(np.zeros([unknownSize,unknownSize]))
    
    
    
    for i in range(unknownSize):
        for j in range(unknownSize):
            val  = -1
            if i == j:
                val = len(Comp) -1
            A[i][j] = val
            
    
    result = np.ndarray.tolist(np.linalg.solve(A,b))
    
    for i in range(len(result)):
        result[i] = math.pow(10,result[i])
            
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


Aresult = HREgeomknown(A,AknownIndexes,AknownVals)

print("final rating HRE geom matrix A:\n {0}".format(Aresult))

Bresult = HREgeomknown(B,BknownIndexes,BknownVals)

print("final rating HRE geom matrix B:\n {0}".format(Bresult))

Cresult = HREgeomknown(C,CknownIndexes,CknownVals)

print("final rating HRE geom matrix C:\n {0}".format(Cresult))