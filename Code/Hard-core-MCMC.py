# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 16:30:22 2018
MCMC simulation of the hard-core model

Flag plot_grid can be set to true to show an animation of the first 1000 steps
@author: Johan Öhman
"""
#import nececcery packatges
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


plot_grid = False


"""
Define neccecary functions

"""

def phi(U,N):                               #Define function Phi that chooses uniformly which vertex to choose
    A = np.cumsum( np.ones((1,N))/N)        #Compute intervals 
    for ii in range(0,N-1):                 #Loop to find the state
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
    
#Define function that computes the number of ones on the grid
def sum_points(Grid):
    s = np.sum(Grid)
    return s


if plot_grid:           #Set smaller value for grid and time steps, and alsoo initiate figure if animation is desired
    N_grid = 8
    N_step = 1000
    frames = []
    fig = plt.figure(1)

else: 
    N_grid = 40                 #Set desired size and time step here
    N_step = 100000
Grid = np.zeros((N_grid+2,N_grid+2))
n_save = np.zeros(N_step)

for ii in range(1,N_step):
    #print(ii)
    U = np.random.rand()                                #Sample uniformly
    si  = phi(U,N_grid**2)                              #Calculate point
    si_unrav = np.unravel_index(si,(N_grid,N_grid))     #Change one-valued index to two-valued
    
    row = si_unrav[0]+1
    col = si_unrav[1]+1
    
    U_a = np.random.rand()                                  #Sample for acceptence
    if U_a > 0.5:
        Grid[row,col] = CheckNeighbours(row,col,Grid)
        
    if plot_grid:
        im = plt.imshow(Grid, animated=True)
        frames.append([im])
        
    n_save[ii] = sum_points(Grid)
#print(n_save[-1])
plt.show()   
#plt.plot(range(0,N_step),n_save/N_grid**2)
#plt.show()
n_save_cum = np.cumsum(n_save)              #Compute cumulative sum
plt.figure(2)
plt.clf()
plt.plot(range(0,N_step),n_save_cum/(1.+ np.array(range(0,N_step))))
plt.xlabel("N")
plt.ylabel("$E(n(x))$")
plt.title("Convergens for "+str(N_grid)+"x"+str(N_grid)+" grid")
plt.show()
plt.grid()

if plot_grid:
    ani = animation.ArtistAnimation(fig, frames, interval=50, blit=True,repeat_delay=1000)
    plt.show()

    
    

