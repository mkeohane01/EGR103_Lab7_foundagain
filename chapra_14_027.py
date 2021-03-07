#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 14:27:36 2020

@author: mikekeohane
"""

import numpy as np
import matplotlib.pyplot as plt

V = [2, 3, 4, 5, 7, 10]
i = [5.2, 7.8, 10.7, 13, 19.3, 27.5]

Vmodel = np.linspace(0,10,100)

p = np.polyfit(V, i, 1)
print("p: {}".format(p))


def yfun(xe, *coefs):
    return coefs[0] * xe**1 #+ coefs[1]


# Reshape data for block matrices
Vv = np.reshape(V, (-1, 1))
iv = np.reshape(i, (-1, 1))
phi_mat = np.block([Vv**1])
pvec = np.linalg.lstsq(phi_mat, iv, rcond=None)[0]
print("pvec: {}".format(pvec))


imodel = yfun(Vmodel,pvec[0])

pmodel = p[0] * Vmodel + p[1]

i2 = np.polyval(p, 2)
print("i2: {}".format(i2))
i3 = pvec[0][0] * 3 
print("i3: {}".format(i3))


fig = plt.figure(num=1, clear=True)
ax = fig.subplots(1,1)

ax.plot(Vmodel, imodel, "r--", label="Zero-intercept")
ax.plot(V, i, "ko", label="Data")
ax.plot(Vmodel, pmodel, "b-", label="polyfit")
ax.set(ylabel='v, V', xlabel='i, A')
ax.grid(True)
ax.legend(loc="best")
fig.tight_layout()


fig.savefig("chapra_14_027.png")