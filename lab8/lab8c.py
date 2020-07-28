# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 09:18:59 2019

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

A = [[-4,-1,-5,-2,0],
     [0,-1,-1,-2,-3]]
b = [-12000,-18000]
c = [-0.1,-0.2,-0.3,-0.4,0]

print("Podziały:")
print("1. tasma 2.1m: 4x0.5m,  0x1.4m,  0.1m odpadku")
print("2. tasma 2.1m: 1x0.5m,  1x1.4m,  0.2m odpadku")
print("3. tasma 4.2m: 8x0.5m,  0x1.4m,  0.2m odpadku")
print("3. tasma 4.2m: 5x0.5m,  1x1.4m,  0.3m odpadku")
print("4. tasma 4.2m: 2x0.5m,  2x1.4m,  0.4m odpadku")
print("5. tasma 4.2m: 0x0.5m,  3x1.4m,  0.0m odpadku")
print("--------------")
print("wykluczyłem podział: tasma 4.2m: 8x0.5m + 0x1.4m + 0.0m odpadku")
print("jest on rownowazny podziałowi 1.")
print("powodował niemożliwosc przeksztalcenia rozwiazania dualnego na x" )
print("--------------")
print("optymalny podział: {0}".format(dualSolve(A,b,c)))

