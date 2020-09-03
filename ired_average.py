# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 10:51:36 2019

@author: Nagy Tamás Milán
"""
import numpy as np
import sys, os
from glob import glob

'''
creating list of .out files of the working directory (all .out files!!!)
'''

name = "*.out"
currDir = os.getcwd()
files_list = glob(os.path.join(currDir , name))

print("creating list of .out files of the working directory...OK")

'''
reading data into dictionary
'''
store = {}
key = 1
var = 0
for i in files_list:
    var = np.loadtxt(i, skiprows=1, usecols=[0])
    store.update( { key : var } )
    key += 1

print("reading data into dictionary...OK")


fileResult= open("ired_average", 'w')
fileResult.write("### Average values of order parameters per residue ### \n")
fileResult.write(" \n")

'''
averaging S2 values of the residues
writing values to file
'''
numRes = 36 #proline 4!

for x in range(1,numRes+1): #numRES+1
    var2 = 0
    for i in range(1, len(store)+1):
        var2 += store[i][x-1]
    var2 /= len(store)
    fileResult.write(str(round(var2,3)) + "\n")

print("averaging S2 values of the residues...OK")
fileResult.close()  
print("writing values to file...OK")  