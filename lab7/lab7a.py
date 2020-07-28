# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 08:22:17 2019

@author: Gloomy
"""

import scipy.optimize as sp

#Ax <= b
#f(x) = c^t * x   -> min
A = [[1,1,1],
     [-1,-1,-1],
     [-1,-2,-1],
     [0,2,1],
     [-1,0,0],
     [0,-1,0],
     [0,0,-1]]
b = [30,-30,-10,20,0,0,0]


c = [-2,-1,-3]

result = sp.linprog(A_ub = A, b_ub = b,c = c)

print("x values: {0}".format(result.x))
print("function value: {0}".format(result.fun))
     