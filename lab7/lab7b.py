# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 08:41:17 2019

@author: Gloomy
"""

import scipy.optimize as sp

#Ax <= b
#f(x) = c^t * x   -> min
A = [[-5,-15],
     [-20,-5],
     [15,2],
     [-1,0],
     [0,-1]]
b = [-50,-40,60,0,0]


c = [8,4]

result = sp.linprog(A_ub = A, b_ub = b,c = c)

print("steki: {0:.2f}\nziemniaki {1:.2f}\ncena: {2:.2f} ".format(result.x[0],result.x[1],result.fun))