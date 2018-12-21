# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 09:50:22 2018

@author: johohm
"""

import matplotlib.pyplot as plt
import numpy as np

def NormalDist(RV):
    
    f = 1/np.sqrt(2*np.pi)*np.exp(-(RV)**2 / (2))
    return f

def Proposal(RV):
    g = np.exp(-RV)
    return g

def Rejection():
    c = np.sqrt(2*np.exp(1)/np.pi)

    while True:
        X = -np.log(np.random.rand())
        U = np.random.rand()
        
        proposal = Proposal(X)
        f = NormalDist(X)
        
        if f/(c*proposal) > U:
            R2 = np.random.rand()
            if R2 > 0.5:
                return X
            else:
                return -X
print('Hej!')
A = Rejection()
N = 10000;
test = np.zeros(N)
for i in range(1,N):
    test[i] = Rejection()
plt.figure(1)
plt.clf()
plt.hist(test,14)
#print(test)
