#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 16:57:20 2017

@author: luiggi
"""
import numpy as np
import pylab as pl
from mpl_toolkits.mplot3d import Axes3D

Nt = 50
Ny = 50

a = 0
b = 2
ay = -5
by = 5
t = np.linspace(a,b,Nt)
y = np.linspace(ay,by,Ny)
xg,yg = np.meshgrid(t,y)

def f(x,y):
    return 1 + t * np.sin(t*y)

u = f(xg,yg)

pl.contourf(xg,yg,u,5,alpha=.75,cmap=pl.cm.hot)
C = pl.contour(xg,yg,u,5, colors='black', linewidth=.5)
pl.clabel(C,inline=1,fontsize=10)
pl.xlabel('$t$')
pl.ylabel('$y(t)$')
pl.grid()
pl.xlim(a - 0.2,b + 0.2)
pl.ylim(ay - 0.2, by + 0.2)

fig = pl.figure()
ax = Axes3D(fig)
ax.plot_surface(xg,yg,u, rstride=1, cstride=1, alpha=.85,cmap=pl.cm.hot)
ax.contour(xg,yg,u,5, colors='black', linewidth=.5)

ax.set_zlim(-2,3)

pl.xlabel('$t$')
pl.ylabel('$y(t)$')

pl.show()
