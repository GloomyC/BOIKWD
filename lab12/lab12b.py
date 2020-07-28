# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 08:48:48 2020

@author: Gloomy
"""

import scipy.optimize as sp


Mat = [[0.8,2,0.7,0.4,0.2,0.3],
       [0.6,1.5,0.6,0.2,0.4,0.5]]
Mat = [Mat[0],
       Mat[0],
       Mat[0],
       Mat[1],
       Mat[1],
       Mat[1],]
row, col = sp.linear_sum_assignment(Mat)

Zadania = ["Z{0}".format(i) for i in range(len(Mat[0])+1)]
Pracownicy = ["Praca nr{0} pracownika 1:".format(i) for i in range(1,4)] + ["Praca nr{0} pracownika 2:".format(i) for i in range(1,4)]


for i in range(len(row)):
    print("{0} {1}".format(Pracownicy[row[i]],Zadania[col[i]]))