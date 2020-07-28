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
        print(Eigvecs)
        Eigvec = Eigvecs[:,np.argmax(Eigvals)]
        print("----------")
        print(Eigvec)
        print("=========")
        
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

H1 = [210,20,20,0]
H2 = [150,20,30,1]
H3 = [230,30,12,0]
H4 = [250,25,8,1]

Hotels = [H1,H2,H3,H4]

#price criteria
price_comp = np.ndarray.tolist(np.zeros((4,4)))
for i in range(0,4):
    for j in range(0,4):
        #the lower the better
        price_comp[i][j] = (Hotels[i][0])/(Hotels[j][0])

#food criteria
food_comp = np.ndarray.tolist(np.zeros((4,4)))
for i in range(0,4):
    for j in range(0,4):
        #the lower the better
        food_comp[i][j] = (Hotels[i][1])/(Hotels[j][1])
        
#time criteria
time_comp = np.ndarray.tolist(np.zeros((4,4)))
for i in range(0,4):
    for j in range(0,4):
        #the lower the better
        food_comp[i][j] = (Hotels[i][2])/(Hotels[j][2])
        
#parking criteria
parking_comp = np.ndarray.tolist(np.zeros((4,4)))
bool_weight_offset = 1
for i in range(0,4):
    for j in range(0,4):
        #arbitrary assumption that having parking is twice as good as not having
        food_comp[i][j] = (Hotels[j][3]+bool_weight_offset)/(Hotels[i][3]+bool_weight_offset)
        
Crits = [price_comp,food_comp,time_comp,parking_comp]

Prio = [[1,5,3,4],
        [1/5,1,4,1],
        [1/3,1/4,1,2],
        [1/4,1,1/2,1]]


result = ahp(Crits,Prio)
