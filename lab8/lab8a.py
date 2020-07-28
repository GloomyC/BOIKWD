# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 08:21:38 2019

@author: Gloomy
"""

import scipy.optimize as sp
import numpy as np
import math

#comparison functions with numerical error tolerance 
def isGreater(a,b):
    if a - b > 0.0000000001:
        return True
    return False

def isLesser(a,b):
    if a - b < -0.0000000001:
        return True
    return False

def fixEquations(A,b):
    #some of rows in equation system represent the same equations multiplied by constant
    #this function removes unnecessary equations converting matrix to square matrix
    #and allowing solver to convert y solution of dual equation to x solution of original problem

    #equal rows are being detected using dot product
    #proper results heavily depend on numerical error tolerance set in functions isLesser and isGreater
    
    A = np.matrix(A)
    A = np.ndarray.tolist(A)
    
    removeThis = []
    for i in range(len(A)):
        row1 = A[i]
        
        for j in range(i+1,len(A)):
            row2 = A[j]
                
            size1 =b[i]*b[i]
            size2 =b[j]*b[j]
            scalar = b[i]*b[j]
            for k in range(len(A[0])):
                size1 += row1[k]*row1[k]
                size2 += row2[k]*row2[k]
                scalar += row1[k]*row2[k]
                
            size1 = math.sqrt(size1)
            size2 = math.sqrt(size2)
            scalar = abs(scalar/(size1*size2))
            
            if not isGreater(scalar,1) and not isLesser(scalar,1):
                removeThis.append(j)
    removeThis = list(set(removeThis))
    
    removeThis.sort()
    
    for i in range(len(removeThis)-1,-1,-1):
        del A[removeThis[i]]
        del b[removeThis[i]]
    return np.array(A) , b
        

def dualSolve(A,b,c):
    
    A = np.array(A)
    A = np.transpose(A)
    Acpy = np.copy(A)
    minusC = [-i for i in c]
    A = np.ndarray.tolist(A)
    
    #geater then zero y's requirement
    ones = np.identity(len(b))
    for one in ones:
        A.append(one)
        minusC.append(0)
    A = np.array(A)
    
    #solve dual equation
    result = sp.linprog(A_ub = -A, b_ub= minusC, c= b)
    y = result.x
    print("Y: {0}".format(y))
    
    #get values
    vals = np.matmul(Acpy,y)
    
    #if value greater then right side of equation, set isZero to true
    isZero = []
    for i in range(len(c)):
        if isGreater(vals[i], c[i]):
            isZero.append(True)
        else:
            isZero.append(False)
            
    #remove columns from original equation that correspond to zero value x'es
    Acpy = np.ndarray.tolist(Acpy)
    for i in range(len(c)-1,-1,-1):
        if isZero[i]:
            del Acpy[i]
    Acpy = np.transpose(np.array(Acpy))
    
    #very important function, read it's description up
    Acpy,b = fixEquations(Acpy,b)
    
    #solve x equation
    x = np.linalg.solve(Acpy,b)
    x= np.ndarray.tolist(x)
    
    #insert known zeros to solution
    for i in range(len(isZero)):
        if isZero[i]:
            x.insert(i,0)
    return x;

A = [[1,3,2,3,1],[4,6,5,7,1]]
b = [6,15]
c = [2,5,3,4,1]


x = dualSolve(A,b,c)

print("X: {0}".format(x))
        
    
    
    
    