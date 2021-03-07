#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 15:34:16 2020

@author: mikekeohane
"""

import numpy as np

t = [0.5, 1, 2, 3, 4, 5, 6, 7, 9]
p = [6, 4.4, 3.2, 2.7, 2, 1.9, 1.7, 1.4, 1.1]





def yfun(xe, *coefs):
    return coefs[0] * np.exp(-1.5*xe) + coefs[1] * np.exp(-0.3*xe) + coefs[2] * np.exp(-0.05*xe)
# Reshape data for block matrices
xv = np.reshape(t, (-1, 1))
yv = np.reshape(p, (-1, 1))
phi_mat = np.block([[np.exp(-1.5*xv), np.exp(-0.3*xv), np.exp(-0.05*xv)]])
pvec = np.linalg.lstsq(phi_mat, yv, rcond=None)[0]

print("A: {} \nB: {} \nC: {}".format(pvec[0][0],pvec[1][0],pvec[2][0]))



def calc_stats(y, yhat, to_print=True):
    # Calculate statistics
    st = np.sum((y - np.mean(y)) ** 2)
    sr = np.sum((y - yhat) ** 2)
    r2 = (st - sr) / st
    if to_print:
        print("st: {:.3e}\nsr: {:.3e}\nr2: {:.3e}".format(st, sr, r2))
    return st, sr, r2

phat = pvec[0][0] * np.exp(-1.5*np.array(t)) + pvec[1][0] * np.exp(-0.3*np.array(t)) + pvec[2][0] * np.exp(-0.05*np.array(t))
calc_stats(p, phat, True)