# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 09:50:22 2018
Kod för rejection sampling. Uppgift 6 i assignment 4
@author: Johan Öhman
"""
import matplotlib.pyplot as plt
import numpy as np
def NormalDist(RV):
    #pdf of normal dist
    f = 1/np.sqrt(2*np.pi)*np.exp(-(RV)**2 / (2))
    return f

def Proposal(RV):
    #Exponential proposol distribution
    g = np.exp(-RV)
    return g

def Rejection(mu,sigma):
    c = np.sqrt(2*np.exp(1)/np.pi)
    while True:
        #sample from exponential
        X = -np.log(np.random.rand())
        #Sample from uniform
        U = np.random.rand()
        
        proposal = Proposal(X)
        f = NormalDist(X)
        
        if f/(c*proposal) > U:
            R2 = np.random.rand()
            if R2 > 0.5:
                return (X*sigma+mu)
            else:
                return (-X*sigma+mu)
            
if __name__ == "__main__":
    
    A = Rejection(1,2)
    x_cont = np.linspace(-5,5,10001)   
    N = 100000;
    test = np.zeros(N)
    sigma = 3
    mu = 0
    for i in range(1,N):
        test[i] = Rejection(mu,sigma)
    plt.figure(1)
    plt.clf()
    plt.hist(test,50,density=True)
    plt.ylim((0,0.5))
    plt.xlim((-15,15))
    #plt.plot(x_cont,NormalDist(x_cont))
    plt.xlabel("Z")
    plt.ylabel("Probability density")
    plt.title("Rejection Sampling, $\mu$ ="+str(mu)+" and $\sigma$ = "+str(sigma))
    #print(test)
