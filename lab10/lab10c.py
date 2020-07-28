# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 09:16:11 2019

@author: Gloomy
"""


import scipy.optimize as sp
import numpy as np
import math

def isNatural(v):
    if abs(v % 1) <= 0.000001:
        return True
    return False
class SolutionNode:
    
    def __init__(self,A,b,c):
        self.A = A
        self.b = b
        self.c = c
        self.cost = 0;
        self.x = [];
        self.children = []
        self.valid = False
    
    def solve(self):
        self.calculate()
        #if no children return self (can be invalid)
        if len(self.children)==0:
            return self
        else:
            child_results = []
            #get valid results from children
            for child in self.children:
                subresult = child.solve()
                if subresult.valid:
                    child_results.append(subresult)
            #if there are valid child solutions, return best one
            if len(child_results )!= 0:
                return max(child_results,key = lambda x: x.cost)
            #if there aren't valid child solutions, return nonvalid self to mark dead branch
            else:
                return self
        
    def calculate(self):
        localSolution = sp.linprog(A_ub = self.A,b_ub = self.b,c = [-val for val in self.c])
        
        x = localSolution.x
        #if there is valid solution
        if localSolution.success:

            selected = False
            selectedIndex = 0;
            #select 1st non natural value from solution
            for i in range(len(x)):
                if not isNatural(x[i]):
                    selected = True
                    selectedIndex = i
                    break
            #if all values are natural, mark self as valid solution
            if not selected:
                
                self.valid = True
                self.x = x
                self.cost = np.dot(x,self.c)
            
            #create children if current solution isn't valid
            if not self.valid:
                #lower restriction
                n = math.floor(x[selectedIndex])
                
                restriction = [1 if j == selectedIndex else 0 for j in range(len(x))]
                
                newA = self.A.copy()
                newA.append(restriction)
                newb = self.b.copy()
                newb.append(n)
                
                child = SolutionNode(newA,newb,self.c)
                self.children.append(child)
                
                #higher restriction
                n = -math.ceil(x[selectedIndex])
                
                restriction = [-1 if j == selectedIndex else 0 for j in range(len(x))]
                
                newA = self.A.copy()
                newA.append(restriction)
                newb = self.b.copy()
                newb.append(n)
                
                child = SolutionNode(newA,newb,self.c)
                self.children.append(child)
            

A = [[4,3],
     [1,1]]
b= [190,55]
c = [23,17]

solver = SolutionNode(A,b,c)

result = solver.solve()

print("optimal product amounts: {0}".format(result.x))
            
        
        
        
        
        
            
            
            
            
            
            
            
            
        