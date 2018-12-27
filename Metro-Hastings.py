"""
Performes Metropolitan-Hasings algorithm

q() är proposal dist, en pdf
Xp är samplat från denna dist



"""
import numpy as np
import matplotlib.pyplot as plt
from rejection_sample import Rejection,NormalDist,Proposal

def alpha(xp,x,sigma):
    p = t_dist(xp)/t_dist(x) * q(x,xp,sigma)/q(xp,x,sigma)
    #print(q_rand_walk(x,xp,sigma)/q_rand_walk(xp,x,sigma))
    return p


def q(x,xp,sigma):
    mu = 0  #0 för uppgift b x för uppgift a
    Q = 1/np.sqrt(2*np.pi*sigma**2)*np.exp(-(xp-mu)**2 / (2*sigma**2))
    return Q
    
    
def t_dist(x):
    c = 1
    d = 5
    f = c*(1+x**2/d)**(-(d+1)/2)
    return f

def main():
    N = 15000
    x = 0
    mu = 0
    sigma = 1
    index = -1
    X = np.zeros(N)
    a_save = np.zeros(N)
    Ex4 = np.zeros(N-101)
    for ii in range(0,N):
        index+=1
        xp = Rejection(mu,sigma) #Andra till mu för uppgift b, annars x
        a = alpha(xp,x,sigma)
        a_save[index] = a
        U = np.random.rand()
        if U < a:
            x = xp
            #print('accept')
       
        X[ii] = x
        if index > 100:
            Ex4[ii-101] = np.mean(X[100:index]**4)
            
    plt.figure(1)
    plt.clf()
    plt.hist(X,24)
    
    plt.figure(2)
    plt.clf()
    plt.plot(X)
    
    plt.figure(3)
    plt.clf()
    plt.plot(Ex4)
    
    plt.figure(4)
    plt.clf()
    plt.plot(a_save)
    
if __name__ == "__main__":
    main()