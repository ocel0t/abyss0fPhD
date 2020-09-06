# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 14:13:03 2019

@author: Nagy Tamás Milán

Calculates population of secondary structures in trajectory by analysing VMD SS timeline output
"""

import numpy as np
from array import *


col4 = np.genfromtxt("37aa_var4_concat_stride",usecols=(4),delimiter=' ', dtype=None)

ss_list = col4.tolist()
ss_list2 = []

for i in ss_list:
    ss_list2.append(i.decode("utf-8"))
    
countT = 0
countH = 0
countG = 0 
countC = 0
countB = 0
countE = 0
countAll = 0
nocount =[]
for i in ss_list2:
    if "T" in i:
        countT +=1
    elif "H" in i:
        countH +=1
    elif "G" in i:
        countG +=1
    elif "C" in i:
        countC +=1
    elif "B" in i:
        countB += 1
    elif "E" in i:
        countE += 1
    else:
        nocount.append(i)
    countAll += 1
        
print(nocount)

print("### Results ###")
print("T= " + str(countT/countAll))
print("H= " + str(countH/countAll))
print("G= " + str(countG/countAll))      
print("C= " + str(countC/countAll))
print("B= " + str(countB/countAll))
print("E= " + str(countE/countAll))

    
