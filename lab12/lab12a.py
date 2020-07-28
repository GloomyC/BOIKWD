# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 08:38:09 2020

@author: Gloomy
"""

import scipy.optimize as sp

Mat = [[5,7,8,7],
       [6,4,7,6],
       [7,5,6,5],
       [4,3,5,9]]
row, col = sp.linear_sum_assignment(Mat)

Warsztaty = ["Warsztat {0}:".format(n) for n in range(1,5)]
Samochody = ["Ford","Volkswagen","Toyota","Fiat"]


for i in range(len(row)):
    print("{0} {1}".format(Warsztaty[row[i]],Samochody[col[i]]))

