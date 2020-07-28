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
    print("[[[[[[[[[[]]]]]]]]]]")
    print(Criteria)
    print("[[[[[[[[[[]]]]]]]]]]")
    
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

def compare_matrix(values, higher_better):
    
    size = len(values)
    price_comp = np.ndarray.tolist(np.zeros((size,size)))
    for i in range(0,size):
        for j in range(0,size):
            if not higher_better:
                #the lower the better
                price_comp[i][j] = (values[i])/(values[j])
            else:
                #the higher the better
                price_comp[i][j] = (values[j])/(values[i])  
                
    return price_comp
    
    

C1 = [68200,8.9,4,460,5]
C2 = [39900,11.2,3.5,415,5]
C3 = [87394,5.8,4.5,430,4]

Cars = np.array([C1,C2,C3])
val = Cars[:,0]
#price criteria
price_comp = compare_matrix(np.ndarray.tolist(Cars[:,0]),False)
#petrol usage criteria
petrol_comp = compare_matrix(np.ndarray.tolist(Cars[:,1]),False)   
#safety criteria
safety_comp = compare_matrix(np.ndarray.tolist(Cars[:,2]),True)
#trunk criteria
trunk_comp = compare_matrix(np.ndarray.tolist(Cars[:,3]),True)
#seats criteria
seats_comp = compare_matrix(np.ndarray.tolist(Cars[:,4]),True)

#I'm lazy so i'm crating comparison matricies from flat priority values
cost_priority = [7,2]   #price, pertol usage
cost_priority = compare_matrix(cost_priority,True)

load_priority = [3,2]  #trunk, seats
load_priority = compare_matrix(load_priority,True)

safety_priority = [1] #safety
safety_priority = compare_matrix(safety_priority,True)

#subcriteria
cost_rating = ahp([price_comp,petrol_comp],cost_priority)
print("cost done")
load_rating = ahp([trunk_comp,seats_comp],load_priority)
print("load done")
safety_rating = ahp([safety_comp],safety_priority)
print("safety done")

#join subcriteria
final_priority = [2,5,1] # Cost, Load, Other
final_priority = compare_matrix(final_priority,True)

cost_comp = compare_matrix(cost_rating,True)
load_comp = compare_matrix(load_rating,True)
safety_comp = compare_matrix(safety_rating,True)

final_rating = ahp([cost_comp,load_comp,safety_comp],final_priority)








