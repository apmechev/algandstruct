#!/usr/bin/env python
import subprocess
import numpy as np      #np.arange
def plot_bif(x0,rmin,rmax,rstep,n,k):
    '''
    x0=the starting x point
    rmin,rmax,rstep= the min max and stride of the parameter
    n=number of iterations for each r,
    k=number of points to discard at the beginning
    '''
    for r in np.arange(rmin,rmax,rstep):
        i=k
        while i<n:
            x=subprocess.Popen( ["../../c++/logistic",str(x0),str(r),str(i)] ,stdout=subprocess.PIPE).communicate()
            print(r,float(x[0].strip('\n')))
            i+=1

plot_bif(0.4,1.0,3.9,0.01,131,100)
