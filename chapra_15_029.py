#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 19:56:47 2020

@author: mikekeohane
"""

import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt

T = np.array([50, 60, 70, 80, 90, 100, 110, 120, 130])
p = np.array([82, 2300, 18500, 80500, 2.3 * (10**5), 5*10**5, 9.6* 10**5, 1.5*10**6, 2.4*10**6])

Tk = T + 273

Tmodel = np.linspace(Tk[0]-10, Tk[-1]+10, 100)

def yfun(x, *coefs):
    return coefs[0] - (coefs[1]/(coefs[2]+x))

popt = opt.curve_fit(yfun, Tk, np.log(p), [10, 200, 6])[0]
print(popt)


def calc_stats(y, yhat, to_print=True):
    # Calculate statistics
    st = np.sum((y - np.mean(y)) ** 2)
    sr = np.sum(((y) - yhat) ** 2)
    r2 = (st - sr) / st
    if to_print:
        print("st: {:.3e}\nsr: {:.3e}\nr2: {:.3e}".format(st, sr, r2))
    return st, sr, r2

phat = popt[0] - (popt[1]/(popt[2]+Tk))
pmodel = popt[0] - (popt[1]/(popt[2]+Tmodel))

s = calc_stats(np.log(p), phat)
sy = np.sqrt(s[1]/(len(p)-3))

print("sT/ln(p): {:0.3e}".format(sy))

fig = plt.figure(num=1, clear=True)
ax = fig.subplots(1,1)

ax.plot(Tk, np.log(p), "ch")
ax.plot(Tmodel,pmodel, "k--")
ax.set(ylabel="ln(p)", xlabel='T, Kelvin')
ax.grid(True)
fig.tight_layout()

fig.savefig("chapra_15_029.png")


