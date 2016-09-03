#!/usr/bin/env python
import subprocess
import numpy as np      #np.arange
import matplotlib.pyplot as plt
def plot_bif(x0,rmin,rmax,rstep,n,k):
    '''
    x0=the starting x point
    rmin,rmax,rstep= the min max and stride of the parameter
    n=number of iterations for each r,
    k=number of points to discard at the beginning
    '''
    rs=[]
    ys=[]
    for r in np.arange(rmin,rmax,rstep):
        i=k
        while i<n:
            x=subprocess.Popen( ["../../c++/logistic",str(x0),str(r),str(i)] ,stdout=subprocess.PIPE).communicate()
            output=x[0].decode()
            y=float(output)
            rs.append(r)
            ys.append(y)

            i+=1
    plt.scatter(rs,ys,s=1,c='k',alpha=0.5)
    plt.title("Bifurication plot of the Logistics map, varying R")
    plt.xlabel("R")
    plt.ylabel("Attractor")
    plt.show()
plot_bif(0.2,2.4,4.5,0.001,1000,805)
