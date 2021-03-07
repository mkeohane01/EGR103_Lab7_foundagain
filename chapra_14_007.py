#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 14:10:21 2020

@author: mikekeohane
"""

import numpy as np


T = [-40, 0, 40, 80, 120, 160] #Celcius
p = [6900, 8100, 9350, 10500, 11700, 12800] #N/m^2
n = 1000 / 28 #moles
Tk = [] #Kelvin
for t in T:
    Tk += [t + 273]
V = 10 #m^3

xv = np.reshape(Tk, (-1, 1))
yv = np.reshape(p, (-1, 1))
phi_mat = np.block([[xv**1, xv**0]])
pvec = np.linalg.lstsq(phi_mat, yv, rcond=None)[0]
print("pvec: {},{}".format(pvec[0][0],pvec[1][0]))

R = pvec[0] * (V/n)

print(R[0])
