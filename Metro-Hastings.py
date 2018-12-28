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
    print(p)
    return p


def q(x,xp,sigma):
    mu = x  #0 för uppgift b x för uppgift a
    Q = 1/np.sqrt(2*np.pi*sigma**2)*np.exp(-(xp-mu)**2 / (2*sigma**2))
    return Q
    
    
def t_dist(x):
    c = 0.38
    d = 5
    f = c*(1+x**2/d)**(-(d+1)/2)
    return f

def main():
    N = 10000
    x = 0
    
    sigma = 100
    index = -1
    X = np.zeros(N)
    a_save = np.zeros(N)
    Ex4 = np.zeros(N-1001)
    for ii in range(0,N):
        index+=1
        mu = x
        xp = Rejection(mu,sigma) 
        a = alpha(xp,x,sigma)
        a_save[index] = a
        U = np.random.rand()
        if U < a:
            x = xp
            #print('accept')
       
        X[ii] = x
        if index > 1000:
            Ex4[ii-1001] = np.mean(X[1000:index]**4)
    x_cont = np.linspace(-10,10,10001)    
    plt.figure(1)
    plt.clf()
    plt.hist(X,50, density=True)
    plt.plot(x_cont,t_dist(x_cont))
    
    plt.figure(2)
    plt.clf()
    plt.plot(X)
    
    plt.figure(3)
    plt.clf()
    plt.plot(Ex4)

    """
    plt.figure(4)
    plt.clf()
    plt.plot(a_save)
    """
if __name__ == "__main__":
    main()