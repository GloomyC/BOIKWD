# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 08:12:17 2019

@author: Gloomy
"""

import numpy as np

def findMins(M,reverse = False):
    mins = np.ndarray.tolist(np.zeros(len(M)))
    for i in range(len(M)):
        if not reverse:
            mins[i] = min(M[i])
        else:
            mins[i] = -max(M[i])
    return mins

M = [[20,-150,-250],[150,-80,-100],[250,100,40]]

Amins = findMins(M)
A_minmax = max(Amins)
A_minmax_choice = Amins.index(A_minmax) +1

M = np.transpose(M)

Bmins = findMins(M,reverse=True)
B_minmax = max(Bmins)
B_minmax_choice = Bmins.index(B_minmax) +1

print("best option for A: {0}".format(A_minmax_choice))
print("best option for B: {0}".format(B_minmax_choice))

