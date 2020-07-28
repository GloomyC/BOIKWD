# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 17:23:42 2019

@author: Gloomy
"""

import numpy as np
import math

def hasTies(matrix):
    s = len(matrix)
    
    for i in range(s):
        for j in range(s):
            if i == j:
                continue
            if matrix[i][j] ==0:
                return True
    return False

def isValidTourney(matrix):
    s = len(matrix)
    
    for i in range(s):
        for j in range(s):
            if matrix[i][j] != -matrix[j][i]:
                return False
    return True

def compFromVals(matrix):
    s = len(matrix)
    result = np.ndarray.tolist(np.zeros((s,s)))
    
    for i in range(s):
        for j in range(s):
            if(i == j):
                matrix[i][j] = 0
            elif(matrix[i][j]==1):
                result[i][j] = 0
            elif(matrix[i][j]>1):
                result[i][j] = 1
            else:
                result[i][j] = -1
    return result

def maxInconsClassic(n):
    if n%2 ==0 :
        return (math.pow(n,3) -4*n)/24
    else:
        return (math.pow(n,3) -n)/24
    
def maxInconsExtended(n):
    rest = n%4
    if rest ==0:
        return (13*n*n*n - 24*n*n - 16*n)/96
    elif rest ==1:
        return (13*n*n*n - 24*n*n - 19*n + 30)/96
    elif rest ==2:
        return (13*n*n*n - 24*n*n - 4*n)/96
    else:
        return (13*n*n*n - 24*n*n - 19*n + 18)/96
    
    
    
def classicKendall(matrix):
    incons =0
    found =set()
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == j:
                continue
            for k in range(len(matrix)):
                 if j == k:
                     continue
                 if(matrix[i][j]==matrix[j][k] and matrix[j][k]==matrix[k][i]):
                     indexes = [i,j,k]
                     indexes.sort()
                     key = math.pow(len(matrix),2)*indexes[0]+indexes[1]*len(matrix)+indexes[2]
                     if(not key in found):
                         incons = incons +1
                         found.add(key)
    return 1- incons/maxInconsClassic(len(matrix))

def extendedKendall(matrix):
    incons =0
    found =set()
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == j:
                continue
            for k in range(len(matrix)):
                 if j == k:
                     continue
                 
                 if(matrix[i][j]==matrix[j][k] and matrix[j][k]==matrix[k][i]):
                     # a == b == c == a GOOD
                     if(matrix[i][j] == 0):
                         continue
                     # a < b < c < a OR a > b > c > a BAD
                     else: 
                         # chceck if not redetected
                         indexes = [i,j,k]
                         indexes.sort()
                         key = math.pow(len(matrix),2)*indexes[0]+indexes[1]*len(matrix)+indexes[2]
                         if(not key in found):
                             incons = incons +1
                             found.add(key)
                # a == b == c < a OR a == b == c > a BAD
                 if(matrix[i][j] == 0 and matrix[j][k] == 0 and matrix[k][i] != 0):
                    # chceck if not redetected
                     indexes = [i,j,k]
                     indexes.sort()
                     key = math.pow(len(matrix),2)*indexes[0]+indexes[1]*len(matrix)+indexes[2]
                     if(not key in found):
                         incons = incons +1
                         found.add(key)
                # a < b < c == a OR a > b > c == a
                 if(matrix[i][j] != 0 and matrix[i][j] == matrix[j][k]  and matrix[k][i] == 0):
                    # chceck if not redetected
                     indexes = [i,j,k]
                     indexes.sort()
                     key = math.pow(len(matrix),2)*indexes[0]+indexes[1]*len(matrix)+indexes[2]
                     if(not key in found):
                         incons = incons +1
                         found.add(key)
    return 1- incons/maxInconsExtended(len(matrix))

A=[[1,2/3,2,5/2,5/3,5],[3/2,1,3,10/3,3,9],[1/2,1/3,1,4/3,7/8,5/2],[2/5,3/10,3/4,1,5/6,12/5],[3/5,1/3,8/7,6/5,1,3],[1/5,1/9,2/5,5/12,1/3,1]]

B=[[1,2/5,3,7/3,1/2,1,2],[5/2,1,4/7,1,1,3,2/3],[1/3,7/4,1,1/2,2,1/2,1],[3/7,1,2,1,4,2,6],[2,1,1/2,1/4,1,1/2,3/4],[1,1/3,2,1/2,2,1,5/8],[1/2,3/2,1,1/6,4/3,8/5,1]]

C=[[1,2/3,2/15,1,8,12/5,1,1/2],[3/2,1,1,2,1,2/3,1/6,1],[15/2,1,1,5/2,7/8,2,1,1/5],[1,1/2,2/5,1,4/3,1,2/7,1],[1/8,1,8/7,3/4,1,1/5,2/7,1],[5/12,3/2,1/2,1,5,1,3,2],[1,6,1,7/2,7/2,1/3,1,3/11],[2,1,5,1,1,1/2,11/3,1]]

D=[[0,1,1,-1,-1,1,-1],[-1,0,0,1,1,-1,0],[-1,0,0,0,1,1,-1],[1,-1,0,0,1,0,1],[1,0,-1,-1,0,1,-1],[-1,1,-1,1,-1,0,0],[1,0,1,-1,1,0,0]]

E=[[0,1,0,0,-1],[-1,0,0,0,1],[0,0,0,1,0],[0,0,-1,0,0],[1,-1,0,0,0]]

F=[[0,-1,1,-1,1,-1,1,-1,1],[1,0,1,1,1,-1,-1,-1,-1],[-1,-1,0,-1,1,-1,1,1,1],[1,-1,1,0,-1,1,-1,1,-1],[-1,-1,-1,1,0,-1,1,1,1],[1,1,1,-1,1,0,-1,-1,-1],[-1,1,-1,1,-1,1,0,1,-1],[1,1,-1,-1,-1,1,-1,0,1],[-1,1,-1,1,-1,1,1,-1,0]]
                 
A = compFromVals(A)
B = compFromVals(B)
C = compFromVals(C)

print("Is matrix A a proper tourney: {0}".format(isValidTourney(A)))
print("Is matrix B a proper tourney: {0}".format(isValidTourney(B)))
print("Is matrix C a proper tourney: {0}".format(isValidTourney(C)))
print("Is matrix D a proper tourney: {0}".format(isValidTourney(D)))
print("Is matrix E a proper tourney: {0}".format(isValidTourney(E)))
print("Is matrix F a proper tourney: {0}".format(isValidTourney(F)))

print("Does matrix A have ties: {0}".format(hasTies(A)))
print("Does matrix B have ties: {0}".format(hasTies(B)))
print("Does matrix C have ties: {0}".format(hasTies(C)))
print("Does matrix E have ties: {0}".format(hasTies(E)))
print("Does matrix F have ties: {0}".format(hasTies(F)))

print("Classic Kendall of matrix A: {0}".format(classicKendall(A)))
print("Classic Kendall of matrix F: {0}".format(classicKendall(F)))

print("Extended Kendall of matrix B: {0}".format(extendedKendall(B)))
print("Extended Kendall of matrix C: {0}".format(extendedKendall(C)))
print("Extended Kendall of matrix E: {0}".format(extendedKendall(E)))
      
                