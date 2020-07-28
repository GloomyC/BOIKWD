# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 00:42:59 2020

@author: Gloomy
"""
import numpy as np
import scipy.optimize as sp

X = -1000000
Mat =[[5.6,6,X,X,4.8],
      [3.2,3.5,4,3.8,4],
      [4.4,4.6,5,4.7,4.5],
      [4.7,4.5,4.8,4.8,4.2],
      [0,0,0,0,0]]
Mat = np.ndarray.tolist(-np.matrix(Mat))

row, col = sp.linear_sum_assignment(Mat)

Lokaty = ["jednodniowa:","1-miesieczna:","3-miesieczna:","6-miesieczna:","żadna"]
Banki = ["PKO PB","PEKAO SA","Millenium","ING","Mbank"]

for i in range(len(row)-1):
    print("{0} {1}".format(Lokaty[row[i]],Banki[col[i]]))



