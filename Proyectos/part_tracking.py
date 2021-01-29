#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 10:28:21 2019

@author: luiggi
"""

import numpy as np
import matplotlib.pyplot as plt

def drawVectorField(A = 1.0, alpha = 2.0, lx = 1, ly = 1, nx = 11, ny = 11):
    xg, yg =np.meshgrid(np.linspace(0,lx,nx),np.linspace(0,ly,ny))
    u = -A * np.cos(np.pi * alpha * yg) * np.sin(np.pi * alpha * xg)
    v =  A * np.sin(np.pi * alpha * yg) * np.cos(np.pi * alpha * xg)
    
    plt.quiver(xg, yg, u, v)

def velocity(x, y, A = 1.0, alpha = 2.0):
    u = -A * np.cos(np.pi * alpha * y) * np.sin(np.pi * alpha * x)
    v =  A * np.sin(np.pi * alpha * y) * np.cos(np.pi * alpha * x) 
    return (u,v)

def initialPos(N = 10, seed = 2):
    np.random.seed(seed)
    return np.random.random((N, 2))

def Euler(x_y, dt, f):
    x, y = x_y
    u, v = f(x, y)
    return (x + dt * u, y + dt * v)
    
plt.figure(figsize=(3,3))

drawVectorField()

x0 = initialPos(N = 10, seed = 3)

plt.plot(x0[:,0], x0[:,1], 'ro')

dt = 0.01

Nt = 100
for t in range(Nt):
    for i, x in enumerate(x0):
        xn, yn = Euler(x, dt, velocity)
        plt.plot(xn, yn, 'b.')
        x0[i,0] = xn
        x0[i,1] = yn

plt.show()
