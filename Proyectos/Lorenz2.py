#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 11:54:15 2019

@author: luiggi
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time 
import ODE_RAUGM as ode

N = 10 # Número de trayectorias en el espacio fase    
Nt = 100 # Número total de pasos
dt = 0.01 # Stepsize

#Posiciones iniciales aleatorias
np.random.seed(1)
x0 = -15 + 30 * np.random.random((N, 3))

# Arreglos para las trayectorias
trace = np.zeros((N, 3, Nt))

trace[:, :, 0] = x0

# Figura
fig = plt.figure();
ax = fig.add_axes([0, 0, 1, 1], projection='3d');
ax.plot(x0[:,0], x0[:,1], x0[:,2], 'k.') # condicion inicial

# Solución de las ecs. de Lorenz
t1_start = time.perf_counter()
for t in range(1,Nt):
    x0 = np.asarray([ode.RK4(x, dt, ode.lorenz_deriv) for x in x0])
    for j,x in enumerate(x0):
        trace[j,:,t] = x0[j,:]
t1_stop = time.perf_counter()
print('[{}] \n Solver CPU Time: {:0.6f} \n '.format(time.ctime(), t1_stop-t1_start))

for i in range(N):
    ax.plot(trace[i,0,:], trace[i,1,:], trace[i,2,:], '-', lw='0.75')

plt.show()
