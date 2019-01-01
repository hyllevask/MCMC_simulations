# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 16:30:22 2018
MCMC simulation of the hard-core model
@author: johohm
"""
import matplotlib.pyplot as plt
import numpy as np


#Define function Phi that chooses uniformly which vertex to choose

def phi(U,N):
    A = np.cumsum( np.ones((1,N))/N)    #Compute intervals 
    for ii in range(0,N-1): #Loop to find the state
        if A[ii] >= U:
            return ii
        elif A[ii] < U <= A[ii+1]:
            return ii+1
"""
#Define the function CheckNeighbours that checks, given the grid and a point specified by 
row and col what the next value of that point should be.
"""       
def CheckNeighbours(row,col,Grid):

    flag1 = (Grid[row-1,col] + Grid[row,col-1] + Grid[row+1,col] + Grid[row,col+1]) == 0
    #If true update the value at the point, else leave it unchanged.
    if flag1:
        if Grid[row,col] == 0:
            return 1
        else:
            #print('remove')
            return 0
    else:
        return Grid[row,col]
    
#Define function 
def sum_points(Grid):
    s = np.sum(Grid)
    return s

plot_grid = 0
N_step = 100

N_grid = 8 #Size
Grid = np.zeros((N_grid+2,N_grid+2))
n_save = np.zeros(N_step)

for ii in range(1,N_step):
    #print(ii)
    U = np.random.rand()
    si  = phi(U,N_grid**2)
    si_unrav = np.unravel_index(si,(N_grid,N_grid))
    
    row = si_unrav[0]+1
    col = si_unrav[1]+1
    
    U_a = np.random.rand()
    if U_a > 0.5:
        Grid[row,col] = CheckNeighbours(row,col,Grid)
        
    if plot_grid == 1:
        plt.figure(1)
        plt.imshow(Grid)
        plt.pause(0.001)
        
    n_save[ii] = sum_points(Grid)
plt.show()   
#plt.plot(range(0,N_step),n_save/N_grid**2)
#plt.show()
plt.figure(2)
plt.plot(range(0,N_step),np.cumsum(n_save)/(1.+ np.array(range(0,N_step))))
plt.show()

    
    
    

