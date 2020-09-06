# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 09:43:20 2019

@author: Nagy Tamás Milán

Creates chart with points.
Reads data from second column of the data file.
"""

import numpy as np
import matplotlib.pyplot as plt
import os
from glob import glob

name = "fileName.extension"
currDir = os.getcwd()
files_list = glob(os.path.join(currDir , name))

store = {}
key = 1
var = 0
for i in files_list:
    var = np.loadtxt(i, usecols=[1])
    store.update( { key : var } )
    key += 1

x = np.linspace(0,10000,3000)

for i in store:
    plt.plot(x, store[i],'.')

#plt.title('A tale of 2 subplots')
plt.ylabel('RoG')
plt.xlabel('time')

plt.savefig('points.png', dpi=600)


plt.show()