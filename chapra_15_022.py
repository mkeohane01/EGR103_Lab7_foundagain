#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 19:36:51 2020

@author: mikekeohane
"""

import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt

x = [0.5, 1, 2, 3, 4]
y = [10.4, 5.8, 3.3, 2.4, 2]

xmodel = np.linspace(0, 5, 100)



def yfun(x, *coefs):
    return ((coefs[0] + np.sqrt(x))/(coefs[1]*np.sqrt(x)))**2

popt = opt.curve_fit(yfun, x, y, [2, 3.3])[0]
print(popt)

print('y(1.6): {}'.format(((popt[0] + np.sqrt(1.6))/(popt[1]*np.sqrt(1.6)))**2))

#yhat = yfun(x,popt)
yhat = ((popt[0] + np.sqrt(x))/(popt[1]*np.sqrt(x)))**2
#ymodel = yfun(xmodel, popt)
ymodel = ((popt[0] + np.sqrt(xmodel))/(popt[1]*np.sqrt(xmodel)))**2

def calc_stats(y, yhat, to_print=True):
    # Calculate statistics
    st = np.sum((y - np.mean(y)) ** 2)
    sr = np.sum((y - yhat) ** 2)
    r2 = (st - sr) / st
    if to_print:
        print("st: {:.3e}\nsr: {:.3e}\nr2: {:.3e}".format(st, sr, r2))
    return st, sr, r2

calc_stats(y, yhat)

fig = plt.figure(num=1, clear=True)
ax = fig.subplots(1,1)

ax.plot(x, y, "ms")
ax.plot(xmodel, ymodel, "y-")
ax.set(ylabel="y", xlabel='x')
ax.grid(True)
fig.tight_layout()

fig.savefig("chapra_15_022.png")

