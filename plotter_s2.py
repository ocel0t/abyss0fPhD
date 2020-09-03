# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 11:24:01 2018

@author: Nagy Tamás Milán

SCRIPT for making S2 plots
"""
import pylab as pylab
import numpy as np


xsteps = [] 
for i in range(1,38):
    xsteps.append(i)
    
'''
Defining INPUTS
'''

data1 = np.loadtxt("ired_result_wt.out", usecols= [0], unpack = True)
data2 = np.loadtxt("ired_result_var3.out", usecols= [0],unpack = True)
data3 = np.loadtxt("ired_result_var4.out", usecols= [0],unpack = True)
#data4 = np.loadtxt("ired_average_var8", usecols= [0],unpack = True)

'''
Skipping 4th point aby making it to contain no data (optional)
'''
data1 = np.ndarray.tolist(data1)
data1 = data1[:3] + [None] + data1[3:]
data2 = np.ndarray.tolist(data2)
data2 = data2[:3] + [None] + data2[3:]
data3 = np.ndarray.tolist(data3)
data3 = data3[:3] + [None] + data3[3:]
#data4 = np.ndarray.tolist(data4)
#data4 = data4[:3] + [None] + data4[3:]
# =============================================================================

'''
Creating figure
'''

pylab.figure('1')
pylab.clf()
pylab.plot(xsteps,data1, label='wt')
pylab.plot(xsteps,data2, label='var3')
pylab.plot(xsteps,data3, label='var4')
#pylab.plot(xsteps,data4, label='var8')
#pylab.title("S2")
pylab.xlabel('residues' , fontweight='bold')
pylab.ylabel('$\mathregular{S^2}$' , fontweight='bold')
pylab.legend(loc = 'lower left')
pylab.ylim(0.0,1.0)
pylab.savefig('s2.png', dpi = 600)



    