"""
Performes Metropolitan-Hasings algorithm

q() är proposal dist, en pdf
Xp är samplat från denna dist


@author: Johan Öhman
"""
import numpy as np
import matplotlib.pyplot as plt
from rejection_sample import Rejection,NormalDist,Proposal

def alpha(xp,x,sigma)                                           #Define acceptence prob.
    p = t_dist(xp)/t_dist(x) * q(x,xp,sigma)/q(xp,x,sigma)
    #print(p)
    return p


def q(x,xp,sigma):                                              #Define proposal dist.
    mu = 0  #0 för uppgift b x för uppgift a
    Q = 1/np.sqrt(2*np.pi*sigma**2)*np.exp(-(xp-mu)**2 / (2*sigma**2))
    return Q
    
    
def t_dist(x):                                                  #Define target dist.
    c = 0.38        #Approx value for normalization
    d = 5
    f = c*(1+x**2/d)**(-(d+1)/2)
    return f

def main():             #Define main function
    N = 100000          #Time steps
    x = 0               #Initial value
    
    sigma = 15           #7 ganska bra för uppgift b, annars 1 på upg a
    index = -1
    X = np.zeros(N)
    a_save = np.zeros(N)
    Ex4 = np.zeros(N)
    
    for ii in range(0,N):   #Loop over all time steps
        if ii%1000 == 0:
            print(ii)
        index+=1
        mu = 0     #0 för uppgift b x för uppgift a
        xp = Rejection(mu,sigma) 
        a = alpha(xp,x,sigma)
        a_save[index] = a
        U = np.random.rand()
        if U < a:
            x = xp
            #print('accept')
       
        X[ii] = x
        if index > 100:         #Remove burn-in
            Ex4[ii] = np.mean(X[100:index]**4)
            
            
    #Plot
    x_cont = np.linspace(-10,10,10001)    
    plt.figure(1)
    plt.clf()
    plt.hist(X,50, density=True)
    plt.plot(x_cont,t_dist(x_cont))
    plt.xlabel("X")
    plt.ylabel("Probability density")
    plt.title("Histogram of target distribution")
    
    plt.figure(2)
    plt.clf()
    plt.plot(X)
    plt.xlabel("N")
    plt.ylabel("X")
    
    plt.figure(3)
    plt.clf()
    plt.plot(Ex4)
    plt.xlabel("N")
    plt.ylabel("$E(X^4)$")
    plt.title("Proposal N(0,"+str(sigma)+")")

    """
    plt.figure(4)
    plt.clf()
    plt.plot(a_save)
    """
if __name__ == "__main__":
    main()          #Run main function