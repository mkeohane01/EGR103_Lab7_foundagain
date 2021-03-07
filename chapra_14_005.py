"""
Created on Tue Apr  7 11:28:05 2020

@author: mikekeohane
"""

import numpy as np
import matplotlib.pyplot as plt

x = [0, 2, 4, 6, 9, 11, 12, 15, 17, 19]
y = [5, 6, 7, 6, 9, 8, 8, 10, 12, 12]

py = np.polyfit(x, y, 1)
px = np.polyfit(y, x, 1)

yhat = np.polyval(py, x)
xhat = np.polyval(px, y)

def calc_stats(y, yhat, to_print=True):
    # Calculate statistics
    st = np.sum((y - np.mean(y)) ** 2)
    sr = np.sum(((y) - yhat) ** 2)
    r2 = (st - sr) / st
    if to_print:
        print("st: {:.3e}\nsr: {:.3e}\nr2: {:.3e}".format(st, sr, r2))
    return st, sr, r2

(sty, sry, r2y) = calc_stats(y, yhat, False)
sy = np.sqrt(sry/(len(y)-2))
ry = np.sqrt(r2y)

(stx, srx, r2x) = calc_stats(x, xhat, False)
sx = np.sqrt(srx/(len(x)-2))
rx = np.sqrt(r2x)

print("For y/x: \nIntercept: {:0.3e} Slope: {:0.3e}".format(py[1], py[0]))
print("Standard Error: {:0.3e} \nr: {:0.3e}".format(sy,ry))

print("For x/y: \nIntercept: {:0.3e} Slope: {:0.3e}".format(px[1], px[0]))
print("Standard Error: {:0.3e} \nr: {:0.3e}".format(sx,rx))

xmodel = np.linspace(0, 20, 100)
ypolymodel = np.polyval(py, xmodel)

ymodel = np.linspace(5, 12, 100)
xpolymodel = np.polyval(px, ymodel)

fig = plt.figure(num=1, clear=True)
ax = fig.subplots(2,1)

def make_plot(x, y, yhat, xmodel, ymodel, fig_num=1):
    ax[fig_num-1].plot(x, y, "ko", label="Data")
    ax[fig_num-1].plot(x, yhat, "ks", label="Estimates", mfc="none")
    ax[fig_num-1].plot(xmodel, ymodel, "k-", label="Model")
    ax[fig_num-1].grid(True)
    ax[fig_num-1].legend(loc="best")
    if fig_num == 1:
        ax[0].set(xlabel='x', ylabel='y')
    else:
        ax[1].set(xlabel='y', ylabel='x')
    fig.tight_layout()
    return fig, ax

make_plot(x, y, yhat, xmodel, ypolymodel, 1)
make_plot(y, x, xhat, ymodel, xpolymodel, 2)

fig.savefig("chapra_14_005.png")