# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 00:04:58 2019

@author: Gloomy
"""

import scipy.optimize as sp
import numpy as np

A = [[2,1,3],[2,3,1],[5,2,3]]
b = [30,20,30]
c = [-32,-24,-48]

result = sp.linprog(A_ub = A, b_ub= b, c= c);

print("optimal values: {0}".format(result.x))
print("cost value: {0}".format(-np.dot(result.x,c)))