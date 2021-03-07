#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 15:33:52 2020

@author: mikekeohane
"""

import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt

I = [50, 80, 130, 200, 250, 350, 450, 550, 700]
P = [99, 177, 202, 248, 229, 219, 173, 142, 72]

Imodel = np.linspace(25, 725, 100)



def yfun(x, *coefs):
    return coefs[0] * (x/coefs[1]) * np.exp(-x/coefs[1] + 1)

popt = opt.curve_fit(yfun, I, P, [250, 229])[0]
print(popt)

def calc_stats(y, yhat, to_print=True):
    # Calculate statistics
    st = np.sum((y - np.mean(y)) ** 2)
    sr = np.sum((y - yhat) ** 2)
    r2 = (st - sr) / st
    if to_print:
        print("st: {:.3e}\nsr: {:.3e}\nr2: {:.3e}".format(st, sr, r2))
    return st, sr, r2


Phat = popt[0] * (np.array(I)/popt[1]) * np.exp(-np.array(I)/popt[1] + 1)
calc_stats(P, Phat)

Pmodel = popt[0] * (Imodel/popt[1]) * np.exp(-Imodel/popt[1] + 1)

fig = plt.figure(num=1, clear=True)
ax = fig.subplots(1,1)

ax.plot(I, P, "rd", label="Data")
ax.plot(Imodel, Pmodel, "g-", label="model")
ax.set(ylabel='P, mg $m^{-3}$ $d^{-1}$', xlabel='I, $\mu$E $m^{-2}$ $s^{-1}$')
ax.grid(True)
ax.legend(loc="best")
fig.tight_layout()


fig.savefig("chapra_15_011.png")