#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 14:51:39 2019

@author: luiggi
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def lorenz_deriv(x_y_z, sigma=10.0, beta=8./3, rho=28.0):
    '''
    Cálculo de las ecuaciones de Lorenz
    '''
    x, y, z = x_y_z
    return [sigma * (y - x), x * (rho - z) - y, x * y - beta * z]


N = 10 # Número de trayectorias en el espacio fase    
Nt = 100 # Número total de pasos
dt = 0.01 # Stepsize

#Posiciones iniciales aleatorias
np.random.seed(1)
x0 = -15 + 30 * np.random.random((N, 3))

# Figura
fig = plt.figure();
ax = fig.add_axes([0, 0, 1, 1], projection='3d');
ax.plot(x0[:,0], x0[:,1], x0[:,2], '.') # condicion inicial

# Solución de las ecs. de Lorenz usando el método de Euler
for t in range(Nt):
    fx = np.asarray([lorenz_deriv(x) for x in x0])
    x0 = x0 + dt * fx
    ax.plot(x0[:,0], x0[:,1], x0[:,2], '.')

plt.show()


