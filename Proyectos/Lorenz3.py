#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 12:30:30 2019

@author: luiggi
"""

import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import time
import ODE_RAUGM as ode
        
def update_lines(num, lines, trace):
    for line, data in zip(lines, trace):
        # Observación: No existe la función set_data() para datos en 3D.
        line.set_data(data[0:2, 0:num])          # x, y
        line.set_3d_properties(data[2, 0:num])   # z
    return lines

N = 10 # Número de trayectorias en el espacio fase    
Nt = 50 # Número total de pasos
dt = 0.01 # Stepsize

#Posiciones iniciales aleatorias
np.random.seed(1)
x0 = -15 + 30 * np.random.random((N, 3))

print(x0.shape)
print(x0)

# Arreglos para las trayectorias
trace = np.zeros((N,3,Nt))

trace[:, :, 0] = x0

# Attaching 3D axis to the figure
fig = plt.figure()
ax = p3.Axes3D(fig)
ax.plot(x0[:,0], x0[:,1], x0[:,2], 'k.') # condicion inicial

# Solución de las ecs. de Lorenz
t1_start = time.perf_counter()
for t in range(1,Nt):
    x0 = np.asarray([ode.RK4(x, dt, ode.lorenz_deriv) for x in x0])
    for j,x in enumerate(x0):
        trace[j,:,t] = x0[j,:]
t1_stop = time.perf_counter()
print('\n[{}] \n Solver CPU Time: {:0.6f} \n '.format(time.ctime(), t1_stop-t1_start))

lines = [ax.plot(dat[0, 0:1], dat[1, 0:1], dat[2, 0:1])[0] for dat in trace]

print(type(lines),len(lines))
[print(type(l), l) for l in lines]


ax.set_xlim3d([-100, 100])
ax.set_xlabel('X')

ax.set_ylim3d([-100, 100])
ax.set_ylabel('Y')

ax.set_zlim3d([-100, 100])
ax.set_zlabel('Z')

ax.set_title('Ecuaciones de Lorenz')

#
from matplotlib.animation import FuncAnimation
#
# Creación del objeto de animación
line_ani = FuncAnimation(fig, 
                         update_lines, 
                         Nt, 
                         fargs=(lines, trace),
                         interval=100, 
                         repeat=False)

plt.show()





