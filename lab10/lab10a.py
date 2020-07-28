# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 08:51:22 2019

@author: Gloomy
"""
import numpy as np
import scipy.optimize as sp

def ilorazSolve(A,b,c,cm):
    Acp = A.copy()
    bcp = b.copy()
    cmcp = cm.copy()
    ccp = c.copy()
    
    for i in range(len(b)):
        Acp[i].append(-b[i])
        bcp[i] = 0
    ccp.append(0)
    cmcp.append(0)
    b2 = [1]
    
    solution = sp.linprog(A_ub = Acp,b_ub =bcp, c = ccp, A_eq = [cmcp],b_eq = b2 )
    
    y = solution.x
    
    y0 = y[len(y)-1]
    
    x = [i/y0 for i in y]
    
    return x[0:len(x)-1]
        
c = [3,4]
cm = [1,2]

A = [[1,2],
     [1,1],
     [-2,-1]]
b = [500,350,-600]

result = ilorazSolve(A,b,c,cm)

print("optimal product amounts: {0}".format(result))


