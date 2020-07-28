# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 21:59:24 2019

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
    
def gameGen():
    moves = ["F1 T2","F1 T3","F2 T3","F2 T4"]
    fingers = [1,1,2,2]
    guess = [2,3,3,4]
    
    G = np.identity(4)
    
    for i in range(4):
        for j in range(4):
            result = fingers[i] + fingers[j]
            if guess[i] == result and guess[j] != result:
                G[i,j] = result
            elif guess[j] == result and guess[i] != result:
                G[i,j] = -result
            else :
                G[i,j] = 0
    return G, moves
    
G, moves = gameGen()

result = linNash(G)

print("P1 move probabilities")
for i in range(len(moves)):
    print("{0}: {1:.6f}".format(moves[i],result.probabilitiesP1[i]))
print("P2 move probabilities")
for i in range(len(moves)):
    print("{0}: {1:.6f}".format(moves[i],result.probabilitiesP2[i]))
print("Min game value: {0}".format(result.valueMin))
print("Max game value: {0}".format(result.valueMax))
    
    
    
    
    
    
    
    
    
    
    
    
    
    


