# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 08:32:49 2019

@author: Gloomy
"""

import numpy as np

def normalise(vec):
    total = sum(vec)
    result = np.matmul((1/total)*np.identity(len(vec)),vec)
    return result
    
def ahp(Criteria, Criteria_prio ):

    subratings =np.ndarray.tolist(np.zeros(len(Criteria)))
    
    for i in range(0,len(Criteria)):
        #calculate eigenvectors and eigenvalues
        Eigvals, Eigvecs = np.linalg.eig(Criteria[i])
        
        #choose eigenvector corresponding to highest eigenvalue 
        Eigvals = np.absolute(Eigvals)
        Eigvecs = np.absolute(Eigvecs)
        Eigvec = Eigvecs[:,np.argmax(Eigvals)]
        
         #normalise chosen eigenvector and place it in subratings matrix
        subratings[i] = np.ndarray.tolist(normalise(Eigvec))
        
    print('each criteria rating: \n {0}'.format(subratings))
    subratings = np.transpose(subratings)
    
    #calculate eigenvector corresponding to highest eigenvalue
    Eigvals, Eigvec = np.linalg.eig(Criteria_prio)
    Eigvals = np.absolute(Eigvals)
    prio = Eigvec[:,np.argmax(Eigvals)]
    prio = np.absolute(prio)
    #normalise it
    prio = normalise(prio)
    
    #calculate final rating
    rating = np.matmul(subratings,prio)
    
    print('final rating: \n {0}'.format(np.ndarray.tolist(rating)))
    print('done')
    return rating


C1 = [[1,1/7,1/5],[7,1,3],[5,1/3,1]]
C2 = [[1,5,9],[1/5,1,4],[1/9,1/4,1]]
C3 = [[1,4,1/5],[1/4,1,1/9],[5,9,1]]
C4 = [[1,9,4],[1/9,1,1/4],[1/4,4,1]]
C5 = [[1,1,1],[1,1,1],[1,1,1]]
C6 = [[1,6,4],[1/6,1,1/3],[1/4,3,1]]
C7 = [[1,9,6],[1/9,1,1/3],[1/6,3,1]]
C8 = [[1,1/2,1/2],[2,1,1],[2,1,1]]

Crits = [C1,C2,C3,C4,C5,C6,C7,C8]

C = [[1,4,7,5,8,6,6,2],
     [1/4,1,5,3,7,6,6,1/3],
     [1/7,1/5,1,1/3,5,3,3,1/5],
     [1/5,1/3,3,1,6,3,4,1/2],
     [1/8,1/7,1/5,1/6,1,1/3,1/4,1/7],
     [1/6,1/6,1/3,1/3,3,1,1/2,1/5],
     [1/6,1/6,1/3,1/4,4,2,1,1/5],
     [1/2,3,5,2,7,5,5,1]
     ]


result = ahp(Crits,C)
