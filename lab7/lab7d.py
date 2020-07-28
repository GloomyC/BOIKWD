# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 09:02:56 2019

@author: Gloomy
"""

import scipy.optimize as sp
import numpy as np

class Result:
    def __init__(self,prob1,prob2,valueMin,valueMax):
        self.probabilitiesP1 = prob1
        self.probabilitiesP2 = prob2
        self.valueMin = valueMin
        self.valueMax = valueMax

def linNash(G):
    res = Result(0,0,0,0)
    
    ylen = len(G)
    xlen = len(G[0])
    G = np.array(G)
    
    m = G.min()
    if m <0:
        Gfixed = G - m
        
    P1 = np.ndarray.tolist(Gfixed)
    
    ones = np.ndarray.tolist(-1*np.identity(xlen))
    for row in ones:
        P1.append(row)
    
    b = [1 for i in range(ylen)]
    b1 = [0 for i in range(xlen)]
    b = b + b1
    
    c = [-1 for i in range(xlen)]
    
    result1 = sp.linprog(A_ub = P1, b_ub= b, c= c)
    x = result1.x
    v = 1/sum(x)
    
    x = [ v* i for i in x]
    if m< 0 :
        v = v+m
    res.probabilitiesP2 = x
    res.valueMax = v
    #----------------
    
    G = np.transpose(G)
    
    m = G.min()
    if m <0:
        Gfixed = G - m
        
    P2 = np.ndarray.tolist(-Gfixed)
    ones = np.ndarray.tolist(-1*np.identity(ylen))
    for row in ones:
        P2.append(row)
    b = [-1 for i in range(xlen)]
    b1 = [0 for i in range(ylen)]
    b = b + b1
    
    c = [1 for i in range(ylen)]
    
    result2 = sp.linprog(A_ub = P2, b_ub= b, c= c)
    x = result2.x
    v = 1/sum(x)
    
    x = [ v* i for i in x]
    if m< 0 :
        v = v+m
    res.probabilitiesP1 = x
    res.valueMin = v
    
    return res
    
    

G = [[-2,8,2],
     [3,-1,0]]

result = linNash(G)

x = result.probabilitiesP1
print("optimal move probabilities for P1")
print("1: {0:.3f}\n2: {1:.3f}".format(x[0],x[1]))
x = result.probabilitiesP2
print("optimal move probabilities for P2")
print("1: {0:.3f}\n2: {1:.3f}\n3: {2:.3f}".format(x[0],x[1],x[2]))
print("max game value: {0:.3f}".format(result.valueMax))
print("min game value: {0:.3f}".format(result.valueMin))

     

    





        
