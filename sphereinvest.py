#!/usr/bin/python
# -*- coding: utf-8 -*-

# This script calculates contacts within a 5 Angström sphere
# NTM 2020

import pytraj as pt
import numpy as np

pdb = "Gal-3-DSeDG-refmac48_H_nowater.pdb"
traj = pt.load(pdb, top=pdb)

lista2 = []
f = open(pdb, "r")
for x in f:
   lista2.append(x[-3])

f.close()

sel_atom = raw_input("Select an atom, center for the 5 Angström sphere: [number] ") # atom
#sel_start = int(raw_input("Select the starting residue: [48] "))
#sel_end = int(raw_input("Select the last residue: [2353] "))
sel_start = 98  # atom
sel_end = 2412 # atom

lista = []
lista.append("CENTER ATOM " + str(sel_atom))
MagicDensity = 0

for i in range(sel_start,sel_end,1):  
   if lista2[i-1] == "H":
      mask = "@" + str(sel_atom) + " @" + str(i) 
      dist = pt.distance(traj, mask)
      element = dist.tolist()
      if element[0] <5.01:
         lista.append("ATOM " + str(i))
         lista.append("DISTANCE " + str(element[0]))
         MagicDensity += element[0]**(1./3)

   
print(lista)

print("MAGICDENSITY: " + str(MagicDensity))

with open('sphereinvest_contacts.out', 'a') as f:
    for item in lista:
        print >> f, item

result = "MagicDensity for ligand ATOM " + sel_atom + " " + "*** " + str(round(MagicDensity,2)) + " ***" 
with open('sphereinvest_density.out', 'a') as f:
    print >> f, result


